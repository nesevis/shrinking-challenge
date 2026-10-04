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
    case duplicatedText
    case haystack
    case zalgoHaystack

    case distinctSum
    case leapDay
    case branchSwitching

    case modularMapping
    case weightedLinearPreservation
    case invoiceDiscount
    case invoiceDiscountDerived
    case refundAllocation
    case refundAllocationDerived
    case depthFourSumBind
    case floatCancellation
    case chunkedDecoder
    case snapshotStore
    case hashCollisionTen
    case hashCollisionHundred
    case hashCollisionThousand
    case hashCollisionStateMachineTen
    case hashCollisionStateMachineHundred
    case hashCollisionStateMachineThousand
    case depthTwoProductSequenceBind
    case depthThreeProductSequenceBind
    case depthFourProductSequenceBind
    case depthFiveProductSequenceBind
    case depthSixProductSequenceBind
    case depthTwoProductBind
    case depthThreeProductBind
    case depthFourProductBind
    case depthFiveProductBind
    case depthSixProductBind

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
        case .duplicatedText: "Duplicated Text"
        case .distinctSum: "Distinct Sum"
        case .leapDay: "Leap Day"
        case .branchSwitching: "Branch Switching"
        case .haystack: "Haystack"
        case .zalgoHaystack: "Zalgo Haystack"
        case .depthTwoProductSequenceBind: "Depth 2 Bind (product sequence)"
        case .depthThreeProductSequenceBind: "Depth 3 Bind (product sequence)"
        case .depthFourProductSequenceBind: "Depth 4 Bind (product sequence)"
        case .depthFiveProductSequenceBind: "Depth 5 Bind (product sequence)"
        case .depthSixProductSequenceBind: "Depth 6 Bind (product sequence)"
        case .depthTwoProductBind: "Depth 2 Bind (product)"
        case .depthThreeProductBind: "Depth 3 Bind (product)"
        case .depthFourProductBind: "Depth 4 Bind (product)"
        case .depthFiveProductBind: "Depth 5 Bind (product)"
        case .depthSixProductBind: "Depth 6 Bind (product)"
        case .modularMapping: "Modular Mapping"
        case .weightedLinearPreservation: "Weighted Linear Preservation"
        case .invoiceDiscount: "Invoice Discount"
        case .invoiceDiscountDerived: "Invoice Discount (derived)"
        case .refundAllocation: "Refund Allocation"
        case .refundAllocationDerived: "Refund Allocation (derived)"
        case .depthFourSumBind: "Depth 4 Bind (sum)"
        case .floatCancellation: "Float Cancellation"
        case .chunkedDecoder: "Chunked Decoder"
        case .snapshotStore: "Snapshot Store"
        case .hashCollisionTen: "Hash Collision (M = 10)"
        case .hashCollisionHundred: "Hash Collision (M = 100)"
        case .hashCollisionThousand: "Hash Collision (M = 1000)"
        case .hashCollisionStateMachineTen: "Hash Collision, state machine (M = 10)"
        case .hashCollisionStateMachineHundred: "Hash Collision, state machine (M = 100)"
        case .hashCollisionStateMachineThousand: "Hash Collision, state machine (M = 1000)"
        }
    }
    
    var reflectsInput: Bool {
        switch self {
        case .anagrams, .usernamePassword, .duplicatedText, .distinctSum, .leapDay, .branchSwitching, .haystack, .zalgoHaystack: true
        default: false
        }
    }
    
    var isCustom: Bool {
        switch self {
        case .bound5, .coupling, .deletion, .differenceNotOne, .differenceNotSmall, .differenceNotZero, .distinct, .largeUnionList, .lengthList, .nestedLists, .reverse:
            false
        default:
            true
        }
    }
}
