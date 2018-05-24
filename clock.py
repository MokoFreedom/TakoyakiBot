# coding: utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet
import my_stream
import odaibako_tweet

sched = BlockingScheduler()

@sched.scheduled_job("interval", hours=4,  start_date="2018-05-23 11:00:00")     
def timed_tweet():
    regular_tweet.moko_takoyaki(0)

@sched.scheduled_job("cron", hour="0,12")
def odaibako() :
    odaibako_tweet.tweet()

if __name__ == "__main__":

    my_stream.takoyaki_streaming()
    sched.start()
