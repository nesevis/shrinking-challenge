//
//  ReverseChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust

enum ReverseChallenge {
    static let gen = #gen(.uint()).array(length: 1 ... 1000)

    static let property: @Sendable ([UInt]) -> Bool = { arr in
        arr.elementsEqual(arr.reversed())
    }
}
