"""get timelines (last 100 tweets)
for tweeps from data/members.txt
raw json data is saved to files data/user.txt"""

import tweepy
from get_config import get_config
import os
import simplejson as json

from tweepy.binder import bind_api
from tweepy.parsers import *
class api_raw(tweepy.API):
    """ statuses/user_timeline """
    user_timeline = bind_api(
        path = '/statuses/user_timeline.json',
        parser = lambda x, api: x,
        allowed_param = ['id', 'user_id', 'screen_name', 'since_id',
                          'max_id', 'count', 'page']
    )

config = get_config()
user = config["twitter_username"]
auth = tweepy.BasicAuthHandler(config["twitter_username"], config["twitter_password"])
api = api_raw(auth)

file = open('data/members.txt','r')

count = 1

for user in file:

    user_name = user.strip().lower()
    print count, user_name
    count += 1 

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

    file_statuses = open('data/%s.txt' % user_name,'w')
    file_statuses.write(json.dumps(timeline))
    file_statuses.close()

    print len(timeline), 'tweets'
    print
