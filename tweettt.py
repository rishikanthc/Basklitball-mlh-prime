#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '97JgwtwX0gub3vE30ZhP6aKZs'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '5gRcGRNFxQmglehMmMKkealtpszXXmpmzb2YRnOtV0lg6t97lY'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1944376015-WjKOE2E4Ir2pznuKcncANbii0da3cPcYpAnsxZA'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'lB6lrpXzS1ibabKAq8YEnkBYJhYdzLHGT3IGFJE10Pzsv'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status("Hey")
    time.sleep(900)#Tweet every 15 minutes
