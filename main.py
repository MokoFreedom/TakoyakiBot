# coding: utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet
import streaming


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
def timed_odaibako_tweet() :
    regular_tweet.odaibako_tweet()


if __name__ == "__main__":

    # ストリーミング開始
    streaming.takoyaki_streaming()
    # スケジューラー開始
    sched.start()
