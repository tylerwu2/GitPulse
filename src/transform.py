import pandas as pd

def transform_data(raw_data):
    records = []

    for item in raw_data["features"]:
        properties = item["properties"]

        records.append({
            "id": item["id",]
        })

    return records

def transform_pull_request_data(pull_data):
    transformed = []

    for pr in pull_data:
        transformed.append({
            "id" : pr["id"],
            "number" : pr["number"],
            "title": pr["title"],
            "author": pr["user"]["login"],
            "state": pr["state"],
            "created_at": pr["created_at"],
            "updated_at": pr["updated_at"],
            "closed_at": pr["closed_at"],
            "merged_at": pr["merged_at"],
        })

    return transformed

def convert_to_df(data):
    return pd.DataFrame(data)