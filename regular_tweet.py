# coding: utf-8

import tweepy
from Library.character_count import check_text_length
from Library.get_auth import get_auth
from Library.takoyaki import Takoyaki


def connect_and_tweet(sentence):
    """
    apiに接続し、sentenceをツイートする
    """

    auth = get_auth()
    api = tweepy.API(auth)

    api.update_status(sentence)


def takoyaki_tweet(tweet_type):
    """
    日本時間で4の倍数時に行うたこ焼きの定期ツイ
    tweet_type: 通常は0(定期ツイ), テスト時は1
    """

    # たこ焼きのツイートを生成
    takotako = Takoyaki(tweet_type)
    sentence = takotako.nyan()

    # ツイートの文字数制限を超えていないかチェック
    # 超えていたら縮小
    sentence = check_text_length(sentence)

    connect_and_tweet(sentence)


def odaibako_tweet():
    """
    日本時間で9時,21時に行うお題箱の定期ツイ
    """

    sentence = "[定期]\n\n"
    sentence += "たこ焼き屋 -調理場-\n\n"
    sentence += "お題箱です。\n\n"
    sentence += "たこ焼きの具やトッピング、売買時のメッセージなどのリクエスト受付中です。入れて下さると嬉しすぎます。\n"
    sentence += "https://odaibako.net/u/moko_takoyaki  #odaibako"

    connect_and_tweet(sentence)
