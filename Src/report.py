import sqlite3
import pandas as pd

conn = sqlite3.connect("../healthcare.db")

query = """
SELECT
    provider_id,
    SUM(claim_amount) AS total_claims
FROM claims
GROUP BY provider_id
ORDER BY total_claims DESC
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()