#!/usr/bin/python
import oauth2 as oauth
import json

config = {}
execfile("twitter_config.py",config)

consumer = oauth.Consumer(key=config["consumer_key"],secret=config["consumer_secret"])
request_token_url = "https://api.twitter.com/oauth/request_token"
client = oauth.Client(consumer)
resp,content = client.request(request_token_url,"GET")

tweet_search = 'https://api.twitter.com/1.1/followers/ids.json?screen_name='+config["account"]
response = client.request(tweet_search, "GET")
output = json.loads(response[1])
num_ids = len(output["ids"])
print output["ids"],num_ids
