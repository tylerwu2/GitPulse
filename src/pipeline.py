from ingest import fetch_data
from transform import transform_data, convert_to_df, transform_pull_request_data
from load import load_data, load_pull_request_data
from github import get_pull_requests


def run():
    pull_data = get_pull_requests("facebook", "react")
    records = transform_pull_request_data(pull_data)
    df = convert_to_df(records)
    # load data to database
    load_

if __name__ == "__main__":
    run()