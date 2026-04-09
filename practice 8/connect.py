import psycopg2
from config import DB_CONFIG

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_CONFIG["dbname"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"]
        )
        print("Connected to PostgreSQL server")
        return conn

    except Exception as error:
        print("Connection error:", error)
