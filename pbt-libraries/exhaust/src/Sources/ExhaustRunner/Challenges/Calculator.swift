//
//  Calculator.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust

enum CalculatorChallenge {
    indirect enum Expr: Equatable, CustomStringConvertible {
        case value(Int)
        case add(Expr, Expr)
        case div(Expr, Expr)

        var intValue: Int? {
            guard case let .value(value) = self else { return nil }
            return value
        }

        var description: String {
            switch self {
            case let .value(value):
                "value(\(value))"
            case let .add(lhs, rhs):
                "add(\(lhs.description), \(rhs.description))"
            case let .div(lhs, rhs):
                "div(\(lhs.description), \(rhs.description))"
            }
        }
    }
    
    enum EvalError: Error {
        case divisionByZero
    }
    
    static func gen(depth: UInt64) -> ReflectiveGenerator<Expr> {
        let leaf = #gen(.int(in: -10 ... 10, scaling: .constant))
            .mapped(forward: { Expr.value($0) }, backward: { $0.intValue ?? 0 })

        return #gen(.recursive(base: leaf, depthRange: 0 ... depth) { recurse, _ in
            let add = #gen(recurse(), recurse())
                .mapped(
                    forward: { lhs, rhs in Expr.add(lhs, rhs) },
                    backward: { value in
                        switch value {
                        case let .add(lhs, rhs): (lhs, rhs)
                        case let .div(lhs, rhs): (lhs, rhs)
                        case .value:
                            (value, value)
                        }
                    }
                )
            let div = #gen(recurse(), recurse())
                .mapped(
                    forward: { lhs, rhs in Expr.div(lhs, rhs) },
                    backward: { value in
                        switch value {
                        case let .add(lhs, rhs): (lhs, rhs)
                        case let .div(lhs, rhs): (lhs, rhs)
                        case .value:
                            (value, value)
                        }
                    }
                )

            return .oneOf(weighted:
                (3, leaf),
                (3, add),
                (3, div))
        })
    }

    // MARK: - Property

    static let property: @Sendable (Expr) -> Bool = { expr in
        guard containsLiteralDivisionByZero(expr) == false else { return true }
        do {
            _ = try evalExpr(expr)
            return true
        } catch {
            return false
        }
    }

    static func evalExpr(_ expr: Expr) throws -> Int {
        switch expr {
        case let .value(value):
            return value
        case let .add(lhs, rhs):
            return try evalExpr(lhs) + evalExpr(rhs)
        case let .div(lhs, rhs):
            let denominator = try evalExpr(rhs)
            guard denominator != 0 else { throw EvalError.divisionByZero }
            return try evalExpr(lhs) / denominator
        }
    }

    static func containsLiteralDivisionByZero(_ expr: Expr) -> Bool {
        switch expr {
        case .value:
            false
        case let .add(lhs, rhs):
            containsLiteralDivisionByZero(lhs) || containsLiteralDivisionByZero(rhs)
        case .div(_, .value(0)):
            true
        case let .div(lhs, rhs):
            containsLiteralDivisionByZero(lhs) || containsLiteralDivisionByZero(rhs)
        }
    }
}
