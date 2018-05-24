# coding: utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet
import my_stream


sched = BlockingScheduler()


@sched.scheduled_job("interval", hours=4,  start_date="2018-05-23 11:00:00")     
def timed_takoyaki_tweet():
    regular_tweet.takoyaki_tweet(0)


@sched.scheduled_job("cron", hour="0,12")
def timed_odaibako_tweet() :
    regular_tweet.odaibako_tweet()


if __name__ == "__main__":

    my_stream.takoyaki_streaming()
    sched.start()
