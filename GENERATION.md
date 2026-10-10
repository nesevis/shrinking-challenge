# Generation benchmarks

1,000 runs per batch, always passing; 1 seed (1337). Apple M4 Max, macOS.

| Library | Version | Configuration | Timing |
|---|---|---|---|
| Hypothesis | 6.168.3 | Python 3.12 | 1 batch |
| Hegel | 0.48.1 (engine 0.44.1) | Debug runner, core opt-level 1 | 1 batch |
| Exhaust (macOS) | 1.6.0 | Debug runner, optimised XCFramework | Median of 10 batches |
| Exhaust (Linux/Windows) | 1.6.0 | Debug runner and source core, measured on macOS | Median of 10 batches |

## Generation

Milliseconds per 1,000 generated values.

| Generator | Hypothesis | Hegel (default/opt-1) | Exhaust (macOS) | Exhaust (Linux/Windows) |
|---|---:|---:|---:|---:|
| Binary Heap | 1,313.77 ms | 31.14 ms | 29.01 ms | 49.96 ms |
| Calculator | 15,288.09 ms | 41.32 ms | 1.51 ms | 3.63 ms |
| Nested Flatmap (product sequence), depth 2 | 632.79 ms | 16.00 ms | 1.26 ms | 6.16 ms |
| Nested Flatmap (product sequence), depth 3 | 1,431.56 ms | 38.59 ms | 1.83 ms | 16.03 ms |
| Modular Mapping | 262.33 ms | 5.35 ms | 0.41 ms | 0.63 ms |
| Weighted Linear Preservation | 274.32 ms | 6.51 ms | 0.61 ms | 1.18 ms |
| Invoice Discount | 283.42 ms | 6.46 ms | 1.44 ms | 2.34 ms |
| Invoice Discount (derived) | 240.31 ms | 6.93 ms | 0.68 ms | 1.79 ms |
| Refund Allocation | 579.03 ms | 12.33 ms | 3.25 ms | 5.28 ms |
| Refund Allocation (derived) | 424.14 ms | 10.89 ms | 2.43 ms | 6.32 ms |
| Float Cancellation | 258.28 ms | 6.15 ms | 0.60 ms | 1.18 ms |
| Chunked Decoder | 486.72 ms | 12.28 ms | 3.90 ms | 10.40 ms |
| Hash Collision (M = 10) | 512.59 ms | 14.03 ms | 3.00 ms | 7.08 ms |
| Hash Collision (M = 100) | 518.40 ms | 14.47 ms | 3.03 ms | 7.23 ms |
| Hash Collision (M = 1000) | 581.76 ms | 14.45 ms | 3.05 ms | 7.41 ms |
| Snapshot Store | 3,918.12 ms | 969.16 ms | 9.85 ms | 31.30 ms |
| Hash Collision (M = 10) (state machine) | 3,419.80 ms | 208.47 ms | 13.74 ms | 34.19 ms |
| Hash Collision (M = 100) (state machine) | 3,105.93 ms | 210.26 ms | 14.11 ms | 34.46 ms |
| Hash Collision (M = 1000) (state machine) | 2,959.78 ms | 208.86 ms | 13.90 ms | 34.40 ms |

## Generated value complexity

Mean / median / maximum.

