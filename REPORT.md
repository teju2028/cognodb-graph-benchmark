# CognoDB Cloud Benchmark Report

## 1. Executive Summary

This project evaluates CognoDB Cloud using reproducible graph database
workloads.

The benchmark measured graph creation, node lookup, 5-hop graph traversal,
and repeated single-node lookups.

The 1,000-node workload completed successfully. Larger graph-creation
workloads of 5,000 and 10,000 nodes reached the execution deadline in the
tested environment.

These results should be interpreted as measurements from the tested
environment and workload, not as a general limitation of CognoDB Cloud.

## 2. Test Environment

- Database: CognoDB Cloud
- Driver: Neo4j Python Driver
- Language: Python
- Operating System: Windows
- Dataset sizes tested: 1,000, 5,000 and 10,000 nodes

## 3. Workloads

### Graph Creation

Creates `BenchmarkNode` nodes and connects consecutive nodes using
`NEXT` relationships.

### Node Lookup

Queries benchmark nodes and counts the matching records.

### 5-Hop Traversal

Traverses `NEXT` relationships from a starting node for up to five hops.

### Repeated Single-Node Lookup

Executes 100 individual node lookup queries and records the total and
average query time.

## 4. Results

| Workload | Dataset | Result |
|---|---:|---:|
| Graph creation | 1,000 | 6.5196 s |
| Node lookup | 1,000 | 0.2729 s |
| 5-hop traversal | 1,000 | 0.2667 s |
| 100 single-node lookups | 1,000 | 26.3167 s total |
| Graph creation | 5,000 | TIMEOUT |
| Graph creation | 10,000 | TIMEOUT |

## 5. Observations

The 1,000-node graph was created successfully and the lookup and traversal
operations also completed successfully.

The 5,000-node and 10,000-node graph creation workloads exceeded the
execution deadline in the tested environment.

The 100-query lookup workload completed all 100 queries successfully,
with an average query time of approximately 0.263 seconds.

## 6. Comparison

The repository includes a feature-oriented comparison with:

- Neo4j Aura
- Amazon Neptune
- Memgraph Cloud

No performance numbers are reported for these platforms because the
same benchmark was not executed against them.

This avoids presenting unsupported or fabricated performance claims.

## 7. Limitations

The results depend on the selected database configuration, network,
workload design, query implementation, and execution limits.

A fair cross-platform performance comparison requires running the same
workload under equivalent conditions on each platform.

The timeout results therefore indicate what happened in this test rather
than proving that larger datasets cannot be handled.

## 8. Reproducibility

Benchmark source code is available in:

```text
benchmarks/