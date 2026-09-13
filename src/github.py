# script to connect to GitHub API client

import requests


def get_pull_requests(owner, repo, page=1):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

    params = {"state": "all", "per_page": 100, "page": page}

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data
