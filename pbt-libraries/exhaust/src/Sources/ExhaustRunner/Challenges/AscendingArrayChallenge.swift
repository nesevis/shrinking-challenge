import Exhaust

/// Generates raw signed arrays and fails when the values are sorted and unique.
enum AscendingArrayChallenge {
  static let gen = #gen(.int().array(length: 5...10))

  static let property: @Sendable ([Int]) -> Bool = { values in
    (Set(values).count == values.count && values.elementsEqual(values.sorted())) == false
  }
}
