from ingest import fetch_data
from transform import transform_data, convert_to_df
from load import load_data

API_URL = "..."

def run():
    raw_data = fetch_data(API_URL)
    records = transform_data(raw_data)
    df = convert_to_df(records)
    # load data to database
    load_data(df)

if __name__ == "__main__":
    run()