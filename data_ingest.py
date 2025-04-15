import random
from datetime import datetime, timedelta
from pymongo import MongoClient
from transformations import transform_data

CATEGORIES = ["sales", "marketing", "engineering"]

def generate_data(num=50):
    base_time = datetime.now()
    data = []
    for _ in range(num):
        entry = {
            "category": random.choice(CATEGORIES),
            "value": round(random.uniform(100, 500), 2),
            "timestamp": base_time - timedelta(minutes=random.randint(0, 1000))
        }
        data.append(entry)
    return data

def insert_data(data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["linq_db"]
    db.metrics.insert_many(data)
    print(f"{len(data)} records inserted.")

if __name__ == "__main__":
    raw_data = generate_data()
    clean_data = transform_data(raw_data)
    insert_data(clean_data)
