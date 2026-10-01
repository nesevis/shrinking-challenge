//
//  NestedBinds.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust

enum NestedBindsChallenge {
    static let depthTwoProductSequence = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 0...1).array(length: a * b)
                .map { (a, b, $0) }
        }
    }
    
    static let depthThreeProductSequence = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 0...1).array(length: a * b * c)
                    .map { (a, b, c, $0) }
            }
        }
    }
    
    static let depthFourProductSequence = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 1...c).bind { d in
                    .int(in: 0...1).array(length: a * b * c * d)
                        .map { (a, b, c, d, $0) }
                }
            }
        }
    }
    
    static let depthFiveProductSequence = #gen(.int(in: 1...10)).bind { a in
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
    
    static let depthSixProductSequence = #gen(.int(in: 1...10)).bind { a in
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
    
    // Product variants drop the payload, so the factors' product is the only thing the property sees
    static let depthTwoProduct = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a)
            .map { b in (a, b) }
    }
    
    static let depthThreeProduct = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b)
                .map { c in (a, b, c) }
        }
    }
    
    static let depthFourProduct = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 1...c)
                    .map { d in (a, b, c, d) }
            }
        }
    }
    
    static let depthFiveProduct = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 1...c).bind { d in
                    .int(in: 1...d)
                        .map { e in (a, b, c, d, e) }
                }
            }
        }
    }
    
    static let depthSixProduct = #gen(.int(in: 1...10)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 1...c).bind { d in
                    .int(in: 1...d).bind { e in
                        .int(in: 1...e)
                            .map { f in (a, b, c, d, e, f) }
                    }
                }
            }
        }
    }
    
    // Payload length is the sum of the factors, so the factor domain can grow without the payload outgrowing Hypothesis's test-case size limit
    static let depthFourSum = #gen(.int(in: 1...100)).bind { a in
        .int(in: 1...a).bind { b in
            .int(in: 1...b).bind { c in
                .int(in: 1...c).bind { d in
                    .int(in: 0...1).array(length: a + b + c + d)
                        .map { (a, b, c, d, $0) }
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
    
    static let propertyTwoProduct: @Sendable (Int, Int) -> Bool = { a, b in
        a * b < 24
    }
    
    static let propertyThreeProduct: @Sendable (Int, Int, Int) -> Bool = { a, b, c in
        a * b * c < 24
    }
    
    static let propertyFourProduct: @Sendable (Int, Int, Int, Int) -> Bool = { a, b, c, d in
        a * b * c * d < 24
    }
    
    static let propertyFiveProduct: @Sendable (Int, Int, Int, Int, Int) -> Bool = { a, b, c, d, e in
        a * b * c * d * e < 24
    }
    
    static let propertySixProduct: @Sendable (Int, Int, Int, Int, Int, Int) -> Bool = { a, b, c, d, e, f in
        a * b * c * d * e * f < 24
    }
}
