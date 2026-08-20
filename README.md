## Current CognoDB Results

The benchmark was executed against CognoDB Cloud using the workload
scripts included in this repository.

| Workload | Dataset Size | Time | Result |
|---|---:|---:|---|
| Graph creation | 1,000 nodes | 6.5196 s | SUCCESS |
| Node lookup | 1,000 nodes | 0.2729 s | SUCCESS |
| 5-hop traversal | 1,000 nodes | 0.2667 s | SUCCESS |
| Graph creation | 5,000 nodes | TIMEOUT | FAILED |
| Graph creation | 10,000 nodes | TIMEOUT | FAILED |
| 100 single-node lookups | 1,000 nodes | 26.3167 s total | SUCCESS |

### Observations

- The 1,000-node graph creation test completed successfully.
- Node lookup completed successfully for 1,000 nodes.
- The 5-hop traversal completed successfully for 1,000 nodes.
- Graph creation at 5,000 nodes exceeded the database execution deadline.
- Graph creation at 10,000 nodes also exceeded the database execution deadline.
- All 100 single-node lookup queries completed successfully.
- Failed and timed-out tests are retained in the results CSV.

These results represent the specific CognoDB Cloud configuration and
workloads tested in this experiment. They should not be interpreted as
universal performance characteristics.
