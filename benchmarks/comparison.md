# Managed Graph Database Comparison

This document compares CognoDB Cloud with other managed graph database
platforms using publicly available information.

## Comparison Method

The comparison focuses on:

- Graph database model
- Query language
- Cloud availability
- Managed-service model
- Scalability
- Developer tooling
- Pricing approach
- Benchmark reproducibility

Performance numbers for other platforms are not invented. Where an
equivalent benchmark has not been executed, the result is marked as
"Not measured".

## Platforms

| Platform | Graph Model | Query Language | Managed Cloud |
|---|---|---|---|
| CognoDB Cloud | Property graph | Cypher | Yes |
| Neo4j Aura | Property graph | Cypher | Yes |
| Amazon Neptune | Property graph / RDF | Gremlin / openCypher / SPARQL | Yes |
| Memgraph Cloud | Property graph | Cypher | Yes |

## CognoDB Cloud

CognoDB Cloud is the primary system tested in this benchmark.

The benchmark measured:

- Graph creation
- Node lookup
- 5-hop graph traversal
- Repeated single-node lookups

The tested 1,000-node workload completed successfully.

The 5,000-node and 10,000-node graph creation workloads experienced
execution timeouts in the tested environment.

See `results/benchmark_results.csv` for the raw measurements.

## Neo4j Aura

Neo4j Aura is Neo4j's managed cloud database service.

Neo4j uses the Cypher query language for property-graph workloads.

No Neo4j Aura performance numbers are reported in this repository because
an equivalent benchmark was not executed against Neo4j Aura.

## Amazon Neptune

Amazon Neptune is a managed graph database service from AWS.

Neptune supports graph workloads including property graphs and RDF.

No Amazon Neptune performance numbers are reported in this repository
because an equivalent benchmark was not executed against Neptune.

## Memgraph Cloud

Memgraph is a graph database platform using a property graph model and
Cypher-compatible querying.

No Memgraph Cloud performance numbers are reported in this repository
because an equivalent benchmark was not executed against Memgraph Cloud.

## Performance Results

Only directly measured CognoDB results are included.

| Workload | Dataset | CognoDB Result |
|---|---:|---:|
| Graph creation | 1,000 nodes | 6.5196 s |
| Node lookup | 1,000 nodes | 0.2729 s |
| 5-hop traversal | 1,000 nodes | 0.2667 s |
| 100 single-node lookups | 1,000 nodes | 26.3167 s total |
| Graph creation | 5,000 nodes | Timeout |
| Graph creation | 10,000 nodes | Timeout |

## Limitations

These results represent one test environment and one workload design.

The results should not be interpreted as proof that CognoDB is faster or
slower than the comparison platforms.

A fair cross-platform performance comparison requires running the same
workload with equivalent hardware, dataset, configuration, network
conditions, and measurement methodology on every platform.

## Conclusion

CognoDB successfully completed the tested 1,000-node graph workloads,
while the larger graph-creation tests encountered execution timeouts.

The comparison with other managed graph databases is currently
feature-oriented rather than a direct performance ranking because
equivalent tests have not yet been executed on the other platforms.