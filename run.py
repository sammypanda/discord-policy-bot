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

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if int(os.getenv('DEBUG_LEVEL')) >=2:
            print(f'ctx: {ctx}')

        if ctx.author.bot is False:
            await ctx.author.guild.system_channel.send(f'no! i do the test {ctx.author}')

@bot.event
async def on_ready(): #wrong syntax?
    if int(os.getenv('DEBUG_LEVEL')) >= 1:
        print("debug: on_ready() ran")
        # print(database.test_query())
        print(test.test_query())
    
    await bot.add_cog(Cogs(bot))

bot.run(os.getenv('BOT_TOKEN'))