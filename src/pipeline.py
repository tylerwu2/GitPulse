import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from src.github import get_pull_requests, get_repository
from src.load import load_pull_request_data, load_repository
from src.transform import transform_pull_request_data, transform_repository_data

load_dotenv()

def run():
    raw_repo_data = get_repository("facebook", "react")
    repo_data = transform_repository_data(raw_repo_data)
    repo_id = repo_data["id"]

    pull_data = get_pull_requests("facebook", "react")
    pr_data = transform_pull_request_data(pull_data, repo_id)

    database_url = os.environ["DATABASE_URL"]
    engine = create_engine(database_url)

    with engine.begin() as conn:
        load_repository(conn, repo_data)
        
        # load data to database
        load_pull_request_data(conn, pr_data)

if __name__ == "__main__":
    run()
