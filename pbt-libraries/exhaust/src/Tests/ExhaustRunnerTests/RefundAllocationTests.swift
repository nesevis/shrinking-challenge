import Exhaust
import Testing
@testable import ExhaustRunner

@Suite("Refund allocation", .serialized)
struct RefundAllocationTests {
    @Test("Constructive requests respect refundable balances")
    func constructiveRequests() {
        #exhaust(RefundAllocationChallenge.gen, .budget(.extensive), .replay(1337)) { request in
            #expect(RefundAllocationChallenge.isValid(request))
            #expect(RefundAllocationChallenge.satisfiesContract(
                request, allocations: repairedAllocations(request),
            ))

            let allocations = RefundAllocationChallenge.allocateRefund(request)
            #expect(allocations.count == request.charges.count)
            #expect(allocations.reduce(Int128(0), { $0 + Int128($1) })
                == Int128(request.refundCents))

            let zeroRefund = RefundAllocationChallenge.RefundRequest(
                charges: request.charges,
                refundCents: 0,
            )
            let zeroPasses = try RefundAllocationChallenge.property(zeroRefund)
            #expect(zeroPasses)

            let firstCharge = request.charges[0]
            let singleRefund = RefundAllocationChallenge.RefundRequest(
                charges: [firstCharge],
                refundCents: Int(min(Int128(request.refundCents), firstCharge.refundableCents)),
            )
            let singlePasses = try RefundAllocationChallenge.property(singleRefund)
            #expect(singlePasses)

            let equalRefund = RefundAllocationChallenge.RefundRequest(
                charges: request.charges.map { _ in firstCharge },
                refundCents: Int(min(
                    Int128(request.refundCents),
                    firstCharge.refundableCents * Int128(request.charges.count),
                )),
            )
            let equalPasses = try RefundAllocationChallenge.property(equalRefund)
            #expect(equalPasses)

            let total = RefundAllocationChallenge.totalRefundable(request.charges)
            if total <= Int128(Int.max) {
                let fullRefund = RefundAllocationChallenge.RefundRequest(
                    charges: request.charges,
                    refundCents: Int(total),
                )
                #expect(repairedAllocations(fullRefund)
                    == request.charges.map { Int($0.refundableCents) })
            }
        }
    }

    @Test("Raw derivation preserves valid contracts and skips invalid requests")
    func derivedRequests() {
        #exhaust(RefundAllocationChallenge.derivedGen, .budget(.extensive), .replay(1337)) {
            request in
            if RefundAllocationChallenge.isValid(request) {
                #expect(RefundAllocationChallenge.satisfiesContract(
                    request, allocations: repairedAllocations(request),
                ))
            } else {
                var skipped = false
                do {
                    _ = try RefundAllocationChallenge.property(request)
                } catch is PropertySkip {
                    skipped = true
                }
                #expect(skipped)
            }
        }
    }

    @Test("Conservation rejects dropped allocations and incorrect refund totals")
    func rejectsBrokenAllocations() {
        #exhaust(RefundAllocationChallenge.gen, .budget(.extensive), .replay(42)) { request in
            var allocations = repairedAllocations(request)
            allocations.removeLast()
            #expect(RefundAllocationChallenge.satisfiesContract(
                request, allocations: allocations,
            ) == false)

            allocations = repairedAllocations(request)
            allocations[0] += allocations[0] == Int.max ? -1 : 1
            #expect(RefundAllocationChallenge.satisfiesContract(
                request, allocations: allocations,
            ) == false)
        }
    }

    @Test("Remainder priority and stable ties use net balances", arguments: [1, 2])
    func remainderPriority(firstBalanceMultiplier: Int) {
        let scales = #gen(.int(in: 1...(Int.max - RefundAllocationChallenge.processingFeeCents) / 3))
        let gen = scales.mapped(
            forward: { scale in
                RefundAllocationChallenge.RefundRequest(
                    charges: [
                        .init(paidCents: firstBalanceMultiplier * scale
                            + RefundAllocationChallenge.processingFeeCents),
                        .init(paidCents: scale + RefundAllocationChallenge.processingFeeCents),
                    ],
                    refundCents: 1,
                )
            },
            backward: {
                Int($0.charges.last?.refundableCents ?? 1)
            },
        )
        #exhaust(gen, .budget(.extensive), .replay(42)) { request in
            #expect(RefundAllocationChallenge.satisfiesContract(request, allocations: [1, 0]))
            #expect(RefundAllocationChallenge.satisfiesContract(
                request, allocations: [0, 1],
            ) == false)
        }
    }

    @Test(
        "Known fee imbalance remains failing through both generators",
        arguments: [Challenge.refundAllocation, .refundAllocationDerived],
    )
    func feeImbalance(challenge: Challenge) throws {
        let gen = challenge == .refundAllocation
            ? RefundAllocationChallenge.gen : RefundAllocationChallenge.derivedGen
        let input = RefundAllocationChallenge.RefundRequest(
            charges: [.init(paidCents: 31), .init(paidCents: 33)],
            refundCents: 4,
        )
        let reduced = #exhaust(
            gen,
            reflecting: input,
            .budget(.extensive),
            .suppress(.all),
            property: RefundAllocationChallenge.property,
        )
        let counterexample = try #require(reduced)
        #expect(RefundAllocationChallenge.isValid(counterexample))
        let passes = try RefundAllocationChallenge.property(counterexample)
        #expect(passes == false)
        #expect(RefundAllocationChallenge.allocateRefund(input) == [2, 2])
        #expect(repairedAllocations(input) == [1, 3])
    }

    @Test(
        "Both registered runner paths discover the fee-weighting defect",
        arguments: [Challenge.refundAllocation, .refundAllocationDerived],
        [UInt64(0), 1, 42, 1337, 2026],
    )
    func runnerDetectsDefect(challenge: Challenge, seed: UInt64) async {
        let stats = await ChallengeRunner.run(challenge, seed: seed, iterations: 1)
        #expect(challenge.isCustom)
        #expect(challenge.reflectsInput == false)
        #expect(stats.missed == 0)
        #expect(stats.entries.count == 1)
        #expect(stats.entries.first?.seed == seed)
    }
}

// MARK: - Repaired Allocator for Fault-Detection Validation

private func repairedAllocations(
    _ request: RefundAllocationChallenge.RefundRequest,
) -> [Int] {
    let total = RefundAllocationChallenge.totalRefundable(request.charges)
    let numerators = request.charges.map {
        Int128(request.refundCents) * $0.refundableCents
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
