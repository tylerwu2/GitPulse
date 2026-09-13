from src.transform import convert_to_df, transform_pull_request_data


def test_convert_to_df():
    data = [{"id": 1, "title": "First"}, {"id": 2, "title": "Second"}]

    df = convert_to_df(data)

    assert len(df) == 2
    assert list(df.columns) == ["id", "title"]


def test_convert_to_df_empty():
    df = convert_to_df([])

    assert df.empty


def test_transform_pull_request_data():
    data = [
        {
            "id": 123,
            "number": 1,
            "title": "Fix bug",
            "state": "closed",
            "user": {"login": "bob"},
            "created_at": "2026-09-01T10:00:00Z",
            "updated_at": "2026-09-02T10:00:00Z",
            "closed_at": "2026-09-02T09:00:00Z",
            "merged_at": "2026-09-02T09:30:00Z",
        }
    ]

    transformed_data = transform_pull_request_data(data)

    assert transformed_data == [
        {
            "id": 123,
            "number": 1,
            "title": "Fix bug",
            "author": "bob",
            "state": "closed",
            "created_at": "2026-09-01T10:00:00Z",
            "updated_at": "2026-09-02T10:00:00Z",
            "closed_at": "2026-09-02T09:00:00Z",
            "merged_at": "2026-09-02T09:30:00Z",
        }
    ]
