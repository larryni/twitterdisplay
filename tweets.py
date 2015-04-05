#!/usr/bin/env python

import os
import tweepy
import csv

# path to csv file (same folder as the js file)
pathcsv = "/home/laurent/Projects/twitterdisplay/"

consumer_key = "sP6KhOuF2Gf62WPW6JJttlLMY"
consumer_secret = "xYk4AtDEqKeBpX9Gbyle3oU7wccsYbMqCilBnnFJJORAlJpgwl"
access_token = "14101981-JITYeJslYxGq87YvDvwD7WCKPxXpR8LP5XnVjHjfX"
access_token_secret = "81IBq2A3e4HvObv6SnwF9FWAPwDrzIDSDZZunmmnx050m"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

timeline_tweets = api.home_timeline(count=20)

f = open(os.path.join(pathcsv, "tweets.csv"),"wb")
csvwriter = csv.writer(f, delimiter="\t", escapechar="\\", quotechar="'", quoting=csv.QUOTE_MINIMAL, doublequote=False)

for tweet in timeline_tweets:
	
	tweettext = (tweet.text).replace('\n', '<br>')
	entities = tweet.entities
	linklist = entities['urls']
	
    # check if entities contains the 'media' key to prevent error
	if 'media' in entities.keys():
		media = entities['media']
		for i in media:
			medialink = i['media_url']
	else:
		medialink = "none"
	
    # expand twitter's shortened urls
	for link in linklist:
		twitter_link = link['url']
		expanded_link = link['expanded_url']
		tweettext = tweettext.replace(twitter_link,expanded_link)
        
	csvwriter.writerow([unicode(tweet.user.name).encode("utf-8"), # display name
						unicode(tweet.user.screen_name).encode("utf-8"), # username
						unicode(tweet.user.profile_image_url.replace('_normal', '_bigger')).encode("utf-8"), # '_normal' - 48x48 image, '_bigger' - 73x73 image
						unicode(tweet.created_at).encode("utf-8"), # tweet sent date
						unicode(tweettext).encode("utf-8"), # tweet content
						unicode(medialink).encode("utf-8")]) # embedded picture link
f.close()
