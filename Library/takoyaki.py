# coding: utf-8

import csv
import random
import os
from datetime import datetime


class Takoyaki:

    def __init__(self, tweet_type):

        # tweet_type = 0: 通常の定期ツイ, 1: テスト, 2: リプ
        self.tweet_type = tweet_type

        self.toppings = {}
        self.ingredients = {}

        self.takoyaki_num = self.ingredients_num = 0
        self.choose_ingredients = self.choose_topping = []

        self.price = self.calories = 0

        # 味の種類の割合
        self.taste_rate = {"Plane": 5, "Sweet": 1}
        self.taste = []
        self.taste_message = {"Sweet": "甘味たこ焼きです。"}

        # 買えなかった理由
        self.reasons = []

        # たこ焼きを買う個数
        self.takoyaki_set = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 57, 59]

        # 時刻ごとのメッセージ
        self.time_name = {4: "早朝", 8: "モーニング", 12: "ランチ", 16: "遅めのおやつ", 
                          20: "ディナー", 0: "深夜"}
        
        self.time_messages = {}

        # リプのメッセージ
        self.reply_data = []


    def information_load(self):

        current_path = os.getcwd()
        next_path = os.path.join(current_path, "Library")
        os.chdir(next_path)

        with open("./Data/plane_toppings.csv", "r") as f:
            data = csv.reader(f)
            self.toppings["Plane"] = []
            for line in data:
                self.toppings["Plane"].append(line)

        with open("./Data/plane_ingredients.csv", "r") as f:
            data = csv.reader(f)
            self.ingredients["Plane"] = []
            for line in data:
                self.ingredients["Plane"].append(line)

        with open("./Data/sweet_toppings.csv", "r") as f:
            data = csv.reader(f)
            self.toppings["Sweet"] = []
            for line in data:
                self.toppings["Sweet"].append(line)

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

        os.chdir(current_path)


    def set_taste(self):

        for taste_name, taste_num in self.taste_rate.items():
            tmp = [taste_name for i in range(taste_num)]
            self.taste.extend(tmp)

        print(self.taste)


    def choose_order(self):

        self.set_taste()

        # たこ焼きを買う個数
        self.takoyaki_num = random.choice(self.takoyaki_set)
        # 具の種類数。1~3個
        self.ingredients_num = random.randrange(3) + 1
        # 味の種類
        self.choose_taste = random.choice(self.taste)

        print(self.choose_taste)
        self.choose_ingredients = random.sample(self.ingredients[self.choose_taste], self.ingredients_num)
        self.choose_topping = random.choice(self.toppings[self.choose_taste])


    def calculate(self):

        # 値段とカロリーの計算
        # 15円と30キロカロリーはたこ焼きのタネの分
        self.price, self.calories = 15, 30

        for i in range(self.ingredients_num):
            self.price += int(self.choose_ingredients[i][1])
            self.calories += int(self.choose_ingredients[i][2])

        self.price += int(self.choose_topping[1])
        self.calories += int(self.choose_topping[2])

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

        if self.choose_taste in self.taste_message.keys():
            res += self.taste_message[self.choose_taste] + "\n\n"

        res += "{}個のご注文ですね。\n\n".format(str(self.takoyaki_num)) 

        res += "具材は"

        for i in range(self.ingredients_num):
            res += self.choose_ingredients[i][0]
            if i == self.ingredients_num - 1:
                res += "で、" # 最後の1個
            else:
                res += "と" # まだ続きがある

        res += "味付けは{}です。\n\n".format(self.choose_topping[0])
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
