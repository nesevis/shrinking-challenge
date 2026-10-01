//
//  SnapshotStoreChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 1/10/2026.
//

import Exhaust

enum SnapshotStoreChallenge {
    // A versioned key-value store. A snapshot sees the store as it was when the snapshot was taken, until it is released.
    // Compaction may discard any version no live snapshot can see.
    final class Store {
        struct Snapshot: Hashable {
            let id: Int
            let timestamp: Int
        }

        private var versions = [Int: [(timestamp: Int, value: Int)]]()
        private var liveSnapshots = [Int: Int]()
        private var clock = 0
        private var nextSnapshotID = 0

        func put(_ key: Int, _ value: Int) {
            clock += 1
            versions[key, default: []].append((clock, value))
        }

        func get(_ key: Int) -> Int? {
            versions[key]?.last?.value
        }

        func snapshot() -> Snapshot {
            defer { nextSnapshotID += 1 }
            liveSnapshots[nextSnapshotID] = clock
            return Snapshot(id: nextSnapshotID, timestamp: clock)
        }

        func read(_ snapshot: Snapshot, _ key: Int) -> Int? {
            versions[key]?.last(where: { $0.timestamp <= snapshot.timestamp })?.value
        }

        func release(_ snapshot: Snapshot) {
            liveSnapshots[snapshot.id] = nil
        }

        func compact() {
            // Deliberate bug: keeps history back to the newest live snapshot rather than the oldest
            let horizon = liveSnapshots.values.max() ?? clock
            for (key, keyVersions) in versions {
                guard let floor = keyVersions.lastIndex(where: { $0.timestamp <= horizon }) else {
                    continue
                }
                versions[key] = Array(keyVersions[floor...])
            }
        }
    }

    // The model never compacts: it keeps every write in order, and a snapshot remembers how many writes it can see
    @StateMachine
    final class Spec {
        static let gen = #gen(.int(in: 0...9))
        // Wide enough that every live snapshot is reachable, and the modulo's bias towards some snapshots is negligible
        static let snapshotGen = #gen(.int(in: 0...999))

        var writes = [(key: Int, value: Int)]()
        var snapshots = [(handle: Store.Snapshot, visibleWrites: Int)]()
        @SystemUnderTest var store = Store()

        @Command(gen, gen)
        func put(key: Int, value: Int) throws {
            writes.append((key, value))
            store.put(key, value)
        }

        @Command(gen)
        func get(key: Int) throws {
            try check(store.get(key) == latest(key, among: writes.count), "get(\(key))")
        }

        @Command
        func snapshot() throws {
            snapshots.append((store.snapshot(), writes.count))
        }

        @Command(snapshotGen, gen)
        func read(snapshot: Int, key: Int) throws {
            guard snapshots.isEmpty == false else { throw skip() }
            let (handle, visibleWrites) = snapshots[newestFirst(snapshot, among: snapshots.count)]
            try check(store.read(handle, key) == latest(key, among: visibleWrites), "read(\(snapshot), \(key))")
        }

        @Command(snapshotGen)
        func release(snapshot: Int) throws {
            guard snapshots.isEmpty == false else { throw skip() }
            let (handle, _) = snapshots.remove(at: newestFirst(snapshot, among: snapshots.count))
            store.release(handle)
        }

        @Command
        func compact() throws {
            store.compact()
        }

        func failureDescription() -> String? {
            "writes: \(writes), snapshots: \(snapshots.map(\.visibleWrites))"
        }

        private func latest(_ key: Int, among visibleWrites: Int) -> Int? {
            writes.prefix(visibleWrites).last(where: { $0.key == key })?.value
        }
    }

    // Resolves a generated index against the live snapshots newest first, as Hypothesis draws from a bundle, so index 0 is the newest snapshot in both libraries
    static func newestFirst(_ index: Int, among count: Int) -> Int {
        count - 1 - index % count
    }

    // Renders the commands that ran, naming snapshots s0, s1, … in creation order, as the Hypothesis machine does
    static func render(_ commands: [Spec.Command]) -> String {
        var created = 0
        var live = [String]()
        var steps = [String]()
        for command in commands {
            switch command {
            case let .put(key, value):
                steps.append("put(\(key), \(value))")
            case let .get(key):
                steps.append("get(\(key))")
            case .snapshot:
                live.append("s\(created)")
                steps.append("s\(created) = snapshot()")
                created += 1
            case let .read(snapshot, key):
                guard live.isEmpty == false else { continue }
                steps.append("read(\(live[newestFirst(snapshot, among: live.count)]), \(key))")
            case let .release(snapshot):
                guard live.isEmpty == false else { continue }
                steps.append("release(\(live.remove(at: newestFirst(snapshot, among: live.count))))")
            case .compact:
                steps.append("compact()")
            }
        }
        return "[\(steps.joined(separator: ", "))]"
    }
}
