import database
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv() # import dotenv values

class ManagerModel:
    def __init__(self):
        self.cur = database.cursor()
        # TODO: run checks to see if important env variables are set/set defaults
        self.intents = discord.Intents.all() # declare that the bot can do anything it wants!
        self.bot = commands.Bot(command_prefix='!', intents=self.intents) # bot instantiate/config

    def get_bot(self):
        return self.bot

    def run_bot(self, bot):
        @bot.event
        async def on_ready():
            if int(os.getenv('DEBUG_LEVEL')) >= 1:
                print("debug: on_ready() ran")
                print(self.test_query())

        self.bot.run(os.getenv('BOT_TOKEN'))

    def test_query(self): # Just outputs all in guilds table
        self.cur.execute("SELECT * FROM guilds")

        # Retrieve query results
        records = self.cur.fetchall()

        return records