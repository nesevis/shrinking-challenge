//
//  Coupling.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 14/4/2026.
//

import Exhaust

enum CouplingChallenge {
    static let gen = #gen(.int(in: 0 ... 10, scaling: .constant))
        .bind { n in
            #gen(.int(in: 0 ... n)).array(length: 2 ... max(2, n + 1), scaling: .constant)
        }
        .filter(.rejectionSampling) { arr in arr.allSatisfy { arr.indices.contains($0) } }

    static let property: @Sendable ([Int]) -> Bool = { arr in
        arr.indices.allSatisfy { i in
            let j = arr[i]
            if j != i, arr[j] == i {
                return false
            }
            return true
        }
    }
}
