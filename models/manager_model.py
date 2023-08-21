import database

class ManagerModel:
    def __init__(self):
        self.cur = database.cursor()

    def test_query(self): # Just outputs all in guilds table
        self.cur.execute("SELECT * FROM guilds")

        # Retrieve query results
        records = self.cur.fetchall()

        return records