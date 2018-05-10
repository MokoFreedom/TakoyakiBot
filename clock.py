from apscheduler.scheculers.blocking import BlockingScheduler
import regular_tweet

twische = BlockingScheduler()

@twische.scheculed_job("interval", hours=4)
def timed_job():
    tweet.moko_takoyaki()

if __name__ == "__main__":
    twische.start()
