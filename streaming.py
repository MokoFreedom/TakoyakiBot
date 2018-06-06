# coding: utf-8

import tweepy
from Library.character_count import check_text_length
from Library.get_auth import get_auth
from Library.takoyaki import Takoyaki


api = None


class TakoyakiListener(tweepy.StreamListener):

    def __init__(self, api):
        super().__init__(api)
        self.me = self.api.me()


    def on_status(self, status):

        # "たこ焼きガチャ"もしくは"たこやきガチャ"というワードをTLで発見
        if "たこ焼きガチャ" in status.text or "たこやきガチャ" in status.text:
            # RTは除外
            if (not status.retweeted) and ("RT @" not in status.text):
                # status.auther.screen_name でツイ主のユーザー名を取得
                tweet_text = "@" + str(status.author.screen_name)  + "\n"
                # Takoyakiのtweet_typeをリプに
                takotako = Takoyaki(2)
                tweet_text += takotako.nyan()

                # ツイートがTwitterの文字数制限を超えていないかチェック
                # 超えていたら縮小
                tweet_text = check_text_length(tweet_text)

                # logに残す
                # 残さなくても大丈夫なのですが、私が残したかったので
                print(tweet_text.split("\n")[0]) # @userID のところだけ表示

                # ツイートして、その送ったツイートの情報を受け取る
                sent_tweet_status = api.update_status(tweet_text, status.id)

                # 今ツイートしたたこ焼きガチャのURLを自分自信(bot)にDMで送る
                # これも行う必要は全く無いのですが、自分が記録として残しておきたかったので
                dm_text = "https://twitter.com/{}/status/{}".format(str(sent_tweet_status.author.screen_name),\
                                                                    sent_tweet_status.id_str)
                api.send_direct_message(screen_name="moko_takoyaki", text=dm_text)

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

    auth = get_auth()
    global api
    api = tweepy.API(auth)

    stream = tweepy.Stream(auth, TakoyakiListener(api), secure=True)
    stream.userstream(async=True)
