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
    static func run(_ challenge: Challenge, seed: UInt64, iterations: UInt64) -> Stats {
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
            case .anagrams, .usernamePassword:
                break
            case .depthTwoBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthTwo,
                    seed: seed,
                    property: NestedBindsChallenge.propertyTwo
                )
                guard let (a, b, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .depthThreeBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthThree,
                    seed: seed,
                    property: NestedBindsChallenge.propertyThree
                )
                guard let (a, b, c, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(c), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .depthFourBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthFour,
                    seed: seed,
                    property: NestedBindsChallenge.propertyFour
                )
                guard let (a, b, c, d, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(c), \(d), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .depthFiveBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthFive,
                    seed: seed,
                    property: NestedBindsChallenge.propertyFive
                )
                guard let (a, b, c, d, e, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(c), \(d), \(e), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
            case .depthSixBind:
                let (output, report, original, wall) = exhaust(
                    NestedBindsChallenge.depthSix,
                    seed: seed,
                    property: NestedBindsChallenge.propertySix
                )
                guard let (a, b, c, d, e, f, ints) = output else {
                    fatalError("Did not find error")
                }
                let oneCount = ints.count(where: { $0 == 1 })
                let singleOneAtEnd = oneCount == 1 && ints.last == 1
                stats.append(report: report, counterExample: "\(a), \(b), \(c), \(d), \(e), \(f), \(ints.count) length, \(singleOneAtEnd ? "[0,…,1]" : "[0,…,1x\(oneCount)]")", seed: seed, original: original, wallMilliseconds: wall)
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
                let (output, report, original, wall) = exhaust(
                    InvoiceDiscountChallenge.derivedGen,
                    seed: seed,
                    property: InvoiceDiscountChallenge.derivedProperty
                )
                stats.append(report: report, counterExample: output?.description, seed: seed, original: original, wallMilliseconds: wall)
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
