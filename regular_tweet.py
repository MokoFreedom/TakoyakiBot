# coding: utf-8

import tweepy
from get_oauth import get_oauth
from takoyaki import Takoyaki


def connect_and_tweet(sentence):

    auth = get_oauth()
    api = tweepy.API(auth)

    api.update_status(sentence)


def moko_takoyaki(tweet_type):

    takotako = Takoyaki(tweet_type) # tweet_typeを定期ツイに指定。
    sentence = takotako.nyan()
    print(sentence)
    connect_and_tweet(sentence)
