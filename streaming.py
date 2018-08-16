# coding: utf-8

import tweepy
import Library


def tweet(api, status):

    # "たこ焼きガチャ"もしくは"たこやきガチャ"というワードをTLで発見
    if "たこ焼きガチャ" in status.text or "たこやきガチャ" in status.text:
        # RTは除外
        if (not status.retweeted) and ("RT @" not in status.text):
            # status.auther.screen_name でツイ主のユーザー名を取得
            tweet_text = "@" + str(status.author.screen_name) + "\n"
            # Takoyakiのtweet_typeをリプに
            takotako = Library.takoyaki.Takoyaki(2)
            tweet_text += takotako.nyan()

            # ツイートがTwitterの文字数制限を超えていないかチェック
            # 超えていたら縮小
            tweet_text = Library.character_count.check_text_length(
                tweet_text)

            # logに残す
            # 残さなくても大丈夫なのですが、私が残したかったので
            print(tweet_text.split("\n")[0])  # @userID のところだけ表示

            try:
                # ツイートして、その送ったツイートの情報を受け取る
                sent_tweet_status = api.update_status(
                    tweet_text, status.id)
            except:
                sent_tweet_status = api.update_status(
                    "エラーが発生しました...。", status.id)

            # 今ツイートしたたこ焼きガチャのURLを自分自信(bot)にDMで送る
            # これも行う必要は全く無いのですが、自分が記録として残しておきたかったので
            dm_text = "https://twitter.com/{}/status/{}".format(str(sent_tweet_status.author.screen_name),
                                                                sent_tweet_status.id_str)
            api.send_direct_message(
                screen_name="moko_takoyaki", text=dm_text)


def tl_check():
    auth = Library.get_auth.get_auth()
    api = tweepy.API(auth)
    for status in api.home_timeline(count=200):
        try:
            tweet(api, status)
        except tweepy.TweepError as e:
            print(e.reason)
