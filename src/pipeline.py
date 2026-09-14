import os

from github import get_pull_requests
from load import load_pull_request_data, load_repository
from transform import transform_pull_request_data
from sqlalchemy import create_engine

def run():
    pull_data = get_pull_requests("facebook", "react")
    pr_data = transform_pull_request_data(pull_data)
    repo_id = pr_data[0]["repository_id"]

    engine = create_engine(os.environdatabase_url)

    with engine.begin() as conn:
        load_repository(conn, repo_id)
        
        # load data to database
        load_pull_request_data(conn, pr_data)

if __name__ == "__main__":
    run()
