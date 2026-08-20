# Managed Graph Database Comparison

## Purpose

This document defines the methodology used to compare CognoDB Cloud
with other managed graph database platforms.

The comparison will focus on:

- Graph creation
- Node lookup
- Multi-hop graph traversal
- Query latency
- Dataset scaling
- Ease of setup
- Pricing and available free tiers

## Candidate Platforms

The initial comparison targets are:

1. CognoDB Cloud
2. Neo4j Aura
3. Amazon Neptune
4. Memgraph Cloud

## Benchmark Workloads

The same logical workloads will be used wherever supported:

### Workload 1 — Graph Creation

Create a chain of graph nodes:

```text
Node 1 -> Node 2 -> Node 3 -> ... -> Node N