//
//  Deletion.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust

enum DeletionChallenge {
    static let gen = {
        let numberGen = #gen(.int(in: 0 ... 20))
        return #gen(numberGen.array(length: 2 ... 20), numberGen)
            .filter(.rejectionSampling) { $0.contains($1) }
    }()

    static let property: @Sendable (([Int], Int)) -> Bool = { pair in
        var array = pair.0
        let element = pair.1
        guard let index = array.firstIndex(of: element) else { return true }
        array.remove(at: index)
        return array.contains(element) == false
    }
}
