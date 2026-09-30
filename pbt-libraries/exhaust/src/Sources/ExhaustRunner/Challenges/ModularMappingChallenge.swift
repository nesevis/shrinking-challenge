//
//  ModularMappingChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust

enum ModularMappingChallenge {
    static let gen = #gen(.int(in: 0...1000))
        .map { ($0 * 37) % 1001 }
    
    static let property: @Sendable (Int) -> Bool = { $0 < 900 }
}
