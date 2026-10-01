//
//  DistinctSumChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust

enum DistinctSumChallenge {
    static let gen = #gen(.int().unique().array())
    static let input = [9973, 4421, 8810, 1203, 7777, 5050]

    static let property: @Sendable ([Int]) -> Bool = { xs in
        Set(xs).count < 5 || xs.reduce(0, +) <= 50
    }
}
