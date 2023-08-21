# imports
import os
import discord
from discord.ext import commands
from models.manager_model import ManagerModel
from controllers.manager_controller import ManagerController
from dotenv import load_dotenv

load_dotenv() # import dotenv values

# TODO: run checks to see if important env variables are set/set defaults

intents = discord.Intents.all() # declare that the bot can do anything it wants!

bot = commands.Bot(command_prefix='!', intents=intents) # bot instantiate/config

_console_manager = ManagerModel() # instantiate a private manager_model just for console/server admin

# Setup 
manager = ManagerController(bot)

@bot.event
async def on_ready():
    if int(os.getenv('DEBUG_LEVEL')) >= 1:
        print("debug: on_ready() ran")
        print(_console_manager.test_query())

bot.run(os.getenv('BOT_TOKEN'))