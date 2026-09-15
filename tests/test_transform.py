from src.transform import (
    transform_pull_request_data,
    transform_repository_data,
)


def test_transform_repository_data():
    raw_repository = {
        "id": 12345,
        "name": "react",
        "html_url": "https://github.com/facebook/react",
        "owner": {
            "login": "facebook"
        },
    }

    result = transform_repository_data(raw_repository)

    assert result == {
        "id": 12345,
        "owner": "facebook",
        "name": "react",
        "url": "https://github.com/facebook/react",
    }


def test_transform_pull_request_data():
    raw_pull_requests = [
        {
            "id": 100,
            "number": 42,
            "title": "Fix bug",
            "user": {
                "login": "alice"
            },
            "state": "open",
            "created_at": "2026-09-01T10:00:00Z",
            "updated_at": "2026-09-02T10:00:00Z",
            "closed_at": None,
            "merged_at": None,
        }
    ]

    result = transform_pull_request_data(
        raw_pull_requests,
        repository_id=12345,
    )

    assert result == [
        {
            "id": 100,
            "repository_id": 12345,
            "number": 42,
            "title": "Fix bug",
            "author": "alice",
            "state": "open",
            "created_at": "2026-09-01T10:00:00Z",
            "updated_at": "2026-09-02T10:00:00Z",
            "closed_at": None,
            "merged_at": None,
        }
    ]


def test_transform_pull_request_data_empty():
    result = transform_pull_request_data(
        [],
        repository_id=12345,
    )

    assert result == []