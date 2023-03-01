# variables
from dotenv import load_dotenv

import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
def cursor():
    return cur