"""get """
import os

from get_config import get_config
import tweepy

config = get_config()
user = config["twitter_username"]

auth = tweepy.BasicAuthHandler(config["twitter_username"], config["twitter_password"])
api = tweepy.API(auth)

lists = []

file = open('data/members.txt','r')

members = {}
for user in file:
    user_name = user.strip().lower()
    members[user_name] = {}

count = 0

for user_name in members:

    print count, user_name
    count += 1

    file_name_lists = 'data/%s_lists.txt' % user_name

    if os.path.exists(file_name_lists):
        print file_name_lists + ' exists'
        file_lists = open(file_name_lists,'r')
        if file_lists.read().strip():
            file_lists.close()
            continue
        else:
            print 'but empty'
            file_lists.close()

    file_lists = open(file_name_lists,'w')
    try:
        for list in tweepy.Cursor(api.lists_memberships, user=user_name).items():
            file_lists.write(list.full_name+'\n')
            print list.full_name
    except tweepy.error.TweepError, v:
        print 'tweepy error: %s' % v

    file_lists.close()

    print
