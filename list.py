import tweepy
import Library
import typing

list_name = "follow takoyaki"


def list_members(api: tweepy.API, listID: str)->typing.Set[int]:
    return set([x.id for x in tweepy.Cursor(api.list_members, list_id=listID).items()])


def followers(api: tweepy.API)->typing.Set[int]:
    return set(list(tweepy.Cursor(api.followers_ids, user_id=api.me().id).items()))


def friends(api: tweepy.API)->typing.Set[int]:
    return set(list(tweepy.Cursor(api.friends_ids, user_id=api.me().id).items()))


def outgoing(api: tweepy.API)->typing.Set[int]:
    return set([int(x) for x in tweepy.Cursor(api.friendships_outgoing).items()])


def create_list(api: tweepy.API)->int:
    return api.create_list(name=list_name, mode="private").id


# リストを探しIDを返す、なければ新しく作成する
def find_list(api: tweepy.API)->int:
    for x in api.lists_all():
        if x.name == list_name:
            return x.id
    return create_list(api)
