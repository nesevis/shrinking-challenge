//
//  NestedListsChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust

enum NestedListsChallenge {
    static let gen = #gen(.uint().array().array())

    static let property: @Sendable ([[UInt]]) -> Bool = { arrs in
        var count = 0
        for arr in arrs {
            count += arr.count
            if count > 10 {
                return false
            }
        }
        return count <= 10
    }
}
