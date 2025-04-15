# Data Ingestion

## What It Does
- Generates 50 mock data entries with fields:
  - `category`: e.g., sales, marketing
  - `value`: random float
  - `timestamp`: a recent time within the last ~17 hours
- Applies a transformation to **round timestamps to the nearest hour**
  - This helps in time-series analysis and cleaner visual grouping
- Inserts the cleaned data into MongoDB

## How to Run
```bash
python3 data_ingest.py
