# coding: utf-8

import tweepy
import settings
from takoyaki import Takoyaki


def connect_and_tweet(sentence):

    CONSUMER_KEY = settings.CONSUMER_KEY
    CONSUMER_SECRET = settings.CONSUMER_SECRET

    ACCESS_TOKEN = settings.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    api.update_status(sentence)

def moko_takoyaki():

    takotako = Takoyaki(0) # tweet_typeを定期ツイに指定。
    sentence = takotako.nyan()
    print(sentence)
    connect_and_tweet(sentence)
