from apscheculer.schedulers.blocking import BlockingScheduler
from takoyaki import Takoyaki

sched = BlockingScheduler()

@sched.scheduled_job("interbal", minutes=1)
def tweet_test():
    takotako = Takoyaki(1) # tweet_typeをテストに設定。
    nya = takotako.nyan()
    print(nya)
    print(len(nya))
