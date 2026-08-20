# CognoDB Cloud Graph Database Benchmark

## Overview

This project benchmarks CognoDB Cloud using reproducible graph database
workloads.

The goal is to measure graph creation, node lookup, and graph traversal
performance at different dataset sizes.

## Environment

- Database: CognoDB Cloud
- Driver: Neo4j Python Driver
- Language: Python
- Operating System: Windows
- Dataset sizes: 1,000, 5,000 and 10,000 nodes

## Benchmark Workloads

### 1. Graph Creation

Creates `BenchmarkNode` nodes and connects consecutive nodes using
`NEXT` relationships.

Example:

```text
Node 1 -> Node 2 -> Node 3 -> ... -> Node N