| Generator | Metric | Hypothesis | Hegel (default/opt-1) | Exhaust |
|---|---|---:|---:|---:|
| Binary Heap | Maximum depth | 3.42<br>4.00<br>5.00 | 3.19<br>4.00<br>5.00 | 2.80<br>3.00<br>5.00 |
| Binary Heap | Nodes | 8.54<br>7.00<br>30.00 | 8.29<br>7.00<br>29.00 | 7.84<br>6.00<br>31.00 |
| Calculator | Maximum depth | 3.25<br>3.00<br>24.00 | 4.36<br>6.00<br>6.00 | 1.98<br>2.00<br>6.00 |
| Calculator | Nodes | 6.22<br>5.00<br>59.00 | 18.42<br>17.00<br>53.00 | 3.26<br>3.00<br>19.00 |
| Nested Flatmap (product sequence), depth 2 | Payload elements | 31.03<br>25.00<br>100.00 | 18.19<br>12.00<br>81.00 | 22.25<br>12.00<br>100.00 |
| Nested Flatmap (product sequence), depth 3 | Payload elements | 96.95<br>32.00<br>1,000.00 | 59.53<br>20.00<br>640.00 | 76.16<br>20.00<br>1,000.00 |
| Modular Mapping | Mean integer bit length | 8.98<br>9.00<br>10.00 | 8.86<br>9.00<br>10.00 | 8.97<br>9.00<br>10.00 |
| Weighted Linear Preservation | Mean integer bit length | 3.53<br>3.67<br>5.00 | 3.42<br>3.67<br>5.00 | 3.52<br>3.67<br>5.00 |
| Invoice Discount | Mean integer bit length | 5.21<br>5.67<br>7.67 | 4.72<br>5.33<br>7.67 | 6.44<br>6.67<br>7.67 |
| Invoice Discount (derived) | Mean integer bit length | 21.84<br>18.00<br>104.00 | 19.65<br>17.00<br>63.00 | 30.89<br>31.00<br>62.67 |
| Refund Allocation | Charges | 7.41<br>6.00<br>20.00 | 7.41<br>6.00<br>20.00 | 6.04<br>5.00<br>20.00 |
| Refund Allocation | Mean integer bit length | 17.84<br>18.02<br>59.00 | 17.41<br>16.62<br>49.75 | 61.88<br>62.00<br>63.00 |
| Refund Allocation (derived) | Charges | 5.89<br>5.00<br>25.00 | 5.47<br>4.00<br>37.00 | 3.24<br>2.00<br>22.00 |
| Refund Allocation (derived) | Mean integer bit length | 22.35<br>21.00<br>123.00 | 19.38<br>17.00<br>64.00 | 30.89<br>31.12<br>62.67 |
| Float Cancellation | Mean absolute binary exponent | 158.45<br>19.00<br>1,074.00 | 265.84<br>19.00<br>1,028.00 | 17.93<br>18.00<br>19.00 |
| Chunked Decoder | Chunks | 6.49<br>5.00<br>24.00 | 5.65<br>4.00<br>23.00 | 8.34<br>6.00<br>34.00 |
| Chunked Decoder | Encoded bytes | 12.03<br>10.00<br>42.00 | 10.29<br>8.00<br>43.00 | 15.84<br>12.00<br>60.00 |
| Hash Collision (M = 10) | Entries | 5.68<br>4.00<br>20.00 | 6.11<br>4.00<br>20.00 | 5.44<br>4.00<br>20.00 |
| Hash Collision (M = 100) | Entries | 5.77<br>5.00<br>20.00 | 6.11<br>4.00<br>20.00 | 5.44<br>4.00<br>20.00 |
| Hash Collision (M = 1000) | Entries | 5.89<br>4.00<br>20.00 | 6.11<br>4.00<br>20.00 | 5.44<br>4.00<br>20.00 |
| Snapshot Store | Commands per history | 44.55<br>50.00<br>50.00 | 48.96<br>50.00<br>50.00 | 25.08<br>25.00<br>50.00 |
| Hash Collision (M = 10) (state machine) | Commands per history | 49.76<br>50.00<br>50.00 | 49.78<br>50.00<br>50.00 | 25.08<br>25.00<br>50.00 |
| Hash Collision (M = 100) (state machine) | Commands per history | 49.75<br>50.00<br>50.00 | 49.78<br>50.00<br>50.00 | 25.08<br>25.00<br>50.00 |
| Hash Collision (M = 1000) (state machine) | Commands per history | 49.67<br>50.00<br>50.00 | 49.78<br>50.00<br>50.00 | 25.08<br>25.00<br>50.00 |
