# coding: utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet
import my_stream

sched = BlockingScheduler()

@sched.scheduled_job("interval", minutes=1,  start_date="2018-05-15 15:26:00")     
def timed_job():
    regular_tweet.moko_takoyaki(1)

if __name__ == "__main__":

    my_stream.takoyaki_streaming()
    sched.start()
