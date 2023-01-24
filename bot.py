import asyncio
import discord
import os
import time
import random
from discord.ui import Button
from discord.ui import Select
from discord.ext import tasks
import ast
import os
from dotenv import load_dotenv






client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    



@client.event
async def on_message(message):
    msg = message.content
    if message.author.bot:
      return

load_dotenv()
token = os.getenv("token")
client.run(token)