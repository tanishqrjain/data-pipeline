import plotly.express as px
import pandas as pd
from pymongo import MongoClient

def fetch_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["linq_db"]
    data = list(db.metrics.find({}, {"_id": 0}))
    return pd.DataFrame(data)

def create_chart(df):
    df_grouped = df.groupby("category")["value"].sum().reset_index()
    fig = px.bar(df_grouped, x="category", y="value", title="Total Value by Category")
    fig.write_image("dashboard.png")  # save screenshot
    fig.show()

if __name__ == "__main__":
    df = fetch_data()
    create_chart(df)
