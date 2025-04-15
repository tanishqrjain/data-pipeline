def transform_data(data):
    # Example transformation: Round timestamp to nearest hour
    for d in data:
        ts = d["timestamp"]
        d["timestamp"] = ts.replace(minute=0, second=0, microsecond=0)
    return data
