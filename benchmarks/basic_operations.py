import os
import csv
import time
from datetime import datetime

from dotenv import load_dotenv
from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError

load_dotenv()

URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

RESULT_FILE = "results/benchmark_results.csv"


def save_result(operation, dataset_size, elapsed, result_count, status):
    file_exists = os.path.exists(RESULT_FILE)

    with open(RESULT_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(RESULT_FILE) == 0:
            writer.writerow([
                "timestamp",
                "operation",
                "dataset_size",
                "time_seconds",
                "result_count",
                "status"
            ])

        writer.writerow([
            datetime.now().isoformat(),
            operation,
            dataset_size,
            round(elapsed, 4),
            result_count,
            status
        ])


def create_graph(session, count):
    # Delete previous benchmark graph
    session.run(
        "MATCH (n:BenchmarkNode) DETACH DELETE n"
    ).consume()

    start = time.perf_counter()

    # Create nodes
    session.run(
        """
        UNWIND range(1, $count) AS id
        CREATE (:BenchmarkNode {id: id})
        """,
        count=count
    ).consume()

    # Create relationships
    session.run(
        """
        MATCH (a:BenchmarkNode)
        MATCH (b:BenchmarkNode {id: a.id + 1})
        WHERE a.id < $count
        CREATE (a)-[:NEXT]->(b)
        """,
        count=count
    ).consume()

    return time.perf_counter() - start


def lookup_nodes(session, count):
    start = time.perf_counter()

    result = session.run(
        """
        MATCH (n:BenchmarkNode)
        WHERE n.id <= $count
        RETURN count(n) AS total
        """,
        count=count
    ).single()

    elapsed = time.perf_counter() - start

    return elapsed, result["total"]


def traverse_graph(session, start_id, hops):
    start = time.perf_counter()

    query = f"""
        MATCH (start:BenchmarkNode {{id: $start_id}})
        MATCH path = (start)-[:NEXT*1..{hops}]->(target)
        RETURN count(path) AS paths
    """

    result = session.run(
        query,
        start_id=start_id
    ).single()

    elapsed = time.perf_counter() - start

    return elapsed, result["paths"]


def main():
    try:
        driver.verify_connectivity()
        print("Connected to CognoDB")

        with driver.session() as session:

            dataset_sizes = [1000, 5000, 10000]

            for dataset_size in dataset_sizes:

                print(f"\n--- Testing {dataset_size} nodes ---")

                # -------------------------
                # CREATE GRAPH TEST
                # -------------------------
                try:
                    create_time = create_graph(
                        session,
                        dataset_size
                    )

                    print(
                        f"Created graph with {dataset_size} nodes "
                        f"in {create_time:.4f} seconds"
                    )

                    save_result(
                        "create_graph",
                        dataset_size,
                        create_time,
                        dataset_size,
                        "SUCCESS"
                    )

                except Neo4jError as e:

                    print(
                        f"Create test FAILED for {dataset_size} nodes"
                    )
                    print(str(e))

                    save_result(
                        "create_graph",
                        dataset_size,
                        0,
                        0,
                        "TIMEOUT"
                    )

                    # Skip lookup and traversal
                    # because the graph was not created
                    continue

                # -------------------------
                # LOOKUP TEST
                # -------------------------
                try:
                    lookup_time, lookup_count = lookup_nodes(
                        session,
                        dataset_size
                    )

                    print(
                        f"Looked up {lookup_count} nodes "
                        f"in {lookup_time:.4f} seconds"
                    )

                    save_result(
                        "lookup_nodes",
                        dataset_size,
                        lookup_time,
                        lookup_count,
                        "SUCCESS"
                    )

                except Neo4jError as e:

                    print(
                        f"Lookup test FAILED for {dataset_size} nodes"
                    )
                    print(str(e))

                    save_result(
                        "lookup_nodes",
                        dataset_size,
                        0,
                        0,
                        "FAILED"
                    )

                # -------------------------
                # 5-HOP TRAVERSAL TEST
                # -------------------------
                try:
                    traversal_time, paths = traverse_graph(
                        session,
                        1,
                        5
                    )

                    print(
                        f"5-hop traversal found {paths} paths "
                        f"in {traversal_time:.4f} seconds"
                    )

                    save_result(
                        "5_hop_traversal",
                        dataset_size,
                        traversal_time,
                        paths,
                        "SUCCESS"
                    )

                except Neo4jError as e:

                    print(
                        f"Traversal test FAILED for {dataset_size} nodes"
                    )
                    print(str(e))

                    save_result(
                        "5_hop_traversal",
                        dataset_size,
                        0,
                        0,
                        "FAILED"
                    )

    finally:
        driver.close()


if __name__ == "__main__":
    main()