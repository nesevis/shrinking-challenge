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
}
