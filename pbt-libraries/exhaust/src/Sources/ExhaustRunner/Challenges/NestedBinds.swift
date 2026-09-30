//
//  NestedBinds.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust

enum NestedBindsChallenge {
    static let depthTwo = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 0...1).array(length: a * b)
                .map { (a, b, $0) }
        }
    }
    
    static let depthThree = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 0...1).array(length: a * b * c)
                    .map { (a, b, c, $0) }
            }
        }
    }
    
    static let depthFour = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 1...c).bind { d in
                    .int(in: 0...1).array(length: a * b * c * d)
                        .map { (a, b, c, d, $0) }
                }
            }
        }
    }
    
    static let depthFive = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 1...c).bind { d in
                    .int(in: 1...d).bind { e in
                        .int(in: 0...1).array(length: a * b * c * d * e)
                            .map { (a, b, c, d, e, $0) }
                    }
                }
            }
        }
    }
    
    static let depthSix = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 1...c).bind { d in
                    .int(in: 1...d).bind { e in
                        .int(in: 1...e).bind { f in
                            .int(in: 0...1).array(length: a * b * c * d * e * f)
                                .map { (a, b, c, d, e, f, $0) }
                        }
                    }
                }
            }
        }
    }
    
    // MARK: - Properties
    
    static let propertyTwo: @Sendable (Int, Int, [Int]) -> Bool = { _, _, ints in
        ints.count < 24 || ints.contains(1) == false
    }
    
    static let propertyThree: @Sendable (Int, Int, Int, [Int]) -> Bool = { _, _, _, ints in
        ints.count < 24 || ints.contains(1) == false
    }
    
    static let propertyFour: @Sendable (Int, Int, Int, Int, [Int]) -> Bool = { _, _, _, _, ints in
        ints.count < 24 || ints.contains(1) == false
    }
    
    static let propertyFive: @Sendable (Int, Int, Int, Int, Int, [Int]) -> Bool = { _, _, _, _, _, ints in
        ints.count < 24 || ints.contains(1) == false
    }
    
    static let propertySix: @Sendable (Int, Int, Int, Int, Int, Int, [Int]) -> Bool = { _, _, _, _, _, _, ints in
        ints.count < 24 || ints.contains(1) == false
    }
}
