from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet

sched = BlockingScheduler()

@sched.scheduled_job("interval", minutes=1, start_date="2018-05-10 21:10:00")
def timed_job():
    regular_tweet.moko_takoyaki()

if __name__ == "__main__":
    sched.start()
