# script to connect to GitHub API client

import requests


def get_repository(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_pull_requests(owner, repo, page=1):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

    params = {"state": "all", "per_page": 100, "page": page}

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data

def get_all_pull_requests(owner, repo):
    page = 1
    all_pull_requests = []

    while True:
        data = get_pull_requests(owner, repo)
        if not data:
            break
        all_pull_requests.extend(data)
        page += 1
    return all_pull_requests
