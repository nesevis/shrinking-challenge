//
//  WeightedLinearPreservationChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust

enum WeightedLinearPreservationChallenge {
    static let intGen = #gen(.int(in: 0...20))
    static let gen = #gen(intGen, intGen, intGen)
    
    static let property: @Sendable (Int, Int, Int) -> Bool = {
        $0 * 2 + $1 + $2 != 20
    }
}
