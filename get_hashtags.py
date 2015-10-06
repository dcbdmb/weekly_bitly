#!/usr/bin/python
#
# useful link to get the URL right: https://twitter.com/search-advanced
#
import oauth2 as oauth
import json
import urllib
import getopt
import sys

def check_input():
    options,remainder = getopt.gnu_getopt(sys.argv[1:], 'u:', ['url='])

    opt_count = 0

    for opt,arg in options:
        opt_count = opt_count + 1
        if opt in ('-u','--url'):
            bitly_url = arg
        else:
            print 'bad option given'
            opt_count = opt_count - 1

    if (opt_count == 0):
        print "usage is:",sys.argv[0]
        print '\t-u, --url'
        exit()

    return(bitly_url)

bitly_url = check_input()

config = {}
execfile("twitter_config.py",config)
consumer = oauth.Consumer(key=config["consumer_key"],secret=config["consumer_secret"])
request_token_url = "https://api.twitter.com/oauth/request_token"
client = oauth.Client(consumer)
resp,content = client.request(request_token_url,"GET")

bitly=urllib.quote_plus(bitly_url)
tweet_search = 'https://api.twitter.com/1.1/search/tweets.json?q="'+bitly+'"%40from:'+config["account"]
response = client.request(tweet_search, "GET")
output = json.loads(response[1])
hashtags = output["statuses"][0]["entities"]["hashtags"]
for hashtag in hashtags:
    print hashtag["text"]
#print json.dumps(hashtags, indent=4, sort_keys=True)
