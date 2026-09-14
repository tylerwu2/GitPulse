CREATE TABLE IF NOT EXISTS pull_requests (
    id BIGINT PRIMARY KEY,
    number INTEGER NOT NULL,
    title TEXT,
    author TEXT,
    state TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    closed_at TIMESTAMP,
    merged_at TIMESTAMP
);