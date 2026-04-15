//
//  BinaryHeap.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 15/4/2026.
//

import Exhaust

enum BinaryHeapChallenge {
    indirect enum Heap<Element: Comparable>: Equatable, CustomStringConvertible {
        case empty
        case node(Element, Heap, Heap)
        
        var description: String {
            switch self {
            case .empty:
                "None"
            case let .node(value, left, right):
                "(\(value), \(left.description), \(right.description))"
            }
        }
    }
    
    static let property: @Sendable (Heap<Int>) -> Bool = { heap in
        guard heapInvariant(heap) else { return true }
        let sorted = heapToSortedList(heap)
        let reference = heapToList(heap).sorted()
        return reference == sorted.sorted() && sorted == sorted.sorted()
    }

    // MARK: - Generator
    
    static let gen = #gen(.uint64(in: 0 ... 20)).bind {
        build(depth: $0)
    }

    static func build(min: Int = 0, depth: UInt64) -> ReflectiveGenerator<Heap<Int>> {
        let maxVal = Int.max
        let emptyGen: ReflectiveGenerator<Heap<Int>> = #gen(.just(.empty))

        guard depth > 0, min <= maxVal else {
            return emptyGen
        }

        let nodeGen = #gen(.int(in: min ... maxVal))
            .bind { value in
                #gen(
                    build(min: value, depth: depth / 2),
                    build(min: value, depth: depth / 2)
                )
                .mapped(
                    forward: { left, right in Heap.node(value, left, right) },
                    backward: { heap in
                        switch heap {
                        case let .node(_, left, right): (left, right)
                        case .empty: (.empty, .empty)
                        }
                    }
                )
            }

        return #gen(.oneOf(weighted: (1, emptyGen), (5, nodeGen)))
    }

    // MARK: - Buggy Heap Operations

    static func heapToList<Element>(_ heap: Heap<Element>) -> [Element] {
        var queue = [heap]
        var result: [Element] = []
        while queue.isEmpty == false {
            let current = queue.removeFirst()
            switch current {
            case .empty:
                continue
            case let .node(x, h1, h2):
                result.append(x)
                queue.append(h1)
                queue.append(h2)
            }
        }
        return result
    }

    static func heapToSortedList<Element: Comparable>(_ heap: Heap<Element>) -> [Element] {
        switch heap {
        case .empty:
            []
        case let .node(x, h1, h2):
            [x] + heapToList(heapMerge(h1, h2))
        }
    }

    private static func heapMerge<Element: Comparable>(_ h1: Heap<Element>, _ h2: Heap<Element>) -> Heap<Element> {
        switch (h1, h2) {
        case (_, .empty):
            h1
        case (.empty, _):
            h2
        case let (.node(x, h11, h12), .node(y, h21, h22)):
            if x <= y {
                .node(x, heapMerge(h12, h2), h11)
            } else {
                .node(y, heapMerge(h22, h1), h21)
            }
        }
    }

    static func heapInvariant(_ heap: Heap<some Comparable>) -> Bool {
        switch heap {
        case .empty:
            true
        case let .node(x, h1, h2):
            heapLte(x, h1) && heapLte(x, h2) && heapInvariant(h1) && heapInvariant(h2)
        }
    }

    private static func heapLte<Element: Comparable>(_ x: Element, _ heap: Heap<Element>) -> Bool {
        switch heap {
        case .empty:
            true
        case let .node(y, _, _):
            x <= y
        }
    }
}
