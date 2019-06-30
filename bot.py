import time
import sys
import tweepy

from generate_advertisement import get_ad

# from credentials import *  # use this one for testing

# use this for production; set vars in heroku dashboard
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# INTERVAL = 60 * 60 * 24  # tweet every 24 hours
INTERVAL = 30  # every 30 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    print("ready to compile madlib phrase...")
    ad = get_ad()
    api.update_status(ad)
    time.sleep(INTERVAL)
