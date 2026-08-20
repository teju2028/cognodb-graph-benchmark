# Benchmark Results Analysis

## CognoDB Cloud Results

### Successful Tests

| Workload | Dataset | Result |
|---|---:|---:|
| Graph creation | 1,000 nodes | 6.5196 seconds |
| Node lookup | 1,000 nodes | 0.2729 seconds |
| 5-hop traversal | 1,000 nodes | 0.2667 seconds |
| 100 single-node lookups | 1,000 nodes | 26.3167 seconds total |

### Timeout Tests

| Workload | Dataset | Result |
|---|---:|---|
| Graph creation | 5,000 nodes | TIMEOUT |
| Graph creation | 10,000 nodes | TIMEOUT |

## Observations

The 1,000-node workload completed successfully for graph creation,
node lookup, and 5-hop traversal.

The 5,000-node and 10,000-node graph creation workloads exceeded the
database execution deadline in the tested environment.

The repeated lookup workload completed all 100 queries successfully,
with an average query time of approximately 0.263 seconds.

## Interpretation

These results show that the tested CognoDB Cloud configuration handled
the 1,000-node workload successfully but encountered execution timeouts
when creating larger graphs.

The timeout results are reported as observed and are not treated as
proof that CognoDB cannot support larger datasets. The results may
depend on the database tier, workload design, query implementation,
network conditions, and execution limits.

## Reproducibility

The benchmark scripts used to generate these results are available in
the `benchmarks` directory.

Raw benchmark measurements are stored in:

```text
results/benchmark_results.csv