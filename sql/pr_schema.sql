CREATE TABLE IF NOT EXISTS repositories (
    id BIGINT PRIMARY KEY,
    owner TEXT NOT NULL,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    UNIQUE(owner, name)
)

CREATE TABLE IF NOT EXISTS pull_requests (
    id BIGINT PRIMARY KEY,
    repository_id BIGINT NOT NULL REFERENCES repositories(id),
    number INTEGER NOT NULL,
    title TEXT,
    author TEXT,
    state TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    closed_at TIMESTAMP,
    merged_at TIMESTAMP
    UNIQUE(repository_id, number)
);