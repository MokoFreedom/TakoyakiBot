# coding: utf-8

import tweepy
from get_oauth import get_oauth
from takoyaki import Takoyaki


def local():
    
    takotako = Takoyaki(1) # tweet_typeをテストに設定。
    nya = takotako.nyan()
    print(nya)
    print(len(nya))


def not_local():

    takotako = Takoyaki(1)
    nya = takotako.nyan()

    auth = get_oauth()
    api = tweepy.API(auth)

    print(nya)
    api.update_status(nya)


if __name__ == "__main__":

    #local()
    not_local()

