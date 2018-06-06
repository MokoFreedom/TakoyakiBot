# coding: utf-8

import os
from os.path import join, dirname
from dotenv import load_dotenv


# settings.py の相対パスを取得し、.env ファイルを指定
dotenv_path = join(dirname(__file__), ".env")
# パスを元にファイルの中身を読み取る
load_dotenv(dotenv_path)

# 環境変数を取得し代入
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

