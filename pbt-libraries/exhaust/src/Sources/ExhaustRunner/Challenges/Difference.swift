//
//  Difference.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust

enum DifferenceChallenge {
    static let gen = #gen(.int()).array(length: 2)

    static let notZero: @Sendable ([Int]) -> Bool = { arr in
        arr[0] < 10 || arr[0] != arr[1]
    }

    static let notSmall: @Sendable ([Int]) -> Bool = { arr in
        if arr[0] < 10 { return true }
        let (result, overflow) = arr[0].subtractingReportingOverflow(arr[1])
        if overflow || result == .min { return true }
        let diff = abs(result)
        return diff < 1 || diff > 4
    }
    
    static let notOne: @Sendable ([Int]) -> Bool = { arr in
        if arr[0] < 10 { return true }
        let (result, overflow) = arr[0].subtractingReportingOverflow(arr[1])
        if overflow || result == .min { return true }
        let diff = abs(result)
        return diff != 1
    }
}
