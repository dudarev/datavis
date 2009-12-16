from get_config import get_config
import tweepy

config = get_config()
user = config["twitter_username"]

auth = tweepy.BasicAuthHandler(config["twitter_username"], config["twitter_password"])
api = tweepy.API(auth)

followers = []

for follower in tweepy.Cursor(api.followers).items():
    followers.append(follower)
    print follower.screen_name

file = open("data/followers.txt","w")

for follower in followers:
    file.write(follower.screen_name+'\n')

file.close()
