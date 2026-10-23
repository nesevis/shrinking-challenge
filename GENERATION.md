# Generation benchmarks

1,000 runs per batch, always passing; 1 seed (1337). Apple M4 Max, macOS.

| Library | Version | Configuration | Timing |
|---|---|---|---|
| Hypothesis | 6.168.3 | Python 3.12 | 1 batch |
| Hegel | 0.49.14 (engine 0.45.13) | Debug runner, core opt-level 1 | 1 batch |

## Generation

Milliseconds per 1,000 generated values.

Exhaust 1.7.4 columns show the median of ten fresh-process batches per workload; both configurations are measured on this Mac.

| Generator | Hypothesis | Hegel (default/opt-1) | Exhaust (macOS) | Exhaust (Linux/Windows) |
|---|---:|---:|---:|---:|
| Binary Heap | 1,313.77 ms | 43.06 ms | 27.98 ms | 49.35 ms |
| Calculator | 15,288.09 ms | 56.71 ms | 1.30 ms | 3.26 ms |
| Nested Flatmap (product sequence), depth 2 | 632.79 ms | 22.92 ms | 1.17 ms | 5.53 ms |
| Nested Flatmap (product sequence), depth 3 | 1,431.56 ms | 44.25 ms | 1.80 ms | 15.30 ms |
| Modular Mapping | 262.33 ms | 5.41 ms | 0.37 ms | 0.55 ms |
| Weighted Linear Preservation | 274.32 ms | 7.00 ms | 0.60 ms | 1.20 ms |
| Invoice Discount | 283.42 ms | 6.99 ms | 1.43 ms | 2.19 ms |
| Invoice Discount (derived) | 240.31 ms | 7.31 ms | 0.64 ms | 1.72 ms |
| Refund Allocation | 579.03 ms | 12.30 ms | 3.00 ms | 5.17 ms |
| Refund Allocation (derived) | 424.14 ms | 11.75 ms | 2.42 ms | 5.97 ms |
| Float Cancellation | 258.28 ms | 6.15 ms | 0.65 ms | 1.38 ms |
| Chunked Decoder | 486.72 ms | 11.96 ms | 3.82 ms | 10.35 ms |
| Hash Collision (M = 10) | 512.59 ms | 14.54 ms | 2.86 ms | 7.17 ms |
| Hash Collision (M = 100) | 518.40 ms | 14.55 ms | 2.78 ms | 6.62 ms |
| Hash Collision (M = 1000) | 581.76 ms | 14.49 ms | 2.98 ms | 6.83 ms |
| Snapshot Store | 3,918.12 ms | 1,382.35 ms | 9.69 ms | 30.25 ms |
| Hash Collision (M = 10) (state machine) | 3,419.80 ms | 199.50 ms | 13.52 ms | 33.68 ms |
| Hash Collision (M = 100) (state machine) | 3,105.93 ms | 209.02 ms | 13.19 ms | 33.42 ms |
| Hash Collision (M = 1000) (state machine) | 2,959.78 ms | 202.85 ms | 13.73 ms | 33.60 ms |

## Generated value complexity

Mean / median / maximum.

| Generator | Metric | Hypothesis | Hegel (default/opt-1) | Exhaust |
|---|---|---:|---:|---:|
| Binary Heap | Maximum depth | 3.42<br>4.00<br>5.00 | 3.23<br>4.00<br>5.00 | 2.80<br>3.00<br>5.00 |
| Binary Heap | Nodes | 8.54<br>7.00<br>30.00 | 8.60<br>7.00<br>31.00 | 7.84<br>6.00<br>31.00 |
| Calculator | Maximum depth | 3.25<br>3.00<br>24.00 | 5.15<br>6.00<br>6.00 | 1.98<br>2.00<br>6.00 |
| Calculator | Nodes | 6.22<br>5.00<br>59.00 | 23.24<br>23.00<br>51.00 | 3.26<br>3.00<br>19.00 |
| Nested Flatmap (product sequence), depth 2 | Payload elements | 31.03<br>25.00<br>100.00 | 27.88<br>20.00<br>100.00 | 22.25<br>12.00<br>100.00 |
| Nested Flatmap (product sequence), depth 3 | Payload elements | 96.95<br>32.00<br>1,000.00 | 75.55<br>36.00<br>576.00 | 76.16<br>20.00<br>1,000.00 |
| Modular Mapping | Mean integer bit length | 8.98<br>9.00<br>10.00 | 8.86<br>9.00<br>10.00 | 8.97<br>9.00<br>10.00 |
| Weighted Linear Preservation | Mean integer bit length | 3.53<br>3.67<br>5.00 | 3.46<br>3.67<br>5.00 | 3.52<br>3.67<br>5.00 |
| Invoice Discount | Mean integer bit length | 5.21<br>5.67<br>7.67 | 5.46<br>6.00<br>7.67 | 6.44<br>6.67<br>7.67 |
| Invoice Discount (derived) | Mean integer bit length | 21.84<br>18.00<br>104.00 | 19.19<br>16.67<br>63.00 | 30.89<br>31.00<br>62.67 |
| Refund Allocation | Charges | 7.41<br>6.00<br>20.00 | 7.78<br>6.00<br>20.00 | 6.04<br>5.00<br>20.00 |
| Refund Allocation | Mean integer bit length | 17.84<br>18.02<br>59.00 | 17.75<br>16.89<br>51.00 | 61.88<br>62.00<br>63.00 |
| Refund Allocation (derived) | Charges | 5.89<br>5.00<br>25.00 | 6.99<br>5.00<br>33.00 | 3.24<br>2.00<br>22.00 |
| Refund Allocation (derived) | Mean integer bit length | 22.35<br>21.00<br>123.00 | 19.44<br>18.00<br>64.00 | 30.89<br>31.12<br>62.67 |
| Chunked Decoder | Chunks | 6.49<br>5.00<br>24.00 | 5.56<br>4.00<br>32.00 | 8.34<br>6.00<br>34.00 |
| Chunked Decoder | Encoded bytes | 12.03<br>10.00<br>42.00 | 10.14<br>8.00<br>64.00 | 15.84<br>12.00<br>60.00 |
| Hash Collision (M = 10) | Entries | 5.68<br>4.00<br>20.00 | 7.23<br>6.00<br>20.00 | 5.44<br>4.00<br>20.00 |
| Hash Collision (M = 100) | Entries | 5.77<br>5.00<br>20.00 | 7.03<br>6.00<br>20.00 | 5.44<br>4.00<br>20.00 |
| Hash Collision (M = 1000) | Entries | 5.89<br>4.00<br>20.00 | 7.03<br>6.00<br>20.00 | 5.44<br>4.00<br>20.00 |
| Snapshot Store | Commands per history | 44.55<br>50.00<br>50.00 | 49.30<br>50.00<br>50.00 | 25.08<br>25.00<br>50.00 |
| Hash Collision (M = 10) (state machine) | Commands per history | 49.76<br>50.00<br>50.00 | 49.73<br>50.00<br>50.00 | 25.08<br>25.00<br>50.00 |
| Hash Collision (M = 100) (state machine) | Commands per history | 49.75<br>50.00<br>50.00 | 49.69<br>50.00<br>50.00 | 25.08<br>25.00<br>50.00 |
| Hash Collision (M = 1000) (state machine) | Commands per history | 49.67<br>50.00<br>50.00 | 49.69<br>50.00<br>50.00 | 25.08<br>25.00<br>50.00 |

