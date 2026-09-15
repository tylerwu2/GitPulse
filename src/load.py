from sqlalchemy import text


def load_pull_request_data(conn, data):
    conn.execute(
        text("""
            INSERT INTO pull_requests (id, repository_id, number, title, author, state, created_at, updated_at, closed_at, merged_at)
            VALUES (:id, :repository_id, :number, :title, :author, :state, :created_at, :updated_at, :closed_at, :merged_at)
            ON CONFLICT (id)
            DO UPDATE SET
                title = EXCLUDED.title,
                state = EXCLUDED.state,
                updated_at = EXCLUDED.updated_at,
                closed_at = EXCLUDED.closed_at,
                merged_at = EXCLUDED.merged_at
        """),
        data,
    )

def load_repository(conn, repo_id):
    conn.execute(
        text("""
            INSERT INTO repositories (id, owner, name, url)
            VALUES (:id, :owner, :name, :url)
            ON CONFLICT (id)
            DO UPDATE SET
                owner = EXCLUDED.owner,
                name = EXCLUDED.name,
                url = EXCLUDED.url
            """),
            repo_id
    )

def load_reviews():
    return None

def load_commits():
    return None