//
//  InvoiceDiscountChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust

enum InvoiceDiscountChallenge {
    @Exhaustable // Synthesises a generator
    struct Invoice: CustomStringConvertible {
        let unitPriceCents: Int
        let quantity: Int
        let discountPercent: Int

        func totalCents() -> Int {
            // Deliberate bug: round each unit before multiplying by quantity
            let discountedUnit = (unitPriceCents * (100 - discountPercent)) / 100
            return discountedUnit * quantity
        }

        var description: String {
            "Invoice(\(unitPriceCents), \(quantity), \(discountPercent))"
        }
    }

    static let gen = #gen(.int(in: 1 ... 1_000), .int(in: 1 ... 100))
        .bind { price, quantity in
            let eligible = price * quantity >= 1_000
            let discountGen = #gen(eligible ? .int(in: 0 ... 50) : .just(0))
            
            return discountGen.map { discount in
                Invoice(unitPriceCents: price, quantity: quantity, discountPercent: discount)
            }
        }

    static let derivedGen = Invoice.gen()

    static let property: @Sendable (Invoice) -> Bool = { invoice in
        invoice.totalCents() == expectedTotal(invoice)
    }

    static let derivedProperty: @Sendable (Invoice) throws -> Bool = { invoice in
        guard isValid(invoice) else {
            throw PropertySkip()
        }
        return property(invoice)
    }

    // Business rule: discount the whole invoice, then round down once
    static func expectedTotal(_ invoice: Invoice) -> Int {
        (invoice.unitPriceCents * invoice.quantity * (100 - invoice.discountPercent)) / 100
    }

    static func isValid(_ invoice: Invoice) -> Bool {
        // Guarding here so @Exhaustable's derived generator can use this as well
        guard
            (1...1_000).contains(invoice.unitPriceCents),
            (1...100).contains(invoice.quantity),
            (0...50).contains(invoice.discountPercent)
        else {
            return false
        }
        let eligible = invoice.unitPriceCents * invoice.quantity >= 1_000
        return eligible || invoice.discountPercent == 0
    }
}
