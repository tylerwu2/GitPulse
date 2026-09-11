import pandas as pd

def transform_data(raw_data):
    records = []

    for item in raw_data["features"]:
        properties = item["properties"]

        records.append({
            "id": item["id",]
        })

    return records

def convert_to_df(data):
    return pd.DataFrame(data)