from apscheduler.scheculers.blocking import BlockingScheduler
import regular_tweet

sched = BlockingScheduler()

@sched.scheduled_job("interval", minutes=5)
def timed_job():
    tweet.moko_takoyaki()

if __name__ == "__main__":
    sched.start()
