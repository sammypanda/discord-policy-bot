import database

cur = database.cursor()

def test_query():
    cur.execute("SELECT * FROM guilds")

    # Retrieve query results
    records = cur.fetchall()

    return records