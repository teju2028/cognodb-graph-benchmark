import os
import csv
import time
from datetime import datetime

from dotenv import load_dotenv
from neo4j import GraphDatabase

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


def prepare_data(session):
    print("Preparing 1,000 nodes...")

    session.run(
        "MATCH (n:BenchmarkNode) DETACH DELETE n"
    ).consume()

    session.run(
        """
        UNWIND range(1, 1000) AS id
        CREATE (:BenchmarkNode {id: id})
        """
    ).consume()

    print("Data ready.")


def single_node_lookup(session, node_id):
    start = time.perf_counter()

    result = session.run(
        """
        MATCH (n:BenchmarkNode {id: $node_id})
        RETURN n.id AS id
        """,
        node_id=node_id
    ).single()

    elapsed = time.perf_counter() - start

    if result is not None:
        return elapsed, 1

    return elapsed, 0


def main():
    try:
        driver.verify_connectivity()
        print("Connected to CognoDB")

        with driver.session() as session:

            prepare_data(session)

            number_of_queries = 100

            print(
                f"\nRunning {number_of_queries} single-node lookups..."
            )

            total_time = 0
            successful_queries = 0

            for i in range(number_of_queries):

                node_id = (i % 1000) + 1

                elapsed, result_count = single_node_lookup(
                    session,
                    node_id
                )

                total_time += elapsed
                successful_queries += result_count

            average_time = total_time / number_of_queries

            print(
                f"Completed {number_of_queries} queries"
            )

            print(
                f"Successful lookups: {successful_queries}"
            )

            print(
                f"Total time: {total_time:.4f} seconds"
            )

            print(
                f"Average query time: {average_time:.6f} seconds"
            )

            save_result(
                "100_single_node_lookups",
                1000,
                total_time,
                successful_queries,
                "SUCCESS"
            )

    finally:
        driver.close()


if __name__ == "__main__":
    main()