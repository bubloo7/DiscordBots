import tweepy
import requests
import random
import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


consumer_key = os.getenv('CONSUMER_KEY_UWUBOT9')
consumer_secret = os.getenv('CONSUMER_SECRET_UWUBOT9')
access_token = os.getenv('ACCESS_TOKEN_UWUBOT9')
acess_token_secret = os.getenv('ACCESS_TOKEN_SECRET_UWUBOT9')
t = True

# twitter api stuff


def oath():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, acess_token_secret)
        return auth
    except Exception as e:
        print(e)
        return None

# code for printing an image. Source: https://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy


def tweet_image(message, url, api):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_status_with_media(filename=filename, status=message)
    else:
        print("Unable to download image")


def tweet_message(message, api):
    api.update_status(message)


oauth = oath()
api = tweepy.API(oauth)

msgs = json.loads(open("msgs.json", "r").read())
allMsgs = [msgs['ucbr'][i] for i in msgs['ucbr']]  + [msgs['rr'][i] for i in msgs['rr'] if msgs['rr'][i]['img'] != ""]

while True:
    randomMsg = random.choice(allMsgs)
    print(randomMsg)

    try:
        if randomMsg["img"] == "":
            tweet_message(randomMsg["msg"], api)
        else:
            tweet_image(randomMsg["msg"], randomMsg["img"], api)
    except Exception as e:
        print(e)
        continue
    break
