#!/usr/bin/python
import requests
import json
import getopt
import sys

def check_input():

    options, remainder = getopt.gnu_getopt(sys.argv[1:], 'u:', ['url='])

    opt_count = 0

    for opt,arg in options:
        opt_count = opt_count + 1
        if opt in ('-u','--url'):
            long_url = arg
        else:
            print 'bad option given'
            opt_count = opt_count - 1

    if (opt_count == 0):
        print "usage is:",sys.argv[0]
        print '\t-u, --url'
        exit()

    return (long_url)

long_url = check_input()

config = {}
execfile("bitly_config.py",config)

link_params = {'access_token':config['token'], 'url':long_url} 

link_lookup = 'https://api-ssl.bitly.com/v3/user/link_lookup'
response = requests.get(link_lookup, params=link_params, verify=True)

output = response.json()['data']['link_lookup'][0]
if 'error' in output.keys():
    print "The URL:\n",output['url'],"\n WAS NOT FOUND!!!"
else:
    print "The URL:\n",output['url'],"\n WAS already saved as:",output['link']
