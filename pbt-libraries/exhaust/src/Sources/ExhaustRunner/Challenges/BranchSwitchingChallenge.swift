//
//  BranchSwitchingChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust

enum BranchSwitchingChallenge {
    // The simpler counterexample lives in the first case, while the start is in the second
    @Exhaustable
    enum Value: CustomStringConvertible {
        case int(Int)
        case text(String)

        var description: String {
            switch self {
            case let .int(value): "\(value)"
            case let .text(value): "\"\(value)\""
            }
        }
    }

    static let gen = Value.gen()
    static let input = Value.text("a branch switch")

    static let property: @Sendable (Value) -> Bool = { value in
        switch value {
        case let .int(number): number <= 1_000
        case let .text(text): text.count < 4
        }
    }
}
