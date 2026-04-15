//
//  Distinct.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust

enum DistinctChallenge {
    static let gen = #gen(.int().array(length: 3 ... 30))

    static let property: @Sendable ([Int]) -> Bool = { arr in
        Set(arr).count < 3
    }
}
