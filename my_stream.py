# coding: utf-8

import tweepy
from get_oauth import get_oauth
from takoyaki import Takoyaki


api = None


class TakoyakiListener(tweepy.StreamListener):

    def __init__(self, api):
        super().__init__(api)
        self.me = self.api.me()
    
    
    def on_status(self, status):

        if "たこ焼きガチャ" in status.text or "たこやきガチャ" in status.text:
            if (not status.retweeted) and ("RT @" not in status.text):
                tweet_text = "@" + str(status.author.screen_name)  + "\n"
                takotako = Takoyaki(2)
                tweet_text += takotako.nyan()

                if len(tweet_text) > 140:
                    tweet_text = tweet_text[:133]
                    tweet_text += "文字数((ry"

                print(tweet_text.split("\n")[0]) # @userID のところだけ表示
                print("{}文字です。".format(len(tweet_text)))

                sent_tweet_status = api.update_status(tweet_text, status.id)

                dm_text = "https://twitter.com/{}/status/{}".format(str(sent_tweet_status.author.screen_name),\
                                                                    sent_tweet_status.id_str)
                
                api.send_direct_message(screen_name="moko_takoyaki", text=dm_text) # たこ焼きガチャのurlを自分にDMで送信
        
        return True

    
    def on_event(self, event):
        # 自動フォロー
        if event.event == "follow":
            if self.me.id != event.source["id"]:
                source_user = event.source
                event._api.create_friendship(source_user["id"])
                print("followed by {} {}".format(source_user["name"], source_user["screen_name"]))


    def on_error(self, status_code):
        
        api.update_status("Omg...An error occured...Sorry...")
        print("Omg...Got an error...: " + str(status_code))
        return True


    def on_timeout(self):

        api.update_status("Timeout...nyan...Sorry...")
        print("Timeout...nyan...")
        return True


def takoyaki_streaming():

    auth = get_oauth()
    global api
    api = tweepy.API(auth)

    stream = tweepy.Stream(auth, TakoyakiListener(api), secure=True)
    stream.userstream(async=True)
