# coding: utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet
import my_stream

sched = BlockingScheduler()

@sched.scheduled_job("interval", hours=4,  start_date="2018-05-16 15:00:00")     
def timed_job():
    regular_tweet.moko_takoyaki(0)

if __name__ == "__main__":

    my_stream.takoyaki_streaming()
    sched.start()
