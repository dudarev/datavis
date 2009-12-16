from get_config import get_config
import tweepy
from pylab import *
import sys,os

config = get_config()
user = config["twitter_username"]

auth = tweepy.BasicAuthHandler(config["twitter_username"], config["twitter_password"])
api = tweepy.API(auth)

file = open('data/followers.txt','r')

hours = arange(24)

for user in file:

    user_name = user.strip()
    print user_name

    if os.path.exists('data/%s.txt' % user_name):
        print 'data/%s.txt exists' % user_name
        file_counts = open('data/%s.txt' % user_name,'r')
        if file_counts.read().strip():
            file_counts.close()
            continue
        else:
            print 'but empty'
            file_counts.close()

    try:
        timeline = api.user_timeline(user_name,count=100)
    except tweepy.TweepError, e: 
        print "error: %s user: %s" % (e,user_name)
        continue

    print len(timeline)

    counts = {}
    counts_array = []

    for status in timeline:
        h = status.created_at.hour
        counts[h] = counts.get(h,0) + 1

    file_counts = open('data/%s.txt' % user_name,'w')
    file_counts.write(user_name)

    for h in hours:
        counts_array.append(counts.get(h,0))
        file_counts.write(',%d' % counts.get(h,0))

    file_counts.close()

    print counts_array
    print
