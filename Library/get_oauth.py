# coding: utf-8

import tweepy
import settings


def get_oauth():

    CONSUMER_KEY = settings.CONSUMER_KEY
    CONSUMER_SECRET = settings.CONSUMER_SECRET

    ACCESS_TOKEN = settings.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return auth
