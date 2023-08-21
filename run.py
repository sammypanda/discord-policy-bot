# functionality
import os
import database
from models import test

# discord
import discord
from discord.ext import commands

# variables
from dotenv import load_dotenv

load_dotenv()

# TODO: run checks to see if important env variables are set/set defaults

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# novice implementation of cogs
class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.slash_command(name="objects", description="output items to interact with")
    async def sample(self, ctx, section=""):
        if (section == "" or section == "ctx"):
            await ctx.respond(f"ctx objects: {dir(ctx)}") # using ctx.send will cause 'application did not respond'
        else:
            await ctx.respond(f"object not found")

    @commands.slash_command(name="setup", description="creates the setup channel")
    async def setup_channel(self, ctx):
        print(ctx.new)

@bot.event
async def on_ready():
    if int(os.getenv('DEBUG_LEVEL')) >= 1:
        print("debug: on_ready() ran")
        # print(database.test_query())
        print(test.test_query())
    
bot.add_cog(Cogs(bot))
bot.run(os.getenv('BOT_TOKEN'))