import time
import sys
import tweepy

from generate_advertisement import get_ad

# from credentials import *  # use this one for testing

# use this for production; set vars in heroku dashboard
from os import environ
CONSUMER_KEY = 'vXbtgZlOyNrSvDR1Wr0Avqedu'
CONSUMER_SECRET = 'UPsEeHn2CAZ0V5HDbFyryaBs4JzY8YXwKw0dtQkXxZF2DEs1Nz'
ACCESS_KEY = '1140648838580936704-86nhtF1dnDKO7mwfTmF1UzDyPNEazT'
ACCESS_SECRET = 'Z1iZJbiETOJL9BRCsqHR1qXg9Ynt02P5pqFr8j3F8QrDT'

# INTERVAL = 60 * 60 * 6  # tweet every 6 hours
INTERVAL = 30  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    print("ready to compile madlib phrase...")
    ad = get_ad()
    api.update_status(ad)
    time.sleep(INTERVAL)
