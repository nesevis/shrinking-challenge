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
    var missed = UInt64(0)
    
    init(challenge: Challenge, iterations: UInt64) {
        self.challenge = challenge
        self.iterations = iterations
    }
    
    func append(report: ExhaustReport!, counterExample: String?, seed: UInt64) {
        guard let report, let counterExample else {
            missed += 1
            return
        }
        reports.append(report)
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
        var cycles = [Double]()
        var itersToFailure = [Double]()
        
        for report in reports {
            evaluations.append(Double(report.propertyInvocations - report.randomSamplingInvocations))
            reductionTimes.append(report.reductionMilliseconds)
            cycles.append(Double(report.cycles))
            itersToFailure.append(Double(report.randomSamplingInvocations))
        }
        let evals = Statistics(evaluations)
        let reductions = Statistics(reductionTimes)
        let iters = Statistics(itersToFailure)
        
        print("\(challenge.description), \(iterations) runs, \(iterations - missed) failures:")

        for (title, stats, decs) in [("evaluations", evals, UInt(1)), ("reductions (ms)", reductions, 2), ("iterations to failure", iters, 1)] {
            print("  \(title): min=\(stats.min.rounded(decimals: decs)) max=\(stats.max.rounded(decimals: decs)) median=\(stats.median.rounded(decimals: decs)) mean=\(stats.mean.rounded(decimals: decs)) (\(stats.ciLow.rounded(decimals: decs))—\(stats.ciHigh.rounded(decimals: decs)))")
        }
        
        let examples = counterExamples.map { ($0.key, $0.value) }
            .sorted(by: { $0.1.count > $1.1.count })
        
        for example in examples {
            let percentage = ((Double(example.1.count) / Double(iterations - missed)) * 100).rounded(decimals: 2)
            print("    \(percentage)% \(example.0) (\(example.1.count))")
        }
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
