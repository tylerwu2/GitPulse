def transform_repository_data(repo_data):
    return {
        "id": repo_data["id"],
        "owner": repo_data["owner"]["login"],
        "name": repo_data["name"],
        "url": repo_data["html_url"],
    }


def transform_pull_request_data(pull_data, repo_id):
    transformed = []

    for pr in pull_data:
        transformed.append(
            {
                "id": pr["id"],
                "repository_id": repo_id,
                "number": pr["number"],
                "title": pr["title"],
                "author": pr["user"]["login"],
                "state": pr["state"],
                "created_at": pr["created_at"],
                "updated_at": pr["updated_at"],
                "closed_at": pr["closed_at"],
                "merged_at": pr["merged_at"],
            }
        )

    return transformed