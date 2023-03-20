# variables
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

# Connect to your postgres DB
conn = psycopg2.connect(
    host=os.getenv('DB_HOST'),
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
def cursor():
    return cur
