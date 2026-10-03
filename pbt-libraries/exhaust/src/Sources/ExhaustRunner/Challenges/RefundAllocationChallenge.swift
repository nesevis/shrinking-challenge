import Exhaust

/// Processing fees are non-refundable, so proportional refunds use net balances.
/// Leftover cents go to the largest fractional remainders, breaking ties by input order.
enum RefundAllocationChallenge {
    static let processingFeeCents = 30

    @Exhaustable
    struct Charge: Equatable, Sendable {
        let paidCents: Int

        var refundableCents: Int128 {
            Int128(self.paidCents) - Int128(RefundAllocationChallenge.processingFeeCents)
        }
    }

    @Exhaustable
    struct RefundRequest: Equatable, Sendable, CustomStringConvertible {
        let charges: [RefundAllocationChallenge.Charge]
        let refundCents: Int

        var description: String {
            "\(Self.self)(\(self.charges.map(\.paidCents)), \(self.refundCents))"
        }
    }

    // MARK: - Generators

    // Twenty charges is a shared benchmark resource bound, not a monetary bound.
    static let chargeLimit = 20
    static let gen: ReflectiveGenerator<RefundRequest> = {
        let charge = #gen(.int(in: (processingFeeCents + 1)...Int.max)).map {
            Charge(paidCents: $0)
        }
        let charges = #gen(charge.array(length: 1...chargeLimit))
        return charges.bind { charges in
            let total = totalRefundable(charges)
            let maximumRefund = Int(min(total, Int128(Int.max)))
            return #gen(.int(in: 0...maximumRefund)).map {
                RefundRequest(charges: charges, refundCents: $0)
            }
        }
    }()

    // Intentionally raw: no domain settings, overrides, repair, or filtering.
    static let derivedGen = RefundRequest.gen()

    // MARK: - Contract

    static func totalRefundable(_ charges: [Charge]) -> Int128 {
        charges.reduce(Int128(0)) { $0 + $1.refundableCents }
    }

    static func isValid(_ request: RefundRequest) -> Bool {
        guard
            (1...chargeLimit).contains(request.charges.count),
            request.charges.allSatisfy({ $0.paidCents > processingFeeCents }),
            request.refundCents >= 0
        else {
            return false
        }
        return Int128(request.refundCents) <= totalRefundable(request.charges)
    }

    /// Widened products of two nonnegative Int-sized amounts fit exactly in Int128.
    static func satisfiesContract(_ request: RefundRequest, allocations: [Int]) -> Bool {
        guard isValid(request), allocations.count == request.charges.count else {
            return false
        }
        let total = totalRefundable(request.charges)
        let refund = Int128(request.refundCents)
        guard allocations.reduce(Int128(0), { $0 + Int128($1) }) == refund else {
            return false
        }

        var remainders = [Int128]()
        var roundedUp = [Bool]()
        for (charge, allocation) in zip(request.charges, allocations) {
            let actual = Int128(allocation)
            guard actual >= 0, actual <= charge.refundableCents else {
                return false
            }
            let numerator = refund * charge.refundableCents
            let floor = numerator / total
            let remainder = numerator % total
            let ceiling = floor + (remainder == 0 ? 0 : 1)
            guard actual == floor || actual == ceiling else {
                return false
            }
            remainders.append(remainder)
            roundedUp.append(actual > floor)
        }

        // An unrounded charge must never outrank one that received an extra cent.
        for recipient in allocations.indices where roundedUp[recipient] {
            for other in allocations.indices where roundedUp[other] == false {
                if remainders[other] > remainders[recipient]
                    || (remainders[other] == remainders[recipient] && other < recipient)
                {
                    return false
                }
            }
        }
        return true
    }

    static let property: @Sendable (RefundRequest) throws -> Bool = { request in
        guard isValid(request) else {
            throw PropertySkip()
        }
        return satisfiesContract(request, allocations: allocateRefund(request))
    }

    // MARK: - Deliberately Faulty Allocator

    static func allocateRefund(_ request: RefundRequest) -> [Int] {
        // Deliberate bug: use gross payments as weights, retaining non-refundable fees.
        let total = request.charges.reduce(Int128(0)) { $0 + Int128($1.paidCents) }
        let numerators = request.charges.map {
            Int128(request.refundCents) * Int128($0.paidCents)
        }
        var allocations = numerators.map { Int($0 / total) }
        let allocated = allocations.reduce(Int128(0)) { $0 + Int128($1) }
        let remaining = Int(Int128(request.refundCents) - allocated)
        let priority = numerators.indices.sorted {
            let left = numerators[$0] % total
            let right = numerators[$1] % total
            return left == right ? $0 < $1 : left > right
        }
        for index in priority.prefix(remaining) {
            allocations[index] += 1
        }
        return allocations
    }
}
