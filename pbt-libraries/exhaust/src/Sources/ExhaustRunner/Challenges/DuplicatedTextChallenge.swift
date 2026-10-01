//
//  DuplicatedTextChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust
import Foundation

enum DuplicatedTextChallenge {
    // Fixed-length strings, so equal values can only shrink by rewriting characters in both
    static let stringGen = #gen(.string(from: CharacterSet(charactersIn: "abcdefghijklmnopqrstuvwxyz0123456789"), length: 8...8))
    static let gen = #gen(stringGen, stringGen)
    static let input = ("q7zq7zq7", "q7zq7zq7")

    static let property: @Sendable (String, String) -> Bool = { a, b in
        a != b || Set(a).count < 3
    }
}
