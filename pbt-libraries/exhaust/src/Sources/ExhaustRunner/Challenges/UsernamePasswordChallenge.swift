//
//  UsernamePasswordChallenge.swift
//  ExhaustRunner
//
//  Created by Chris Kolbu on 30/9/2026.
//

import Exhaust
import Foundation

enum UsernamePasswordChallenge {
    static let userPrefix = "u: "
    static let passwordPrefix = "p: "
    static let credentialCharacters = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    static let stringGen = #gen(.string(from: CharacterSet(charactersIn: credentialCharacters + ": ")))
    static let gen = #gen(stringGen, stringGen)
    static let input = ("\(userPrefix)passw0rd", "\(passwordPrefix)passw0rd")

    static let property: @Sendable (String, String) -> Bool = { user, pass in
        guard
            user.hasPrefix(userPrefix),
            pass.hasPrefix(passwordPrefix)
        else {
            return true
        }
        
        let username = user.dropFirst(userPrefix.count)
        let password = pass.dropFirst(passwordPrefix.count)
        
        guard
            password.count >= 4,
            password.allSatisfy(credentialCharacters.contains)
        else {
            return true
        }
        
        return username != password
    }
}
