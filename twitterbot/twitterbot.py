from twython import Twython
from lyrics import make_tweet
from time import sleep

APP_KEY = 'KbfgQhe2D4mSudrbLuJGtiY0W'
APP_SECRET = '88KGrdAwPYvjUCpZNZq8r8MekwudkhCzNzKpTratWtIw6JNjrq'
OAUTH_TOKEN = '1094684224781799425-NVNIiJln26hNI2ioq9ogR9dnQsMTyA'
OAUTH_TOKEN_SECRET = 'gN6Da4z1QUJQWGtwlfIGbyea1HvMm19S0HHdIV7OAjX7A'
WAIT_TIME = 3600

def send_tweet(tweet):
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter.update_status(status=tweet)

while True:
    send_tweet(make_tweet.build_tweet())
    sleep(WAIT_TIME)
