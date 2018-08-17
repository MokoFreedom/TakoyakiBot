import tweepy
import Library
from typing import Set

list_name = "follow takoyaki"


def list_members(api: tweepy.API, listID: str)->Set[int]:
    set([x.id for x in tweepy.Cursor(api.list_members, list_id=listID).items()])


def followers(api: tweepy.API)->Set[int]:
    set(list(tweepy.Cursor(api.followers_ids, user_id=api.me().id).items()))


def friends(api: tweepy.API)->Set[int]:
    set(list(tweepy.Cursor(api.friends_ids, user_id=api.me().id).items()))


def outgoing(api: tweepy.API)->Set[int]:
    set([int(x) for x in tweepy.Cursor(api.friendships_outgoing).items()])
