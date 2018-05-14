# coding: utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet
import stream

sched = BlockingScheduler()

@sched.scheduled_job("interval", minutes=1, start_date="2018-05-14 13:45:00")
def timed_job():
    regular_tweet.moko_takoyaki(1)

if __name__ == "__main__":

    sched.start()
    stream.takoyaki_streaming()
