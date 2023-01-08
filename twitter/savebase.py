import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# ucbot
intents = discord.Intents.all()

client = commands.Bot(command_prefix='~', intents=intents)

@client.event
async def on_ready():
    print('gamer time')

    cred = credentials.Certificate("admin.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # def getAll(collection):
    #     docs = db.collection(collection).stream()
    #     for doc in docs:
    #         doc.reference.to_dict()

    # save firebase collection as dictionary
    def getAll(collection):
        docs = db.collection(collection).stream()
        a = {}
        for doc in docs:
            a[doc.id] = doc.to_dict()
        return a
    ucbr = getAll('ucbr')
    ucbr_p = getAll('ucbr_p')
    rr = getAll('rr')
    rr_p = getAll('rr_p')
    msgs = {
        'ucbr': ucbr,
        'ucbr_p': ucbr_p,
        'rr': rr,
        'rr_p': rr_p
    }
    # save dictionary as json file
    with open('msgs.json', 'w') as f:
        json.dump(msgs, f)

    print("Success!")


client.run(os.getenv('UCBOT'))
