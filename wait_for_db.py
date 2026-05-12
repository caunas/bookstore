import time
import psycopg2
import os

DB_NAME = os.getenv("SQL_DATABASE")
DB_USER = os.getenv("SQL_USER")
DB_PASSWORD = os.getenv("SQL_PASSWORD")
DB_HOST = os.getenv("SQL_HOST")
DB_PORT = os.getenv("SQL_PORT")

while True:
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        conn.close()
        print("Banco pronto!")
        break
    except psycopg2.OperationalError:
        print("Aguardando banco...")
        time.sleep(2)

