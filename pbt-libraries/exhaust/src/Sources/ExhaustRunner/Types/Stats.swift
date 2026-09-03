//
//  Stats.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust
import Foundation

final class Stats {
    let challenge: Challenge
    let iterations: UInt64
    var counterExamples = [String: Accumulator]()
    var reports = [ExhaustReport]()
    var wallTimes = [Double]()
    var entries = [Entry]()
    var missed = UInt64(0)
    
    init(challenge: Challenge, iterations: UInt64) {
        self.challenge = challenge
        self.iterations = iterations
    }
    
    func append(report: ExhaustReport!, counterExample: String?, seed: UInt64, original: String?, wallMilliseconds: Double) {
        guard let report, let counterExample else {
            missed += 1
            return
        }
        if let original {
            entries.append(
                Entry(
                    seed: seed,
                    evaluations: report.reductionInvocations,
                    original: original,
                    shrunk: counterExample
                )
            )
        }
        reports.append(report)
        wallTimes.append(wallMilliseconds)
        let example = counterExamples[counterExample] ?? .init()
        example.count += 1
        example.seeds.append(seed)
        counterExamples[counterExample] = example
    }
    
    func printSummary() {
        guard reports.isEmpty == false else {
            return 
        }
        var evaluations = [Double]()
        var reductionTimes = [Double]()
        var generationTimes = [Double]()
        var totalTimes = [Double]()
        var screeningTimes = [Double]()
        var cycles = [Double]()
        var itersToFailure = [Double]()
        
        for report in reports {
            evaluations.append(Double(report.reductionInvocations))
            reductionTimes.append(report.reductionMilliseconds)
            generationTimes.append(report.generationMilliseconds)
            screeningTimes.append(report.screeningMilliseconds)
            totalTimes.append(report.totalMilliseconds)
            cycles.append(Double(report.cycles))
            itersToFailure.append(Double(report.screeningInvocations + report.randomSamplingInvocations))
        }
        let evals = Statistics(evaluations)
        let reductions = Statistics(reductionTimes)
        let generations = Statistics(generationTimes)
        let screening = Statistics(screeningTimes)
        let totals = Statistics(totalTimes)
        let iters = Statistics(itersToFailure)
        let walls = Statistics(wallTimes)
        
        print("\(challenge.description), \(iterations) runs, \(iterations - missed) failures:")

        for (title, stats, decs) in [("evaluations", evals, UInt(1)), ("reductions (ms)", reductions, 2), ("generation (ms)", generations, 3), ("screening (ms)", screening, 3), ("total (ms)", totals, 3), ("wall (ms)", walls, 3), ("iterations to failure", iters, 1)] {
            print("  \(title): min=\(stats.min.rounded(decimals: decs)) max=\(stats.max.rounded(decimals: decs)) median=\(stats.median.rounded(decimals: decs)) mean=\(stats.mean.rounded(decimals: decs)) (\(stats.ciLow.rounded(decimals: decs))—\(stats.ciHigh.rounded(decimals: decs)))")
        }
        
        let examples = counterExamples.map { ($0.key, $0.value) }
            .sorted(by: { $0.1.count > $1.1.count })

        for example in examples {
            let percentage = ((Double(example.1.count) / Double(iterations - missed)) * 100).rounded(decimals: 2)
            print("    \(percentage)% \(example.0) (\(example.1.count)) \(example.1.seeds.prefix(1))")
        }
    }
    
    /// Writes the lowest `limit` seeds to `<directory>/<challenge>.json` in the shape the other libraries in this repository publish.
    ///
    /// Each entry pairs the input as generated with the input after reduction, keyed `p` for the single property parameter. Seeds whose run never failed are absent.
    func writeReport(toDirectory directory: String, limit: Int = 100) throws {
        let selected = entries.sorted(by: { $0.seed < $1.seed }).prefix(limit)
        guard selected.isEmpty == false else {
            return
        }
        let payload = selected.map {
            ReportEntry(
                evaluations: $0.evaluations,
                original: ["p": $0.original],
                seed: $0.seed,
                shrunk: ["p": $0.shrunk]
            )
        }
        let encoder = JSONEncoder()
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys, .withoutEscapingSlashes]
        let url = URL(fileURLWithPath: directory).appendingPathComponent("\(challenge.rawValue).json")
        try encoder.encode(payload).write(to: url, options: .atomic)
        print("  wrote \(selected.count) entries to \(url.path)")
    }

    struct Entry {
        let seed: UInt64
        let evaluations: Int
        let original: String
        let shrunk: String
    }

    final class Accumulator {
        var count = 0
        var seeds = [UInt64]()
        
        init() { }
        
        func append(seed: UInt64) {
            count += 1
            seeds.append(seed)
        }
    }
    
    private struct ReportEntry: Encodable {
        let evaluations: Int
        let original: [String: String]
        let seed: UInt64
        let shrunk: [String: String]
    }

    struct Statistics {
        let source: [Double]
        let min: Double
        let max: Double
        let mean: Double
        let median: Double
        let ciHigh: Double
        let ciLow: Double
        
        init(_ source: [Double]) {
            let sorted = source.sorted()
            let count = Double(sorted.count)
            let mean = sorted.reduce(0, +) / count
            let median = sorted.count % 2 == 0
                ? (sorted[sorted.count / 2 - 1] + sorted[sorted.count / 2]) / 2
                : sorted[sorted.count / 2]
            let variance = sorted.map { pow($0 - mean, 2) }.reduce(0, +) / (count - 1)
            let stdError = sqrt(variance / count)
            
            self.source = sorted
            self.min = sorted.min()!
            self.max = sorted.max()!
            self.ciLow = mean - 1.96 * stdError
            self.ciHigh = mean + 1.96 * stdError
            self.mean = mean
            self.median = median
        }
    }
}

private extension Double {
    func rounded(decimals: UInt) -> Double {
        let factor = Double(pow(10.0, Double(decimals)))
        return (self * factor).rounded(.toNearestOrEven) / factor
    }
}
