# Username and Password Report for Exhaust

These results are from Exhaust v1.5.2, October 1st, 2026.

## Normalization

Exhaust reduced the fixed starting example `("u: passw0rd", "p: passw0rd")` once, passing it to `#exhaust` with `reflecting:` instead of generating a failure:

| Counterexample |
|---|
| `("u: 0000", "p: 0000")` |

The minimal counterexample is `("u: 0000", "p: 0000")`.

See [the starting input](/pbt-libraries/exhaust/failures/usernamePassword.json).

## Performance

| Metric | Value |
|---|---|
| Evaluations | 723 |
| Reduction time (ms) | 5.81 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge usernamePassword --iterations 1`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
