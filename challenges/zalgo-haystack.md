# Zalgo Haystack

A fixed-start deletion challenge: reduce the original Zalgo passage while preserving
an occurrence of `the ichor permeates` after Unicode normalization.

## Property

1. Canonically decompose the candidate (NFD).
2. Remove nonspacing, spacing-combining, and enclosing marks (`Mn`, `Mc`, `Me`).
3. Remove format characters (`Cf`), including the source's zero-width spaces.
4. Lowercase and search for the literal substring `the ichor permeates`.

The property fails when that substring is present. Only matching is normalized;
the reducer receives the original decorated text. Spaces and punctuation are not
stripped, and compatibility characters are not transliterated. An undecorated
`the ichor permeates` is a 19-scalar counterexample; letter case can vary.
The normalized starting input contains this phrase once, with a zero-width space
inside `ichor` in the original.

The identical 3,237-scalar input is pasted as a string literal into
`pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/ZalgoHaystackChallenge.swift`
and `pbt-libraries/hypothesis/challenges/zalgo_haystack.py`.
It is the first paragraph of the source answer, with HTML formatting tags removed
and entities decoded, preserving its combining marks and format characters. The
XML-parser suggestion and moderator note are excluded. Macbeth `haystack` remains
unchanged.

## Run

From `pbt-libraries/exhaust/src`:

```sh
swift run -c release ExhaustRunner --challenge zalgoHaystack --iterations 1
```

From `pbt-libraries/hypothesis`:

```sh
venv/bin/python support/run_challenge.py challenges/zalgo_haystack.py
```

Both are single fixed-start reductions, with no failure-generation phase.
Exhaust uses reflection; Hypothesis uses its private strategy `_invert` method.
Hegel is excluded because the pinned public API has no equivalent inversion or
reflection support; its explicit test cases bypass generators rather than seed
shrinking.

## Verification

Smoke runs with seed 1337 reduced both inputs to the undecorated uppercase needle:

| Needle | Hypothesis 6.168.3 evaluations | Exhaust checkout `65c030739` evaluations |
|---|---:|---:|
| `the pony` (previous needle) | 182 | 187 |
| `the ichor permeates` (current needle) | 444 | 461 |

Both current reductions produce `"THE ICHOR PERMEATES"`.

These are not the published Exhaust 1.5.3 benchmark results. Hypothesis counts the
initial evaluation; Exhaust's printed count is `report.reductionInvocations`,
without adding an initial call.
Source fidelity, identical literals, Hypothesis inversion round-trip, and matching
of precomposed accents, all three mark categories, format characters, and mixed
case were checked. Negative examples preserve the literal space requirement.

## Attribution

Adapted from [bobince's Stack Overflow answer](https://stackoverflow.com/a/1732454)
to “RegEx match open tags except XHTML self-contained tags”, retrieved October 2,
2026 via the Stack Exchange API. The retrieved revision is licensed
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); the copied passage
and its adaptation retain that license. Changes: HTML presentation removed and
only the first paragraph retained.
