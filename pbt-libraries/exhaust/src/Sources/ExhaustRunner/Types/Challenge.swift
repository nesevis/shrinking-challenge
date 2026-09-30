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
    
    // The challenges below are not part of the official shrinking challenge
    
    case anagrams
    case usernamePassword

    case depthTwoBind
    case depthThreeBind
    case depthFourBind
    case depthFiveBind
    case depthSixBind
    case modularMapping
    case weightedLinearPreservation
    case invoiceDiscount
    case invoiceDiscountDerived

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
        case .anagrams: "Anagrams"
        case .usernamePassword: "Username and Password"
        case .depthTwoBind: "Depth 2 Bind"
        case .depthThreeBind: "Depth 3 Bind"
        case .depthFourBind: "Depth 4 Bind"
        case .depthFiveBind: "Depth 5 Bind"
        case .depthSixBind: "Depth 6 Bind"
        case .modularMapping: "Modular Mapping"
        case .weightedLinearPreservation: "Weighted Linear Preservation"
        case .invoiceDiscount: "Invoice Discount"
        case .invoiceDiscountDerived: "Invoice Discount (derived)"
        }
    }
    
    var reflectsInput: Bool {
        switch self {
        case .anagrams, .usernamePassword: true
        default: false
        }
    }
}
