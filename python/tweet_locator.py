import sys
import tweepy
from tweepy import OAuthHandler
import json

if sys.argv[1] is None:
    print("""Usage:
        This script takes a single json file as an argument. The file contains
        a list of tweet IDs, one per line""")
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)



api = tweepy.API(auth)

tweet = api.get_status()
print(tweet.place)
