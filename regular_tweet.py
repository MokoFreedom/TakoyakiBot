import tweepy
from takoyaki import Takoyaki

CONSUMER_KEY = "Y7C8ozoZXn5YIq97on6seWzqA"
CONSUMER_SECRET = "JYEUQd0OiRCaII40DDhZxWODk2Wyg0A6RtO08BOgocFXqtbEvZ"

ACCESS_TOKEN = "993799205608079361-JbAI9w3BkUgHOxGIAiLSNvmfaBlqHAC"
ACCESS_TOKEN_SECRET = "d5dKwCj8l8CBiduRKwOaM4PjUHHXmBiuRfq567FrT3lv3"

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
