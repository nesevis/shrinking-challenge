//
//  Anagrams.swift
//  src
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust

enum AnagramsChallenge {
    static let stringGen = #gen(.string())
    static let gen = #gen(stringGen, stringGen)
    static let input = ("a gentle man and astronomer", "elegant man and moon starer")

    static let property: @Sendable (String, String) -> Bool = { lhs, rhs in
        lhs == rhs || lhs.sorted() != rhs.sorted()
    }
}
