from dotenv import load_dotenv
import os

import psycopg2

# Load environment variables
load_dotenv()

dbname = os.getenv("DATABASE_NAME")
user = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")


try:
    # Connect to your postgres DB
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    print(f"Connected to database {dbname} successfully.")
except Exception as e:
    print(f"An error occurred while connecting to the database {dbname}: {e}")