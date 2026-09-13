from sqlalchemy import create_engine


def load_data(df, database_url, table_name):
    engine = create_engine(database_url)

    df.to_sql(table_name, engine, if_exists="append", index=False)


def load_pull_request_data(df, database_url, table_name):
    engine = create_engine(database_url)
    df.to_sql(table_name, engine, if_exists="append", index=False)
