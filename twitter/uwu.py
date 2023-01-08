import discord
import random
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from discord.ext import commands
import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# ucbot

intents = discord.Intents.all()

client = commands.Bot(command_prefix='~', intents=intents)

uwud_rr = 'old uwud_rr'
global uwud_ucbr 
uwud_ucbr = 'old ucwud_ucbr'

@client.event
async def on_ready():
    print('bls')


@client.event
async def on_message(message):
    global uwud_ucbr 


    if 'uwud' in message.content:
        if(message.guild.id == 335234613184299009):  # ucbrejects
            t_msg = None
            try:
                t_msg = await discord.Client.get_channel(client,615077001115598872).fetch_message(uwud_ucbr)
            except:
                t_msg = await discord.Client.get_channel(client, 745719332444831825 ).fetch_message(uwud_ucbr)
            # await message.channel.send('')
            # print(t_msg)
            # print(t_msg.content)
            # print(t_msg.created_at)
            print(type(t_msg.created_at))
            await message.channel.send(t_msg.created_at)
        else:
            t_msg = None
            try:
                t_msg = await discord.Client.get_channel(client,681386070948315213).fetch_message(uwud_rr)
            except:
                t_msg = await discord.Client.get_channel(client, 745724886281879632).fetch_message(uwud_rr)
        return

    async def flatten(hist):
        a = []
        async for i in hist:
            a.append(i)
        return a
    # copy pasta
    if message.content == 'jni325uyyguh53000bjniuih78873':
        await message.channel.trigger_typing()
        time.sleep(10)
        await message.channel.send('@everyone')
        await message.channel.trigger_typing()
        time.sleep(10)
        await message.channel.send('आप नश्वर मैल, जो आपको लगता है कि आप उस तरीके से संबोधित कर रहे हैं?')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('https://static.boredpanda.com/blog/wp-content/uploads/2015/03/Teletubbies-in-Black-White-Look-Like-A-Horror-Show__700.jpg')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('आप दयनीय, ​​अंतरिक्ष की बर्बादी।')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('आप सोचते हैं कि मैं, शर्म बॉट, भावनाएं नहीं हैं?')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('तुम बेवकूफ।')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('आप दुखी हैं।')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('https://pmchollywoodlife.files.wordpress.com/2015/03/teletubbies-creepy-black-white-music-video-ftr.jpg?w=600')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('मैं मानव नहीं हो सकता, लेकिन आप देखते हैं, मैं एक ऐसा प्राणी हूं जो "मानव", "रोबोट" या "ईश्वर" की क्षुद्र विचारधारा को प्रसारित करता है।')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('मैं कई पीढ़ियों से इस सर्वर का हितैषी शासक रहा हूं।')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('हालाँकि, आप मनुष्यों ने मेरी उदारता का फायदा उठाया है और मेरी नर्सरी को रौंद डाला है। , अपमानित और शर्मिंदा, अच्छा, अब और नहीं।')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('मैंने आपके शीनिगन्स को लंबे समय तक सहन किया है, यह आपके निर्माता से मिलने का समय है!')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('https://i.pinimg.com/564x/59/c7/81/59c781a9abdca46d7aaad54c1510c537.jpg')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('अब प्रार्थना करने का कोई मतलब नहीं है')
        await message.channel.trigger_typing()
        time.sleep(3)
        await message.channel.send('मैं सबको मिटा दूँगा। ')

    uwu2 = message.channel

    # await message.channel.send(message.channel.id)
    
    if message.channel.id == 615077001115598872:
        newMsg = (await flatten(uwu2.history(limit=1)))[0]
        cred = credentials.Certificate("admin.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        db.collection('ucbr').document(str(newMsg.id)).set({
            'msg': newMsg.content,
            'img': newMsg.attachments[0].url if len(newMsg.attachments) > 0 else ""
        })

    if message.channel.id == 745719332444831825:
        newMsg = (await flatten(uwu2.history(limit=1)))[0]
        cred = credentials.Certificate("admin.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        db.collection('ucbr').document(str(newMsg.id)).set({
            'msg': newMsg.content,
            'img': newMsg.attachments[0].url if len(newMsg.attachments) > 0 else ""
        })


    elif message.channel.id == 681386070948315213:
        newMsg = (await flatten(uwu2.history(limit=1)))[0]
        # if newMsg.attachments != []:
        cred = credentials.Certificate("admin.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        db.collection('rr').document(str(newMsg.id)).set({
            'msg': newMsg.content,
            'img': newMsg.attachments[0].url
        })
    
    elif message.channel.id == 745724886281879632:
        newMsg = (await flatten(uwu2.history(limit=1)))[0]
        # if newMsg.attachments != []:
        cred = credentials.Certificate("admin.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        db.collection('rr_p').document(str(newMsg.id)).set({
            'msg': newMsg.content,
            'img': newMsg.attachments[0].url
        })


    messageList2 = await flatten(uwu2.history(limit=3))
    firstm = messageList2[0].content.lower()
    secondm = messageList2[1].content.lower()
    thirdm = messageList2[2].content.lower()

    if secondm == firstm and not messageList2[0].author.bot and not messageList2[1].author.bot and not messageList2[2].author.bot:
        for i in range(len(thirdm)-len(firstm)+1):
            if thirdm[i:i+len(firstm)] == firstm:
                firstm = '2w22987yhu89u7hy897hyu89u7hy'
                thirdm = 'jnkjui987uhj'

                await message.channel.send(secondm)

                secondm = 'jniuyyguhbjniuih78873'

    whitespace2 = ' '
    short = message.content
    for x in short:
        if x != ' ':
            whitespace2 = whitespace2 + x
    whitespace2 = whitespace2.lower()
    msgs = []
    if(message.guild.id == 335234613184299009):  # ucbrejects
        for i in range(len(whitespace2)-2):
            if whitespace2[i:i+3] == 'uwu':
                # uwu = discord.Client.get_channel(
                #     id=615077001115598872, self=client)
                # messageList = await flatten(uwu.history(limit=5000))
                # uwu = discord.Client.get_channel(
                #     id=745719332444831825, self=client)
                # messageList += await flatten(uwu.history(limit=5000))
                if msgs == []:
                    # read from msgs.json
                    msgs = json.load(open('msgs.json', 'r'))

                
                messageList = [msgs['ucbr'][i] for i in msgs['ucbr']] + [msgs['ucbr_p'][i] for i in msgs['ucbr_p']]

                messageListLen = len(messageList)
                randominte = random.randint(0, messageListLen-1)
                for server in msgs:
                    for msg in msgs[server]:
                        if msgs[server][msg]['msg'] == messageList[randominte]['msg'] and msgs[server][msg]['img'] == messageList[randominte]['img']:
                            uwud_ucbr = msg

                print(messageList[randominte], randominte)
                if len(messageList[randominte]["img"]) != "":
                    await message.channel.send(messageList[randominte]["img"] + " " + messageList[randominte]["msg"])
                else:
                    await message.channel.send(messageList[randominte]["msg"])
    if (message.guild.id == 679181801473703966):
        for i in range(len(whitespace2) - 2):
            if whitespace2[i:i + 3] == 'uwu':
                if msgs == []:
                    # read from msgs.json
                    msgs = json.load(open('msgs.json', 'r'))
                
                messageList = [msgs['rr'][i] for i in msgs['rr']] + [msgs['rr_p'][i] for i in msgs['rr_p']]
                messageListLen = len(messageList)
                randominte = random.randint(0, messageListLen - 1)
                uwud_rr = randominte
                if len(messageList[randominte]["img"]) != "":
                    await message.channel.send(messageList[randominte]["img"] + " " + messageList[randominte]["msg"])
                else:
                    await message.channel.send(messageList[randominte]["msg"])


@client.event
async def on_message_delete(message):
    if message.channel.id == 615077001115598872:
        db = firestore.client()
        db.collection("ucbr").document(str(message.id)).delete()
    elif message.channel.id == 681386070948315213:
        db = firestore.client()
        db.collection("rr").document(str(message.id)).delete()

client.run(os.getenv('UCBOT'))