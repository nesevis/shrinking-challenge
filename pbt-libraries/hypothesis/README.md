# Hypothesis

[Hypothesis](https://hypothesis.works/) is a property-based library for Python.
It's implemented as a standalone library and can be used with most Python testing frameworks.

## Hypothesis's Shrinking Approach

Hypothesis adopts an approach called *internal test-case reduction*, which does shrinking by manipulating the behaviour of the generation process rather than attempting to modify the generated value.

This approach is described in [an ECOOP paper about the Hypothesis reducer](https://drmaciver.github.io/papers/reduction-via-generation-preview.pdf), and is a form of [integrated shrinking](https://hypothesis.works/articles/integrated-shrinking/) which ensures by construction that all constraints from value generation also hold in shrinking.

## Implemented Challenges

- [wrong binary heap](/pbt-libraries/hypothesis/challenges/binheap.py) ([100-seed report](/pbt-libraries/hypothesis/challenges/binheap.md))
- [invoice discount rounding](/pbt-libraries/hypothesis/challenges/invoice_discount.py)
- [invoice discount rounding, fully derived](/pbt-libraries/hypothesis/challenges/invoice_discount_derived.py)
- [username/password collision](/pbt-libraries/hypothesis/challenges/username_password.py) (one fixed-start shrinking run)
- [WeightedLinearPreservation](/pbt-libraries/hypothesis/challenges/weighted_linear_preservation.py)
- [modular mapping](/pbt-libraries/hypothesis/challenges/modular_mapping.py)
- [anagrams](/pbt-libraries/hypothesis/challenges/anagrams.py) (one fixed-start shrinking run)
- [bound5](/pbt-libraries/hypothesis/challenges/bound5.py)
- [large union list](/pbt-libraries/hypothesis/challenges/large_union_list.py)
- [calculator](/pbt-libraries/hypothesis/challenges/calculator.py)
- [nested binds (composite, product sequence), depth 2](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_2.py)
- [nested binds (composite, product sequence), depth 3](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_3.py)
- [nested binds (composite, product sequence), depth 4](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_4.py)
- [nested binds (composite, product sequence), depth 5](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_5.py)
- [nested binds (composite, product sequence), depth 6](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_6.py)
- [length list](/pbt-libraries/hypothesis/challenges/lengthlist.py)
- [reverse](/pbt-libraries/hypothesis/challenges/reverse.py)

## Running Anagrams

```sh
make challenges/anagrams.md
```

Anagrams uses internal Hypothesis APIs to replay and shrink the supplied starting
pair once, with `max_stall = 2000`. It does not use Hypothesis's test-suite helpers
or perform the usual 100 generated runs. The JSON records property evaluations,
including the initial failing example.
