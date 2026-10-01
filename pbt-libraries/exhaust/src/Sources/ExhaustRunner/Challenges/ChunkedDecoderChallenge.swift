//
//  ChunkedDecoderChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 1/10/2026.
//

import Exhaust

enum ChunkedDecoderChallenge {
    // A message's kind travels out of band, like a WebSocket opcode; only its content is encoded
    enum Message: Equatable, CustomStringConvertible {
        case binary([UInt8])
        case text(String)

        var description: String {
            switch self {
            case let .binary(bytes): "binary, \(bytes)"
            case let .text(text): "text, \(escaped(text))"
            }
        }
    }

    struct Transmission: CustomStringConvertible {
        let message: Message
        let cuts: [Bool]

        var description: String {
            "(\(message), \(split(encode(message), cuts: cuts).map(\.count)))"
        }
    }

    static let binaryGen = #gen(.uint8().array(length: 0...64))
        .map(Message.binary)
    static let textGen = #gen(.string(length: 0...16))
        .map(Message.text)

    // The transport may split the encoded bytes anywhere: one flag per gap between bytes says whether a chunk boundary falls there
    static let gen = #gen(.oneOf(binaryGen, textGen))
        .bind { message in
            let gaps = max(encode(message).count - 1, 0)
            return .bool().array(length: gaps)
                .map { cuts in Transmission(message: message, cuts: cuts) }
        }

    static let property: @Sendable (Transmission) -> Bool = { transmission in
        let chunks = split(encode(transmission.message), cuts: transmission.cuts)
        return decode(kind: transmission.message, chunks: chunks) == transmission.message
    }

    static func encode(_ message: Message) -> [UInt8] {
        switch message {
        case let .binary(bytes): bytes
        case let .text(text): Array(text.utf8)
        }
    }

    // Deliberate bug: text chunks are decoded independently, so a scalar split across two chunks becomes replacement characters
    static func decode(kind: Message, chunks: [[UInt8]]) -> Message {
        switch kind {
        case .binary: .binary(chunks.flatMap { $0 })
        case .text: .text(chunks.map { String(decoding: $0, as: UTF8.self) }.joined())
        }
    }

    static func split(_ bytes: [UInt8], cuts: [Bool]) -> [[UInt8]] {
        guard bytes.isEmpty == false else {
            return []
        }
        var chunks = [[bytes[0]]]
        for (byte, cut) in zip(bytes.dropFirst(), cuts) {
            if cut {
                chunks.append([byte])
            } else {
                chunks[chunks.count - 1].append(byte)
            }
        }
        return chunks
    }
}

// MARK: - Helpers

// Escapes every scalar outside printable ASCII, so control characters and invisible scalars show up in reports
private func escaped(_ text: String) -> String {
    let body = text.unicodeScalars.map { scalar in
        switch scalar {
        case "\"": "\\\""
        case "\\": "\\\\"
        case " "..."~": String(scalar)
        default: "\\u{\(String(scalar.value, radix: 16))}"
        }
    }
    return "\"\(body.joined())\""
}
