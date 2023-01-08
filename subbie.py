import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# subbiebot
intents = discord.Intents.all()

client = commands.Bot(command_prefix='~', intents=intents)

# 271845683840024586
@client.event
async def on_ready():
    print('bls')

@client.event
async def on_message(message):
    print(message.author.nick)
    print(message.author.id)
    if message.author.id == 271845683840024586:
        if(random.randint(0,9)==1):
            await message.channel.send('SIMP')



client.run(os.getenv('SUBBIE'))
