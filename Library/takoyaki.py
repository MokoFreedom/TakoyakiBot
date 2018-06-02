# coding: utf-8

import csv
import random
import os
from datetime import datetime


class Takoyaki:

    def __init__(self, tweet_type):

        # tweet_type = 0: 通常の定期ツイ, 1: テスト, 2: リプ
        self.tweet_type = tweet_type

        # それぞれ、具と味付けのリストをたこ焼きの種類(Plane, Sweet)ごとに持つ。
        # [名前,値段,カロリー] という配列の配列。
        self.taste = {}
        self.ingredients = {}

        # 選んだたこ焼きの数,具の数,具,味付け
        self.takoyaki_num = self.ingredients_num = 0
        self.choose_ingredients = self.choose_taste = []
        self.choose_takoyaki_type = ""

        # たこ焼きの合計価格,合計カロリー
        self.price = self.calories = 0

        # たこ焼きの種類の割合
        self.takoyaki_type_rate = {"Plane": 5, "Sweet": 1}
        # takoyaki_type_rateの割合に応じた配列を生成(ランダムに種類を選ぶため)
        self.takoyaki_type_list = []
        # 種類に応じたメッセージ
        self.takoyaki_type_message = {"Sweet": "甘味たこ焼きです。"}

        # 買えなかった理由
        self.reasons = []

        # たこ焼きを買う個数
        self.takoyaki_set = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 57, 59]

        # 時刻ごとの名前(定期ツイ用)
        self.time_name = {4: "早朝", 8: "モーニング", 12: "ランチ", 16: "遅めのおやつ", 
                          20: "ディナー", 0: "深夜"}
        
        # 時刻ごとのメッセージ(定期ツイ用)
        self.time_messages = {}

        # リプのメッセージ
        self.reply_data = []


    def information_load(self):

        # カレントディレクトリを移動
        # TakoyakiBot -> TakoyakiBot/Library
        current_path = os.getcwd()
        next_path = os.path.join(current_path, "Library")
        os.chdir(next_path)

        with open("./Data/plane_taste.csv", "r") as f:
            data = csv.reader(f)
            self.taste["Plane"] = []
            for line in data:
                self.taste["Plane"].append(line)

        with open("./Data/plane_ingredients.csv", "r") as f:
            data = csv.reader(f)
            self.ingredients["Plane"] = []
            for line in data:
                self.ingredients["Plane"].append(line)

        with open("./Data/sweet_taste.csv", "r") as f:
            data = csv.reader(f)
            self.taste["Sweet"] = []
            for line in data:
                self.taste["Sweet"].append(line)

        with open("./Data/sweet_ingredients.csv", "r") as f:
            data = csv.reader(f)
            self.ingredients["Sweet"] = []
            for line in data:
                self.ingredients["Sweet"].append(line)

        with open("./Data/time_messages.csv", "r") as f:
            data = csv.reader(f)
            for line in data:
                line_time = int(line[0])
                line.pop(0)
                self.time_messages[line_time] = line

        with open("./Data/reply_data.txt", "r") as f:
            self.reply_data = [line.replace("\n", "") for line in f.readlines()]

        with open("./Data/reasons.txt", "r") as f:
            self.reasons = [line.replace("\n", "") for line in f.readlines()]

        # カレントディレクトリを戻す
        os.chdir(current_path)


    def set_takoyaki_type(self):

        # self.takoyaki_type_rate = {"Plane": 3, "Sweet": 2}
        # だったら
        # self.takoyaki_type = ["Plane", "Plane", "Plane", "Sweet", "Sweet"]
        # という配列を生成
        for takoyaki_type_name, takoyaki_type_num in self.takoyaki_type_rate.items():
            tmp = [takoyaki_type_name for i in range(takoyaki_type_num)]
            self.takoyaki_type_list.extend(tmp)


    def choose_order(self):


        self.set_takoyaki_type()

        # たこ焼きを買う個数
        self.takoyaki_num = random.choice(self.takoyaki_set)
        # 具の種類数。1~3個
        self.ingredients_num = random.randrange(3) + 1
        # 味の種類
        self.choose_takoyaki_type = random.choice(self.takoyaki_type_list)

        print(self.choose_takoyaki_type)
        self.choose_ingredients = random.sample(self.ingredients[self.choose_takoyaki_type], self.ingredients_num)
        self.choose_taste = random.choice(self.taste[self.choose_takoyaki_type])


    def calculate(self):

        # 値段とカロリーの計算
        # 15円と30キロカロリーはたこ焼きのタネの分
        self.price, self.calories = 15, 30

        for i in range(self.ingredients_num):
            self.price += int(self.choose_ingredients[i][1])
            self.calories += int(self.choose_ingredients[i][2])

        self.price += int(self.choose_taste[1])
        self.calories += int(self.choose_taste[2])

        self.price *= self.takoyaki_num
        self.calories *= self.takoyaki_num


    def make_tweet(self):

        # ツイートの作成
        if self.tweet_type == 0:
            now_time = int((datetime.utcnow().hour + 9) % 24)
            res = self.time_name[now_time] + "のたこ焼きです。\n\n"
        elif self.tweet_type == 1:
            res = "テスト\n\n"
        else:
            res = "ご注文ありがとうございますたこ。\n\n"

        if self.choose_takoyaki_type in self.takoyaki_type_message.keys():
            res += self.takoyaki_type_message[self.choose_takoyaki_type] + "\n\n"

        res += "{}個のご注文ですね。\n\n".format(str(self.takoyaki_num)) 

        res += "具材は"

        for i in range(self.ingredients_num):
            res += self.choose_ingredients[i][0]
            if i == self.ingredients_num - 1:
                res += "で、" # 最後の1個
            else:
                res += "と" # まだ続きがある

        res += "味付けは{}です。\n\n".format(self.choose_taste[0])
        res += "{}円になります。\n".format(str(self.price))
        res += "合計{}キロカロリーです。\n\n".format(str(self.calories))

        if self.tweet_type == 0:
            res += random.choice(self.time_messages[now_time])
        elif self.tweet_type == 1:
            res += "テスト成功"
        else:
            res += random.choice(self.reply_data) + "\n"
            res += "またのお越しをお待ちしておりますたこ。"

        return res 




    def nyan(self):

        self.information_load()

        self.choose_order()

        # たこ焼きを買わなかった
        if self.takoyaki_num == 0:
            return random.choice(self.reasons)

        self.calculate()

        tweet_text = self.make_tweet()
        
        return tweet_text
