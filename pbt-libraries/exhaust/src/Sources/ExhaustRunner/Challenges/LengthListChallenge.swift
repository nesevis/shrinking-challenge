//
//  LengthListChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust

enum LengthListChallenge {
    static let gen = #gen(.uint(in: 0 ... 1000)).array(length: 1 ... 100)

    static let property: @Sendable ([UInt]) -> Bool = { arr in
        arr.max() ?? 0 < 900
    }
}
