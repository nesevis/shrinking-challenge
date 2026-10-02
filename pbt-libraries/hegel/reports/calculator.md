# Calculator — Hegel

Hegel 0.48.1, native engine 0.44.1, release build. **100 generated-and-shrunk
runs**, using the numeric seeds recorded in Hypothesis's calculator results.
[Raw results](calculator.json). Equal seeds do not imply equal starting expressions.

| Metric | Mean / count |
|---|---:|
| Runs | 100 |
| Distinct reduced counterexamples | 1 |
| Reference minimum | 100% |
| Evaluations from first failure | 446.89 |
| Original counterexample length | 240.63 |
| Total elapsed time (ms) | 101.94 |

Every run reduced to:

```text
('/', 0, ('+', 0, 0))
```

There is no literal division by zero, but the denominator evaluates to zero.
All 200 recorded original/reduced expressions independently reproduced a
`ZeroDivisionError` in Hypothesis's calculator evaluator and passed its literal
zero-divisor precondition.

## Semantics and generator

- Expressions are integer literals, additions, and divisions, constructed with
  Hegel's public `recursive` and `one_of!` generators.
- Integer leaves are signed 64-bit; maximum branch depth is 5 and maximum leaf
  count is 32. These bounds differ from Hypothesis's unbounded integer and deferred
  expression strategy. The depth limit follows the existing Exhaust runner.
- Literal `x / 0` anywhere in the tree rejects the example, matching Hypothesis's
  assumption rather than filtering the generator.
- Evaluation uses exact `i128` intermediates and Python-style floor division.
  The bounded tree guarantees intermediates fit. This intentionally differs from
  Exhaust's wrapping addition and truncating division, so machine overflow is not
  counted as a calculator failure.
- Counts include confirmation and final replay. Total time includes generation
  and reduction; Hegel does not expose separate phase timings.

## Current comparison

The updated Hypothesis 6.168.3 run also reached this result in 100/100 trials,
with 90.53 mean completed property evaluations and 1538.10 ms mean total elapsed
time. Exhaust's supplied 100-run summary likewise reports 100% at the equivalent
`div(value(0), add(value(0), value(0)))`, with 53.2 reduction invocations and
0.687 ms wall time. The README adds the initial call to Exhaust's evaluation
mean. Generator domains, evaluation semantics, and accounting differ as described
above and in the library reports; these are not paired-start performance results.

## Reproduction

From `pbt-libraries/hegel`:

```sh
cargo run --release --locked -- --challenge calculator --iterations 100 --seed-file support/calculator-seeds.json --output reports
```

The standalone port is included in `--list` but excluded from `--challenge all`
and the existing comparison-report scripts. `support/calculator-seeds.json`
contains the 100 numeric seeds from the recorded Hypothesis calculator results.
