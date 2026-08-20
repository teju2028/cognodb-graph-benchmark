# Benchmark Comparison Targets

This project benchmarks CognoDB Cloud using reproducible graph database workloads.

## Primary comparison platforms

The comparison will consider:

- CognoDB Cloud
- Neo4j Aura
- Amazon Neptune
- Memgraph Cloud

## Metrics

The benchmark focuses on:

1. Graph creation time
2. Node lookup latency
3. Multi-hop traversal latency
4. Behavior as dataset size increases
5. Timeout/failure behavior

## Methodology

All platforms should use:

- The same dataset structure
- The same node properties
- The same relationship structure
- The same Cypher queries where supported
- The same dataset sizes
- The same number of repeated queries

Results should be recorded without changing or hiding unsuccessful runs.