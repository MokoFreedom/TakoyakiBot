# coding: utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet
import streaming
from sync import sync, find_list
import tweepy
import Library

api = tweepy.API(Library.get_auth.get_auth())
list_id = find_list(api)

api.update_status("起動しましたたこ。")

# スケジューラー
sched = BlockingScheduler()


# 日本時間で4の倍数時に行うたこ焼きの定期ツイ
# 設定のhourはUTC
@sched.scheduled_job("cron", hour="3,7,11,15,19,23")
def timed_takoyaki_tweet():
    regular_tweet.takoyaki_tweet(0)


# 日本時間で9時,21時に行うお題箱の定期ツイ
# 設定のhourはUTC
@sched.scheduled_job("cron", hour="0,12")
def timed_odaibako_tweet():
    regular_tweet.odaibako_tweet()


# 2秒に一回TL取得
@sched.scheduled_job("interval", seconds=2)
def tl_tweet():
    streaming.tl_check(list_id)


# 30分に一回リスト同期
@sched.scheduled_job("cron", minute="0,30")
def timed_sync():
    print("同期")
    sync(api, list_id)


if __name__ == "__main__":
    # スケジューラー開始
    sched.start()
