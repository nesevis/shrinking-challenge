//
//  HashCollisionChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 1/10/2026.
//

import Exhaust
import Foundation

// One fixture for every hash modulus: keys are drawn from 0..<10M, so collisions are distinct keys congruent mod M
enum HashCollisionChallenge {
    // A map whose hash code is the key mod M
    struct HashMap {
        let modulus: Int
        private var entries = [(key: Int, value: Int)]()

        init(modulus: Int) {
            self.modulus = modulus
        }

        // Deliberate bug: put and get match entries by hash code rather than by key, so a key overwrites and reads any key sharing its hash
        mutating func put(_ key: Int, _ value: Int) {
            if let index = entries.firstIndex(where: { hash($0.key) == hash(key) }) {
                entries[index].value = value
            } else {
                entries.append((key, value))
            }
        }

        func get(_ key: Int) -> Int? {
            entries.first(where: { hash($0.key) == hash(key) })?.value
        }

        private func hash(_ key: Int) -> Int {
            key % modulus
        }
    }

    static func keyGen(modulus: Int) -> ReflectiveGenerator<Int> {
        #gen(.int(in: 0...(10 * modulus - 1)))
    }

    static let valueGen = #gen(.int(in: 0...9))

    static func gen(modulus: Int) -> ReflectiveGenerator<([(Int, Int)], Int, Int)> {
        let keyGen = keyGen(modulus: modulus)
        let entryGen = #gen(keyGen, valueGen)
        return #gen(entryGen.array(length: 0...20), keyGen, valueGen)
    }

    // Frame property: putting a key leaves every other key in the map unchanged
    static func property(modulus: Int) -> @Sendable ([(Int, Int)], Int, Int) -> Bool {
        { entries, key, value in
            var map = HashMap(modulus: modulus)
            for (entryKey, entryValue) in entries {
                map.put(entryKey, entryValue)
            }
            let otherKeys = Set(entries.map(\.0)).subtracting([key]).sorted()
            let before = otherKeys.map { map.get($0) }
            map.put(key, value)
            return otherKeys.map { map.get($0) } == before
        }
    }

    // Shared by the state machine specs: puts the key, and reports whether every other key put so far kept its value
    static func framePreserved(putting key: Int, _ value: Int, into map: inout HashMap, keys: inout Set<Int>) -> Bool {
        let otherKeys = keys.subtracting([key]).sorted()
        let before = otherKeys.map { map.get($0) }
        map.put(key, value)
        keys.insert(key)
        return otherKeys.map { map.get($0) } == before
    }

    // Renders command descriptions without argument labels, matching the Hypothesis machine: put(key: 0, value: 1) becomes put(0, 1)
    static func render(_ commands: [some CustomStringConvertible]) -> String {
        let steps = commands.map { "\($0)".replacingOccurrences(of: #"\w+: "#, with: "", options: .regularExpression) }
        return "[\(steps.joined(separator: ", "))]"
    }

    // The same frame property as a state machine, checked after every put. A spec is created with init(), so each modulus has its own spec
    @StateMachine
    final class SpecTen {
        static let keyGen = HashCollisionChallenge.keyGen(modulus: 10)

        var keys = Set<Int>()
        @SystemUnderTest var map = HashMap(modulus: 10)

        @Command(keyGen, valueGen)
        func put(key: Int, value: Int) throws {
            try check(framePreserved(putting: key, value, into: &map, keys: &keys), "put(\(key), \(value)) changed another key")
        }

        func failureDescription() -> String? {
            "keys: \(keys.sorted())"
        }
    }

    @StateMachine
    final class SpecHundred {
        static let keyGen = HashCollisionChallenge.keyGen(modulus: 100)

        var keys = Set<Int>()
        @SystemUnderTest var map = HashMap(modulus: 100)

        @Command(keyGen, valueGen)
        func put(key: Int, value: Int) throws {
            try check(framePreserved(putting: key, value, into: &map, keys: &keys), "put(\(key), \(value)) changed another key")
        }

        func failureDescription() -> String? {
            "keys: \(keys.sorted())"
        }
    }

    @StateMachine
    final class SpecThousand {
        static let keyGen = HashCollisionChallenge.keyGen(modulus: 1000)

        var keys = Set<Int>()
        @SystemUnderTest var map = HashMap(modulus: 1000)

        @Command(keyGen, valueGen)
        func put(key: Int, value: Int) throws {
            try check(framePreserved(putting: key, value, into: &map, keys: &keys), "put(\(key), \(value)) changed another key")
        }

        func failureDescription() -> String? {
            "keys: \(keys.sorted())"
        }
    }
}
