//
//  LargeUnionList.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust

enum LargeUnionListChallenge {
    static let gen = #gen(.int().array().array())

    static let property: @Sendable ([[Int]]) -> Bool = { arr in
        Set(arr.flatMap(\.self)).count <= 4
    }
}
