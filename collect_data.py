import tweepy
import json
import jsonpickle
import re
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pprint import pprint
from collections import Counter, OrderedDict
import plotly.graph_objects as go
import csv


consumer_key = "n4z0l4XN4WDTWrDztFIGTurTj"
consumer_secret = "50aNtfg4NKlam5oHsc3aGvKN3uYdil5OSSyvxwv6iDdgQl65RC"
access_token = "1331204142-ZUHzv0f352cGQliAsMNcCuLAYOfg9AnhBk2J6wA"
access_token_secret = "1sgHt1JBlZaO6sSxabj2EwHfdO9YeZWyIobJE2U1EfUF7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tags = api.trends_place(2295414)
top_tags = tags[0]['trends']
top_tag = ""
for tag in top_tags:
    if tag['name'].startswith("#"):
        top_tag = tag['name']
        break
query = top_tag
query += " exclude:retweets"
print(query, " is the query")
max_tweets = 20000




csvFile = open('data.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)

# Write column names
csvWriter.writerow(["tweet_id", "tweet_full_text", "tweet_created_at", "tweet_lang", "hashtags", "tweet_retweet_count", "tweet_favorite_count", "tweet_place", "user_id", "user_screen_name", "user_followers_count", "user_friends_count", "user_created_at", "user_favourites_count", "user_statuses_count", "user_lang", "user_verified", "user_location"])
i = 1

for tweet in tweepy.Cursor(api.search, tweet_mode="extended", q=query).items(max_tweets):
    hashtag = ""
    for has in tweet.entities.get('hashtags'):
        hashtag += "#"+has['text']+" "
    print(i)
    i+=1
        
    csvWriter.writerow([tweet.id, tweet.full_text.encode('utf-8'), tweet.created_at, tweet.lang, hashtag, tweet.retweet_count, tweet.favorite_count, tweet.place.full_name + ', ' + tweet.place.country_code if tweet.place else "Not tagged", tweet.user.id, tweet.user.screen_name, tweet.user.followers_count, tweet.user.friends_count, tweet.user.created_at, tweet.user.favourites_count, tweet.user.statuses_count, tweet.user.lang, tweet.user.verified, tweet.user.location])

