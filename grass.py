from discord.ext import commands
import discord
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# grassbot

intents = discord.Intents.all()
client = commands.Bot(command_prefix='~', intents= intents)


@client.event
async def on_ready():
    print('bls')


@client.event
async def on_message(message):
    e = message.content
    if '2' in e.split():
        await message.channel.send('https://tenor.com/view/peggle-peggle2-two-e3-meme-gif-15554864')


client.run(os.getenv('GRASS'))
