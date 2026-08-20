import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")


def test_connection():
    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD)
    )

    try:
        driver.verify_connectivity()
        print("✅ Successfully connected to CognoDB!")

    except Exception as e:
        print("❌ Connection failed:")
        print(e)

    finally:
        driver.close()


if __name__ == "__main__":
    test_connection()