import tweepy
import settings
from takoyaki import Takoyaki

CONSUMER_KEY = settings.CONSUMER_KEY
CONSUMER_SECRET = settings.CONSUMER_SECRET

ACCESS_TOKEN = settings.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def tweet():
    takotako = Takoyaki()
    sentence = takotako.nyan()
    print(sentence)
    api.update_status(sentence)

def main():
    tweet()

if __name__ == "__main__":
    main()
