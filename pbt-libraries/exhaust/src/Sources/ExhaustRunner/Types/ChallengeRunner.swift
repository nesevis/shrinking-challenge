//
//  ChallengeRunner.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 14/4/2026.
//

import Dispatch
import Exhaust
import Foundation

enum ChallengeRunner {
    static func run(_ challenge: Challenge, seed: UInt64, iterations: UInt64) async -> Stats {
        let stats = Stats(challenge: challenge, iterations: iterations)
        
        if challenge.reflectsInput {
            switch challenge {
            case .anagrams:
                let (output, report, original, wall) = exhaustReflecting(
                    AnagramsChallenge.gen,
                    reflecting: AnagramsChallenge.input,
                    seed: seed,
                    property: AnagramsChallenge.property
                )
                let description = "(\"\(output?.0 ?? "")\", \"\(output?.1 ?? "")\")".replacingOccurrences(of: "\0", with: #"\0"#)
                stats.append(report: report, counterExample: description, seed: seed, original: original, wallMilliseconds: wall)
            case .usernamePassword:
                let (output, report, original, wall) = exhaustReflecting(
                    UsernamePasswordChallenge.gen,
                    reflecting: UsernamePasswordChallenge.input,
                    seed: seed,
                    property: UsernamePasswordChallenge.property
                )
                let description = "(\"\(output?.0 ?? "")\", \"\(output?.1 ?? "")\")"
                stats.append(report: report, counterExample: description, seed: seed, original: original, wallMilliseconds: wall)
            case .duplicatedText:
                let (output, report, original, wall) = exhaustReflecting(
                    DuplicatedTextChallenge.gen,
                    reflecting: DuplicatedTextChallenge.input,
                    seed: seed,
                    property: DuplicatedTextChallenge.property
                )
                let description = "(\"\(output?.0 ?? "")\", \"\(output?.1 ?? "")\")"
                stats.append(report: report, counterExample: description, seed: seed, original: original, wallMilliseconds: wall)
            case .distinctSum:
                let (output, report, original, wall) = exhaustReflecting(
                    DistinctSumChallenge.gen,
                    reflecting: DistinctSumChallenge.input,
                    seed: seed,
                    property: DistinctSumChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)
            case .leapDay:
                let (output, report, original, wall) = exhaustReflecting(
                    LeapDayChallenge.gen,
                    reflecting: LeapDayChallenge.input,
                    seed: seed,
                    property: LeapDayChallenge.property
                )
                stats.append(report: report, counterExample: output.map { String(describing: $0) }, seed: seed, original: original, wallMilliseconds: wall)
            case .branchSwitching:
                let (output, report, original, wall) = exhaustReflecting(
                    BranchSwitchingChallenge.gen,
                    reflecting: BranchSwitchingChallenge.input,
                    seed: seed,
                    property: BranchSwitchingChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)
            case .haystack:
                let (output, report, original, wall) = exhaustReflecting(
                    HaystackChallenge.gen,
                    reflecting: HaystackChallenge.input,
                    seed: seed,
                    property: HaystackChallenge.property
                )
                stats.append(report: report, counterExample: output.map { $0.debugDescription }, seed: seed, original: original, wallMilliseconds: wall)
            case .zalgoHaystack:
                let (output, report, original, wall) = exhaustReflecting(
                    ZalgoHaystackChallenge.gen,
                    reflecting: ZalgoHaystackChallenge.input,
                    seed: seed,
                    property: ZalgoHaystackChallenge.property
                )
                stats.append(report: report, counterExample: output.map { $0.debugDescription }, seed: seed, original: original, wallMilliseconds: wall)
            default:
                break
            }
        }

        for iteration in 0 ..< iterations {
            let seed = seed + iteration
            switch challenge {
            case .binaryHeap:
                let (output, report, original, wall) = exhaust(
                    BinaryHeapChallenge.gen,
                    seed: seed,
                    property: BinaryHeapChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .bound5:
                let (output, report, original, wall) = exhaust(
                    Bound5Challenge.gen,
                    seed: seed,
                    property: Bound5Challenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .calculator:
                let (output, report, original, wall) = exhaust(
                    CalculatorChallenge.gen(depth: 5),
                    seed: seed,
                    property: CalculatorChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .coupling:
                let (output, report, original, wall) = exhaust(
                    CouplingChallenge.gen,
                    seed: seed,
                    property: CouplingChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .deletion:
                let (output, report, original, wall) = exhaust(
                    DeletionChallenge.gen,
                    seed: seed,
                    property: DeletionChallenge.property
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed, original: original, wallMilliseconds: wall)

            case .differenceNotZero:
                let (output, report, original, wall) = exhaust(
                    DifferenceChallenge.gen,
                    seed: seed,
                    property: DifferenceChallenge.notZero
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .differenceNotSmall:
                let (output, report, original, wall) = exhaust(
                    DifferenceChallenge.gen,
                    seed: seed,
                    property: DifferenceChallenge.notSmall
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .differenceNotOne:
                let (output, report, original, wall) = exhaust(
                    DifferenceChallenge.gen,
                    seed: seed,
                    property: DifferenceChallenge.notOne
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .distinct:
                let (output, report, original, wall) = exhaust(
                    DistinctChallenge.gen,
                    seed: seed,
                    property: DistinctChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)
                
            case .largeUnionList:
                let (output, report, original, wall) = exhaust(
                    LargeUnionListChallenge.gen,
                    seed: seed,
                    property: LargeUnionListChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .lengthList:
                let (output, report, original, wall) = exhaust(
                    LengthListChallenge.gen,
                    seed: seed,
                    property: LengthListChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .nestedLists:
                let (output, report, original, wall) = exhaust(
                    NestedListsChallenge.gen,
                    seed: seed,
                    property: NestedListsChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .reverse:
                let (output, report, original, wall) = exhaust(
                    ReverseChallenge.gen,
                    seed: seed,
                    property: ReverseChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)
            case .anagrams, .usernamePassword, .duplicatedText, .distinctSum, .leapDay, .branchSwitching, .haystack, .zalgoHaystack:
                break
            case .depthTwoProductSequenceBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthTwoProductSequence,
                    seed: seed,
                    property: NestedBindsChallenge.propertyTwo
                )
                guard let (a, b, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .depthThreeProductSequenceBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthThreeProductSequence,
                    seed: seed,
                    property: NestedBindsChallenge.propertyThree
                )
                guard let (a, b, c, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(c), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .depthFourProductSequenceBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthFourProductSequence,
                    seed: seed,
                    property: NestedBindsChallenge.propertyFour
                )
                guard let (a, b, c, d, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(c), \(d), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .depthFiveProductSequenceBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthFiveProductSequence,
                    seed: seed,
                    property: NestedBindsChallenge.propertyFive
                )
                guard let (a, b, c, d, e, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(c), \(d), \(e), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .depthSixProductSequenceBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthSixProductSequence,
                    seed: seed,
                    property: NestedBindsChallenge.propertySix
                )
                guard let (a, b, c, d, e, f, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(c), \(d), \(e), \(f), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .depthTwoProductBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthTwoProduct,
                    seed: seed,
                    property: NestedBindsChallenge.propertyTwoProduct
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed, original: original, wallMilliseconds: wall)
            case .depthThreeProductBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthThreeProduct,
                    seed: seed,
                    property: NestedBindsChallenge.propertyThreeProduct
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed, original: original, wallMilliseconds: wall)
            case .depthFourProductBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthFourProduct,
                    seed: seed,
                    property: NestedBindsChallenge.propertyFourProduct
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed, original: original, wallMilliseconds: wall)
            case .depthFiveProductBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthFiveProduct,
                    seed: seed,
                    property: NestedBindsChallenge.propertyFiveProduct
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed, original: original, wallMilliseconds: wall)
            case .depthSixProductBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthSixProduct,
                    seed: seed,
                    property: NestedBindsChallenge.propertySixProduct
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed, original: original, wallMilliseconds: wall)
            case .modularMapping:
                let (output, report, original, wall) = exhaust(
                    ModularMappingChallenge.gen,
                    seed: seed,
                    property: ModularMappingChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)
            case .weightedLinearPreservation:
                let (output, report, original, wall) = exhaust(
                    WeightedLinearPreservationChallenge.gen,
                    seed: seed,
                    property: WeightedLinearPreservationChallenge.property
                )
                stats.append(report: report, counterExample: String(describing: output ?? (-1, -1, -1)), seed: seed, original: original, wallMilliseconds: wall)

            case .invoiceDiscount:
                let (output, report, original, wall) = exhaust(
                    InvoiceDiscountChallenge.gen,
                    seed: seed,
                    property: InvoiceDiscountChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)

            case .invoiceDiscountDerived:
                let (output, report, original, wall) = exhaustSkipping(
                    InvoiceDiscountChallenge.derivedGen,
                    seed: seed,
                    property: InvoiceDiscountChallenge.derivedProperty
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)
            case .depthFourSumBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthFourSum,
                    seed: seed,
                    property: NestedBindsChallenge.propertyFour
                )
                guard let (a, b, c, d, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(c), \(d), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .floatCancellation:
                let (output, report, original, wall) = exhaust(
                    FloatCancellationChallenge.gen,
                    seed: seed,
                    property: FloatCancellationChallenge.property
                )
                stats.append(report: report, counterExample: output.map { "(\($0.0), \($0.1))" }, seed: seed, original: original, wallMilliseconds: wall)
            case .chunkedDecoder:
                let (output, report, original, wall) = exhaust(
                    ChunkedDecoderChallenge.gen,
                    seed: seed,
                    property: ChunkedDecoderChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)
            case .snapshotStore:
                // Matches Hypothesis's default stateful_step_count, so both libraries generate histories of up to 50 commands
                let (output, report, _, wall) = await execute(SnapshotStoreChallenge.Spec.self, commandLimit: 50, seed: seed)
                stats.append(
                    report: report,
                    counterExample: output.map { SnapshotStoreChallenge.render($0.commands) },
                    seed: seed,
                    original: output.map { SnapshotStoreChallenge.render($0.originalCommands ?? $0.commands) },
                    wallMilliseconds: wall
                )
            case .hashCollisionTen:
                let (output, report, original, wall) = exhaust(
                    HashCollisionChallenge.gen(modulus: 10),
                    seed: seed,
                    property: HashCollisionChallenge.property(modulus: 10)
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed, original: original, wallMilliseconds: wall)
            case .hashCollisionHundred:
                let (output, report, original, wall) = exhaust(
                    HashCollisionChallenge.gen(modulus: 100),
                    seed: seed,
                    property: HashCollisionChallenge.property(modulus: 100)
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed, original: original, wallMilliseconds: wall)
            case .hashCollisionThousand:
                let (output, report, original, wall) = exhaust(
                    HashCollisionChallenge.gen(modulus: 1000),
                    seed: seed,
                    property: HashCollisionChallenge.property(modulus: 1000)
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed, original: original, wallMilliseconds: wall)
            // Matches Hypothesis's default stateful_step_count, as for Snapshot Store
            case .hashCollisionStateMachineTen:
                let (output, report, _, wall) = await execute(HashCollisionChallenge.SpecTen.self, commandLimit: 50, seed: seed)
                stats.append(report: report, counterExample: output.map { HashCollisionChallenge.render($0.commands) }, seed: seed, original: output.map { HashCollisionChallenge.render($0.originalCommands ?? $0.commands) }, wallMilliseconds: wall)
            case .hashCollisionStateMachineHundred:
                let (output, report, _, wall) = await execute(HashCollisionChallenge.SpecHundred.self, commandLimit: 50, seed: seed)
                stats.append(report: report, counterExample: output.map { HashCollisionChallenge.render($0.commands) }, seed: seed, original: output.map { HashCollisionChallenge.render($0.originalCommands ?? $0.commands) }, wallMilliseconds: wall)
            case .hashCollisionStateMachineThousand:
                let (output, report, _, wall) = await execute(HashCollisionChallenge.SpecThousand.self, commandLimit: 50, seed: seed)
                stats.append(report: report, counterExample: output.map { HashCollisionChallenge.render($0.commands) }, seed: seed, original: output.map { HashCollisionChallenge.render($0.originalCommands ?? $0.commands) }, wallMilliseconds: wall)
            }
        }
        return stats
    }

    static func exhaust<Output>(
        _ gen: ReflectiveGenerator<Output>,
        seed: UInt64,
        property: @Sendable (Output) -> Bool
    ) -> (Output?, ExhaustReport, String?, Double) {
        var report: ExhaustReport!
        nonisolated(unsafe) var original: String?
        let start = DispatchTime.now().uptimeNanoseconds

        let output = #exhaust(
            gen,
            .budget(.custom(screening: 0, sampling: 25_000)),
            .suppress(.all),
            .replay(.numeric(seed)),
            .onReport { report = $0 },
            property: { value in
                let result = property(value)
                if result == false, original == nil {
                    original = String(describing: value)
                }
                return result
            }
        )
        let wallMilliseconds = Double(DispatchTime.now().uptimeNanoseconds - start) / 1_000_000.0
        return (output, report, original, wallMilliseconds)
    }
    
    // Same as `exhaust`, for properties that discard invalid inputs by throwing `PropertySkip`
    static func exhaustSkipping<Output>(
        _ gen: ReflectiveGenerator<Output>,
        seed: UInt64,
        property: @Sendable (Output) throws -> Bool
    ) -> (Output?, ExhaustReport, String?, Double) {
        var report: ExhaustReport!
        nonisolated(unsafe) var original: String?
        let start = DispatchTime.now().uptimeNanoseconds

        let output = #exhaust(
            gen,
            .budget(.custom(screening: 0, sampling: 25_000)),
            .suppress(.all),
            .replay(.numeric(seed)),
            .onReport { report = $0 },
            property: { value in
                let result = try property(value)
                if result == false, original == nil {
                    original = String(describing: value)
                }
                return result
            }
        )
        let wallMilliseconds = Double(DispatchTime.now().uptimeNanoseconds - start) / 1_000_000.0
        return (output, report, original, wallMilliseconds)
    }
    
    // Same as `exhaust`, for state machine specs run sequentially
    static func execute<Spec: StateMachineSpec>(
        _ spec: Spec.Type,
        commandLimit: Int,
        seed: UInt64
    ) async -> (StateMachineResult<Spec>?, ExhaustReport?, String?, Double) {
        nonisolated(unsafe) var report: ExhaustReport?
        let start = DispatchTime.now().uptimeNanoseconds

        let result = await #execute(
            Spec.self,
            mode: .sequential,
            .commandLimit(commandLimit),
            .budget(.custom(screening: 0, sampling: 25_000)),
            .suppress(.all),
            .replay(.numeric(seed)),
            .onReport { report = $0 }
        )
        let wallMilliseconds = Double(DispatchTime.now().uptimeNanoseconds - start) / 1_000_000.0
        return (result, report, nil, wallMilliseconds)
    }

    static func exhaustReflecting<Output>(
        _ gen: ReflectiveGenerator<Output>,
        reflecting output: Output,
        seed: UInt64,
        property: @Sendable (Output) -> Bool
    ) -> (Output?, ExhaustReport, String?, Double) {
        var report: ExhaustReport!
        nonisolated(unsafe) var original: String?
        let start = DispatchTime.now().uptimeNanoseconds

        let output = #exhaust(
            gen,
            reflecting: output,
            .budget(.custom(screening: 0, sampling: 25_000)),
            .suppress(.all),
            .onReport { report = $0 },
            property: { value in
                let result = property(value)
                if result == false, original == nil {
                    original = String(describing: value)
                }
                return result
            }
        )
        let wallMilliseconds = Double(DispatchTime.now().uptimeNanoseconds - start) / 1_000_000.0
        return (output, report, original, wallMilliseconds)
    }
}
