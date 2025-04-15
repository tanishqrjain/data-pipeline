from pymongo import MongoClient

def setup_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["linq_db"]

    # Only create the collection if it doesn't exist
    if "metrics" not in db.list_collection_names():
        db.create_collection("metrics")
        print("Collection 'metrics' created.")
    else:
        print("Collection 'metrics' already exists. Skipping creation.")

if __name__ == "__main__":
    setup_database()
