# coding: utf-8

import tweepy
import settings
from takoyaki import Takoyaki


api = None


def get_oauth():
    
    CONSUMER_KEY = settings.CONSUMER_KEY
    CONSUMER_SECRET = settings.CONSUMER_SECRET

    ACCESS_TOKEN = settings.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return auth


class TakoyakiListener(tweepy.StreamListener):

    def __init__(self, api):
        super().__init__(api)
        self.me = self.api.me()
    
    
    def on_status(self, status):

        if "たこ焼きガチャ" in status.text:
            if (not status.retweeted) and ("RT @" not in status.text):
                res = "@" + str(status.author.screen_name)  + "\n"
                takotako = Takoyaki(2)
                res += takotako.nyan()

                print(res)

                api.update_status(res, status.id)
        
        return True

    
    def on_event(self, event):
        # 自動フォロー
        if event.event == "follow":
            if self.me.id != event.source["id"]:
                source_user = event.source
                event._api.create_friendship(source_user["id"])
                print("followed by {} {}".format(source_user["name"], source_user["screen_name"]))


    def on_error(self, status_code):
        
        print("Omg...Got an error...: " + str(status_code))
        return True


    def on_timeout(self):

        print("Timeout...nyan...")
        return True


def takoyaki_streaming():

    auth = get_oauth()
    global api
    api = tweepy.API(auth)

    stream = tweepy.Stream(auth, TakoyakiListener(api), secure=True)
    stream.userstream(async=True)
