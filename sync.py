import tweepy
import Library
import typing

list_name = "follow takoyaki"


def find_members(api: tweepy.API, listID: str)->typing.Set[int]:
    return set([x.id for x in tweepy.Cursor(api.list_members, list_id=listID).items()])


def find_followers(api: tweepy.API)->typing.Set[int]:
    return set(list(tweepy.Cursor(api.followers_ids, user_id=api.me().id).items()))


def find_friends(api: tweepy.API)->typing.Set[int]:
    return set(list(tweepy.Cursor(api.friends_ids, user_id=api.me().id).items()))


def find_outgoing(api: tweepy.API)->typing.Set[int]:
    return set([int(x) for x in tweepy.Cursor(api.friendships_outgoing).items()])


def create_list(api: tweepy.API)->int:
    return api.create_list(name=list_name, mode="private").id


# リストを探しIDを返す、なければ新しく作成する
def find_list(api: tweepy.API)->int:
    for x in api.lists_all():
        if x.name == list_name:
            return x.id
    print("リスト作成")
    return create_list(api)


def sync_list(api: tweepy.API, list_id: int, friends: typing.Set[int], members: typing.Set[int]):
    # リストに追加
    for id in friends-members:
        print("リスト追加:"+str(id))
        api.add_list_member(list_id=list_id, user_id=id)
    # リストから削除
    for id in members-friends:
        print("リスト削除:"+str(id))
        api.remove_list_member(list_id=list_id, user_id=id)


def sync_friends(api: tweepy.API, friends: typing.Set[int], followers: typing.Set[int], outgoing: typing.Set[int]):
    # フォロー
    for id in followers-friends-outgoing:
        print("フォロー:"+str(id))
        api.create_friendship(user_id=id)

    # リム
    for id in friends-followers:
        print("アンフォロー:"+str(id))
        api.destroy_friendship(user_id=id)


def sync(api: tweepy.API, list_id: int):
    members = find_members(api, list_id)
    friends = find_friends(api)
    followers = find_followers(api)
    outgoing = find_outgoing(api)

    sync_list(api, list_id, friends, members)
    sync_friends(api, friends, followers, outgoing)
