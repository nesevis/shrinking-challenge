# Haystack Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

## Normalization

Exhaust reduced this fixed starting example once, passing it to `#exhaust` with `reflecting:` instead of generating a failure:

```
"""
She should have died hereafter;
There would have been a time for such a word.
Tomorrow, and tomorrow, and tomorrow,
Creeps in this petty pace from day to day,
To the last syllable of recorded time;
And all our yesterdays have lighted fools
The way to dusty death. Out, out, brief candle!
Life's but a walking shadow, a poor player,
That struts and frets his hour upon the stage,
And then is heard no more. It is a tale
Told by an idiot, full of sound and fury,
Signifying nothing.
"""
```

| Counterexample |
|---|
| `"Creepidiot"` |

The property lowercases the text and fails when it contains both `"creep"` and `"idiot"`. The minimal counterexample has ten characters.

See [the starting input](/pbt-libraries/exhaust/failures/haystack.json).

## Performance

| Metric | Value |
|---|---|
| Evaluations | 4582 |
| Reduction time (ms) | 86.62 |
| Wall time (ms) | 89.812 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge haystack --iterations 1`

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
