# functionality
import os

# discord
import discord

# variables
from dotenv import load_dotenv

load_dotenv()

class bot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

intents = discord.Intents.default()
intents.message_content = True

client = bot(intents=intents)
client.run(os.getenv('BOT_TOKEN'))