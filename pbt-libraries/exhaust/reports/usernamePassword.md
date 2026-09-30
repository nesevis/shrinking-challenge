# Username and Password Report for Exhaust

These results are from Exhaust v1.5.1, September 30th, 2026.

## Normalization

Exhaust reduced the fixed starting example `("u: passw0rd", "p: passw0rd")` once, passing it to `#exhaust` with `reflecting:` instead of generating a failure:

| Counterexample |
|---|
| `("u: 0000", "p: 0000")` |

This is the semantic optimum.

See [the starting input](/pbt-libraries/exhaust/failures/usernamePassword.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 723.0 | 723.0 | 723.0 | 723.0 | 723.0–723.0 |
| Reduction time (ms) | 4.72 | 4.72 | 4.72 | 4.72 | 4.72–4.72 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge usernamePassword --iterations 100`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
