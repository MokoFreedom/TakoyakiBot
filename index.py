# coding: utf-8

# Herokuでプロセスを動かしておくためのダミーのWebアプリ
# botとは直接関係が無いらしい
# 動作が安定するとか読んだ
# bottleのドキュメント(http://bottlepy.org/docs/dev/recipes.html#using-bottle-with-heroku)をそのまま流用


import os
from bottle import route, run


@route("/")
def hello_world():
    return "" # ここで返す内容は何でもいい。

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
