# coding: utf-8

import tweepy
from Library.character_count import check_text_length
from Library.get_oauth import get_oauth
from Library.takoyaki import Takoyaki


def connect_and_tweet(sentence):

    auth = get_oauth()
    api = tweepy.API(auth)

    api.update_status(sentence)


def takoyaki_tweet(tweet_type):

    takotako = Takoyaki(tweet_type) # tweet_typeを定期ツイに指定。
    sentence = takotako.nyan()

    sentence = check_text_length(sentence)
    connect_and_tweet(sentence)


def odaibako_tweet():
    
    sentence = "[定期]\n\n"
    sentence += "たこ焼き屋 -調理場-\n\n"
    sentence += "お題箱です。\n\n"
    sentence += "たこ焼きの具やトッピング、売買時のメッセージなどのリクエスト受付中です。入れて下さると嬉しすぎます。\n"
    sentence += "https://odaibako.net/u/moko_takoyaki  #odaibako"

    print(sentence)
    connect_and_tweet(sentence)
