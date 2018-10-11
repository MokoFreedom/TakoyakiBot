# coding: utf-8

import tweepy
import regular_tweet
from Library.takoyaki import Takoyaki

class TakoyakiTest:

    def local(self):
    
        takotako = Takoyaki(1) # tweet_typeをテストに設定。
        nya = takotako.nyan()
        print(nya)
        print(len(nya))


    def not_local(self):

        regular_tweet.takoyaki_tweet(1)


class OdaibakoTest:

    def local(self):
        
        pass


    def not_local(self):

        regular_tweet.odaibako_tweet()


if __name__ == "__main__":

    # テスト内容記述
    tako = TakoyakiTest()
    odai = OdaibakoTest()

    tako.local()
    #tako.not_local()

    #odai.local()
    #odai.not_local()
