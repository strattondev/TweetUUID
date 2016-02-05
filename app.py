from config import CONFIG_TWITTER

import tweepy
import uuid

auth = tweepy.OAuthHandler(CONFIG_TWITTER['key'], CONFIG_TWITTER['secret'])
auth.set_access_token(CONFIG_TWITTER['access_key'], CONFIG_TWITTER['access_secret'])

twitter = tweepy.API(auth)

def run():
    status = twitter.update_status(status="{} #uuid".format(str(uuid.uuid4())))

if __name__ == "__main__":
    run()