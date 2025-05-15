import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()
# Fetching the data
def fetch_all_synonyms():
    try:
        # Use directly without extra escaping
        server = os.getenv("SQL_SERVER")
        database = os.getenv("SQL_DB")
        username = os.getenv("SQL_USER")
        password = os.getenv("SQL_PASSWORD")

        print("🔍 Connecting to:", server, database, username)

        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password}'
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM synonyms")
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return results

    except Exception as e:
        return {"error": str(e)}
