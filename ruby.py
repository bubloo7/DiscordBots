import discord
from discord.ext import commands
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# rubot
intents = discord.Intents.all()

client = commands.Bot(command_prefix='~', intents=intents)
@client.event
async def on_ready():
    print('bls')

@client.event
async def on_message(message):

    # short react
    short = message.content
    whitespace2 =''
    for x in short:
        if x != ' ':
            whitespace2 = whitespace2 + x
    whitespace2 = whitespace2.lower()
    for i in range(len(whitespace2)-4):

        if whitespace2[i:i+5] == "short":
            await message.channel.send('i hate u')
            whitespace2 = ''
            break
    print('test')
    for i in range(len(whitespace2)-4):

        if whitespace2[i:i+5] == "small":
            await message.channel.send('i hate u')
            whitespace2 = ''
            break
    for i in range(len(whitespace2)-3):

        if whitespace2[i:i+4] == "smol":
            await message.channel.send('i hate u')
            whitespace2 = ''
            break
    for i in range(len(whitespace2)-3):

        if whitespace2[i:i+4] == "tiny":
            await message.channel.send('i hate u')
            whitespace2 = ''
            break
    for i in range(len(whitespace2)-2):

        if whitespace2[i:i+3] == "lil":
            await message.channel.send('i hate u')
            whitespace2 = ''
            break

    for i in range(len(whitespace2)-7):
 
        if whitespace2[i:i+8] == "rubysize":
            await message.channel.send('i hate u')
            whitespace2 = ''
            break
    for i in range(len(whitespace2)-3):

        if whitespace2[i:i+4] == "mini":
            await message.channel.send('i hate u')
            whitespace2 = ''
            break
    for i in range(len(whitespace2)-5):
   
        if whitespace2[i:i+6] == "little":
            await message.channel.send('i hate u')
            whitespace2 = ''
            break
            
client.run(os.getenv('RUBY'))


