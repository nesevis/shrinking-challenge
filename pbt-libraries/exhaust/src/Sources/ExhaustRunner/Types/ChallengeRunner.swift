//
//  ChallengeRunner.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 14/4/2026.
//

import Exhaust
import Foundation

enum ChallengeRunner {
    static func run(_ challenge: Challenge, seed: UInt64, iterations: UInt64) -> Stats {
        let stats = Stats(challenge: challenge, iterations: iterations)

        for iteration in 0 ..< iterations {
            let seed = seed + iteration
            switch challenge {
            case .binaryHeap:
                let (output, report) = exhaust(
                    BinaryHeapChallenge.gen,
                    seed: seed,
                    property: BinaryHeapChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .bound5:
                let (output, report) = exhaust(
                    Bound5Challenge.gen,
                    seed: seed,
                    property: Bound5Challenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .calculator:
                let (output, report) = exhaust(
                    CalculatorChallenge.gen(depth: 5),
                    seed: seed,
                    property: CalculatorChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .coupling:
                let (output, report) = exhaust(
                    CouplingChallenge.gen,
                    seed: seed,
                    property: CouplingChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .deletion:
                let (output, report) = exhaust(
                    DeletionChallenge.gen,
                    seed: seed,
                    property: DeletionChallenge.property
                )
                stats.append(report: report, counterExample: output.map { "\($0)" }, seed: seed)

            case .differenceNotZero:
                let (output, report) = exhaust(
                    DifferenceChallenge.gen,
                    seed: seed,
                    property: DifferenceChallenge.notZero
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .differenceNotSmall:
                let (output, report) = exhaust(
                    DifferenceChallenge.gen,
                    seed: seed,
                    property: DifferenceChallenge.notSmall
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .differenceNotOne:
                let (output, report) = exhaust(
                    DifferenceChallenge.gen,
                    seed: seed,
                    property: DifferenceChallenge.notOne
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .distinct:
                let (output, report) = exhaust(
                    DistinctChallenge.gen,
                    seed: seed,
                    property: DistinctChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)
                
            case .largeUnionList:
                let (output, report) = exhaust(
                    LargeUnionListChallenge.gen,
                    seed: seed,
                    property: LargeUnionListChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .lengthList:
                let (output, report) = exhaust(
                    LengthListChallenge.gen,
                    seed: seed,
                    property: LengthListChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .nestedLists:
                let (output, report) = exhaust(
                    NestedListsChallenge.gen,
                    seed: seed,
                    property: NestedListsChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)

            case .reverse:
                let (output, report) = exhaust(
                    ReverseChallenge.gen,
                    seed: seed,
                    property: ReverseChallenge.property
                )
                stats.append(report: report, counterExample: output?.description, seed: seed)
            }
        }
        return stats
    }
    
    static func exhaust<Output>(
        _ gen: ReflectiveGenerator<Output>,
        seed: UInt64,
        property: @Sendable (Output) -> Bool
    ) -> (Output?, ExhaustReport) {
        var report: ExhaustReport!
        let output = #exhaust(
            gen,
            .budget(.custom(coverage: 0, sampling: 25_000)),
            .suppress(.all),
            .replay(.numeric(seed)),
            .onReport { report = $0 },
            property: property
        )
        return (output, report)
    }
}
