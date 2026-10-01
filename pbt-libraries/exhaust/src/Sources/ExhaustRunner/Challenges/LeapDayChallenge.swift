//
//  LeapDayChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust
import Foundation

enum LeapDayChallenge {
    static let gen = #gen(
        .date(
            between: Date.distantPast...Date.distantFuture,
            interval: .minutes(1)
        )
    )

    static let calendar: Calendar = {
        var calendar = Calendar(identifier: .gregorian)
        calendar.timeZone = TimeZone(identifier: "UTC")!
        return calendar
    }()

    static let input = calendar.date(
        from: DateComponents(year: 2088, month: 2, day: 29, hour: 13, minute: 47)
    )!

    static let property: @Sendable (Date) -> Bool = { date in
        let parts = calendar.dateComponents([.month, .day], from: date)
        return (parts.month == 2 && parts.day == 29) == false
    }
}
