import discord
from discord.ext import commands
import random
import time
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# ucbot
intents = discord.Intents.all()

client = commands.Bot(command_prefix='~', intents=intents)




@client.event
async def on_ready():
    print('bls')
@client.event
async def on_message(message):
    # print(message.author.id)

    if message.content=='jni325uyyguh53000bjniuih78873' or random.randint(0,100000) == 10:
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






    async def flatten(hist):
        a = []
        async for i in hist:
            a.append(i)
        return a

    uwu2 = message.channel
    messageList2 = await flatten(uwu2.history(limit=3))
    # print(messageList2)


    firstm = messageList2[0].content.lower()
    secondm = messageList2[1].content.lower()
    thirdm = messageList2[2].content.lower()

    # print('firstm: ' + firstm)
    # print('secondm: ' + secondm)
    # print('thirdm: ' + thirdm)

    if secondm == firstm and not messageList2[0].author.bot and not messageList2[1].author.bot and not messageList2[2].author.bot:
        for i in range(len(thirdm)-len(firstm)+1):
            # print(thirdm[i:i+len(thirdm)])
            if thirdm[i:i+len(firstm)]==firstm:
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
    if(message.guild.id == 335234613184299009): # ucbrejects
        for i in range(len(whitespace2)-2):
            if whitespace2[i:i+3] == 'uwu':
                # uwu = discord.Client.get_channel(id=615077001115598872, self = client)
                uwu = discord.Client.get_channel(client,615077001115598872)
                messageList = await flatten(uwu.history(limit=5000))
                uwu = discord.Client.get_channel(client,745719332444831825)
                messageList += await flatten(uwu.history(limit=5000))
                messageListLen = len(messageList)
                randominte = random.randint(0, messageListLen-1)
                # print(len(messageList))
                # print(randominte)
                if len(messageList[randominte].attachments) > 0:
                    await message.channel.send(messageList[randominte].attachments[0].url)
                if len(messageList[randominte].attachments) == 0:
                    await message.channel.send(messageList[randominte].content)
    if (message.guild.id == 679181801473703966):
        for i in range(len(whitespace2) - 2):
            if whitespace2[i:i + 3] == 'uwu':
                uwu = discord.Client.get_channel(client, 681386070948315213)
                messageList = await flatten(uwu.history(limit=5000))
                uwu = discord.Client.get_channel(client, 745724886281879632)
                messageList += await flatten(uwu.history(limit=5000))
                messageListLen = len(messageList)
                randominte = random.randint(0, messageListLen - 1)
                if len(messageList[randominte].attachments) > 0:
                    await message.channel.send(messageList[randominte].attachments[0].url)
                if len(messageList[randominte].attachments) == 0:
                    await message.channel.send(messageList[randominte].content)


client.run(os.getenv('UCBOT'))
