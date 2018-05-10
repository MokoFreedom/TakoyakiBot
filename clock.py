from apscheduler.schedulers.blocking import BlockingScheduler
import regular_tweet

sched = BlockingScheduler()

@sched.scheduled_job("interval", hours=4, start_date="2018-05-10 15:00:00")
def timed_job():
    regular_tweet.moko_takoyaki()

if __name__ == "__main__":
    sched.start()
