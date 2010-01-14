"""get group members from a list of a user @user/slug"""

from get_config import get_config
import tweepy

user = 'dudarev'
slug = 'donetsk'

config = get_config()
user = config["twitter_username"]

auth = tweepy.BasicAuthHandler(config["twitter_username"], config["twitter_password"])
api = tweepy.API(auth)

members = []

for member in tweepy.Cursor(api.list_members, owner=user, slug=slug).items():
    members.append(member)
    print member.screen_name

file = open("data/members.txt","w")

for member in members:
    file.write(member.screen_name+'\n')

file.close()
