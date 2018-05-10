# coding: utf-8
import csv
import random
from datetime import datetime

class Takoyaki:

    def __init__(self):

        self.toppings = []
        self.ingredients = []
        self.reasons = ["お金が足りませんでした。", "ダイエット中なのでたこ焼きを控えることにしました。",
                        "買い忘れてしまいました。", "寿司に浮気してしまいました。"]
        self.takoyaki_set = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 57, 59]

        self.time_data = {4: ["早朝", "早く寝ましょう。"],
                          8: ["モーニング", "おはようございます。"],
                          12: ["ランチ", "眠くならない程度に食べましょう。"],
                          16: ["遅めのおやつ", "おやつだおやつだー"],
                          20: ["ディナー", "1日お疲れ様でした。"],
                          0: ["深夜", "たこ焼きは美味しいので深夜に食べても大丈夫です。"]}

    def infomation_load(self):

        with open("toppings.csv", "r") as f:
            data = csv.reader(f)
            for line in data:
                self.toppings.append(line)

        with open("ingredients.csv", "r") as f:
            data = csv.reader(f)
            for line in data:
                self.ingredients.append(line)

    def choose_order(self):

        takoyaki_num = random.randrange(20)
        ingredients_num = random.randrange(3) + 1
        choose_ingredients = random.sample(self.ingredients, ingredients_num)
        choose_topping = random.sample(self.toppings, 1)

        return takoyaki_num, ingredients_num, choose_ingredients, choose_topping

    def nyan(self):

        self.infomation_load()

        takoyaki_num, ingredients_num, choose_ingredients, choose_topping = self.choose_order()

        if takoyaki_num == 0:
            return random.sample(self.reasons, 1)

        price, calories = 15, 30
        for i in range(ingredients_num):
            price += int(choose_ingredients[i][1])
            calories += int(choose_ingredients[i][2])

        price *= takoyaki_num
        calories *= takoyaki_num

        price += int(choose_topping[0][1])
        calories += int(choose_topping[0][2])

        now_time = datetime.now().hour

        if now_time in self.time_data:
            res = self.time_data[now_time][0] + "のたこ焼きです。\n\n"
        else:
            res = "テスト\n\n"

        res += str(takoyaki_num) + "個注文しました。\n\n"
        res += "具材: "

        for i in range(ingredients_num):
            res += choose_ingredients[i][0]
            if i == ingredients_num - 1:
                res += "\n"
            else:
                res += " "

        res += "味  : " + choose_topping[0][0] + "\n\n"
        res += str(price) + "円でした。\n"
        res += "合計" + str(calories) + "カロリーです\n\n"

        if now_time in self.time_data:
            res += self.time_data[now_time][1]
        else:
            res += "テスト成功"

        return res
