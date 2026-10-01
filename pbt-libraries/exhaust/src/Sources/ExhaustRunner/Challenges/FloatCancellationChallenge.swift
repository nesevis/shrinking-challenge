//
//  FloatCancellationChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust

enum FloatCancellationChallenge {
    static let doubleGen = #gen(.double(in: -1e6 ... 1e6))
    static let gen = #gen(doubleGen, doubleGen)

    static let property: @Sendable (Double, Double) -> Bool = { a, b in
        (a + b) - b == a
    }
}
