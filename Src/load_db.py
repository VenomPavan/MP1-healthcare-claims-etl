import sqlite3

def load_db(df):

    conn = sqlite3.connect("../healthcare.db")

    df.to_sql(
        "claims",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Data loaded into SQLite")