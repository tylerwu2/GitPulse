from github import get_pull_requests
from load import load_pull_request_data
from transform import convert_to_df, transform_pull_request_data


def run():
    pull_data = get_pull_requests("facebook", "react")
    records = transform_pull_request_data(pull_data)
    df = convert_to_df(records)
    # load data to database
    load_pull_request_data(df)

if __name__ == "__main__":
    run()
