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

### 3.1 Graph Creation

Creates `BenchmarkNode` nodes and connects consecutive nodes using
`NEXT` relationships.

Example:

```text
Node 1 -> Node 2 -> Node 3 -> ... -> Node N
