from sqlalchemy import text


def load_pull_request_data(conn, data):
    
    return None

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