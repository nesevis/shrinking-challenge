//
//  Challenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 14/4/2026.
//

import ArgumentParser

enum Challenge: String, CaseIterable, CustomStringConvertible, Decodable, ExpressibleByArgument {
    case binaryHeap
    case bound5
    case calculator
    case coupling
    case deletion
    case differenceNotZero
    case differenceNotSmall
    case differenceNotOne
    case distinct
    case largeUnionList
    case lengthList
    case nestedLists
    case reverse

    var description: String {
        switch self {
        case .binaryHeap: "Binary Heap"
        case .bound5: "Bound5"
        case .calculator: "Calculator"
        case .coupling: "Coupling"
        case .deletion: "Deletion"
        case .differenceNotZero: "Difference: Not Zero"
        case .differenceNotSmall: "Difference: Not Small"
        case .differenceNotOne: "Difference: Not One"
        case .distinct: "Distinct"
        case .largeUnionList: "Large Union List"
        case .lengthList: "Length List"
        case .nestedLists: "Nested Lists"
        case .reverse: "Reverse"
        }
    }
}
