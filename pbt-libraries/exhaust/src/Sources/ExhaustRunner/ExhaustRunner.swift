//
//  ExhaustRunner.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import ArgumentParser

@main
struct ExhaustRunner: ParsableCommand {
    @Option(name: .shortAndLong, help: "Which challenge to run. All of them if unspecified")
    var challenge: Challenge?
    
    @Option(name: .shortAndLong, help: "How many iterations")
    var iterations: UInt64 = 100
    
    @Option(name: .shortAndLong, help: "What seed to start with")
    var seed: UInt64 = 1337

    mutating func run() throws {
        let challenges = challenge.map { [$0] } ?? Challenge.allCases
        
        print("Starting run of \(challenges.count) challenge(s) with \(iterations) iteration(s)…")

        for challenge in challenges {
            let stats = ChallengeRunner.run(challenge, seed: seed, iterations: iterations)
            stats.printSummary()
            print()
        }
    }
}
