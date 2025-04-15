# Datastore Choice: MongoDB

I chose MongoDB because:
### 📦 1. Schema-less Flexibility
- This task requires inserting **mock data** with fields like `category`, `value`, and `timestamp`.
- MongoDB's flexible document model makes it easy to ingest varying structures without schema migrations or setup overhead.

### ⚡ 2. Fast Prototyping for Small Data Projects
- This is a short, iterative project focused on speed and simplicity.
- MongoDB allows quick setup without worrying about table design, data types, or constraints — ideal for short-cycle development like this assessment.

### 📊 3. Great for Time-Series & Aggregations
- This task involves generating time-based data (`timestamp`) and grouping it by `category` for insights.
- MongoDB is well-suited for **time-series data**, and its aggregation framework can be used to support real-time dashboards in extended versions.

Setup is handled by `datastore_setup.py`, which initializes the database and collection.
