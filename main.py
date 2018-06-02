# coding: utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet
import streaming
from Library.get_oauth import get_oauth


sched = BlockingScheduler()


@sched.scheduled_job("cron", hour="3,7,11,15,19,23")     
def timed_takoyaki_tweet():
    regular_tweet.takoyaki_tweet(0)


@sched.scheduled_job("cron", hour="0,12")
def timed_odaibako_tweet() :
    regular_tweet.odaibako_tweet()


if __name__ == "__main__":

    streaming.takoyaki_streaming()
    sched.start()
