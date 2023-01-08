import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# ucbot
intents = discord.Intents.all()

client = commands.Bot(command_prefix='~', intents=intents)

@client.event
async def on_ready():
    print('gamer time')

    async def flatten(hist):
        a = []
        async for i in hist:
            a.append(i)
        return a
    cred = credentials.Certificate("admin.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    def removeAll(collection):
        docs = db.collection(collection).stream()
        for doc in docs:
            doc.reference.delete()
    removeAll("rr")
    print("rr removed")
    removeAll("ucbr")
    print("ucbr removed")
    removeAll("rr_p")
    print("rr_p removed")
    removeAll("ucbr_p")
    print("ucbr_p removed")

    ucbr_channel = discord.Client.get_channel(client, 615077001115598872)
    ucbr_msgs = await flatten(ucbr_channel.history(limit=None))

    for msg in ucbr_msgs:

        db.collection("ucbr").document(str(msg.id)).set({
            "msg": msg.content,
            "img": msg.attachments[0].url if len(msg.attachments) > 0 else ""
        })
    print('ucbr uploaded')


    ucbr_channel = discord.Client.get_channel(client, 745719332444831825)
    ucbr_msgs = await flatten(ucbr_channel.history(limit=None))

    for msg in ucbr_msgs:

        db.collection("ucbr_p").document(str(msg.id)).set({
            "msg": msg.content,
            "img": msg.attachments[0].url if len(msg.attachments) > 0 else ""
        })
    print('ucbr_p uploaded')


    rr_channel = discord.Client.get_channel(client, 681386070948315213)
    rr_msgs = await flatten(rr_channel.history(limit=None))
    for msg in rr_msgs:
        # if msg.attachments == []:
        #     continue
        db.collection("rr").document(str(msg.id)).set({
            "msg": msg.content,
            "img": msg.attachments[0].url if len(msg.attachments) > 0 else ""
        })
    print('rr uploaded')

    rr_channel = discord.Client.get_channel(client, 745724886281879632)
    rr_msgs = await flatten(rr_channel.history(limit=None))
    
    for msg in rr_msgs:
        # if msg.attachments == []:
        #     continue
        db.collection("rr_p").document(str(msg.id)).set({
            "msg": msg.content,
            "img": msg.attachments[0].url if len(msg.attachments) > 0 else ""
        })
    print('rr_p uploaded')

    print("Success!")


client.run(os.getenv('UCBOT'))
