import configparser
import sys
import os
from collections import defaultdict

import pysnooper

'''
外部ファイルからパラメータを取得する
 USERID:    PepUpのログインID
 PASSWORD:  PepUpのログインパスワード

 [歩数情報]
 MIN_STEP〜MAX_STEPの範囲でランダムで値を決定する
 MAX_STEP:  最大歩数
 MIN_STEP:  最小歩数

 [睡眠情報]
 MIN_SLEEP_HOUR〜MAX_SLEEP_HOURの範囲でランダムで値を決定する
 MAX_SLEEP_HOUR: 最大睡眠時間
 MIN_SLEEP_HOUR: 最小睡眠時間

'''


class Parser(object):
    def __init__(self):
        self.config = defaultdict(list)

    def parse(self):
        parse = configparser.ConfigParser()
        try:
            parse.read("./config.ini")
        except FileNotFoundError as e:
            print(e)

        self.setParameter("USERID",
                          parse["ACCOUNT"]["USERID"][1:-1])
        self.setParameter("PASSWORD",
                          parse["ACCOUNT"]["PASSWORD"][1:-1])
        self.setParameter("MAX_STEP", int(
            parse["PARAMETER"]["MAX_STEP"]))
        self.setParameter("MIN_STEP", int(
            parse["PARAMETER"]["MIN_STEP"]))
        self.setParameter("MAX_SLEEP_HOUR",
                          float(parse["PARAMETER"]["MAX_SLEEP_HOUR"]))
        self.setParameter("MIN_SLEEP_HOUR",
                          float(parse["PARAMETER"]["MIN_SLEEP_HOUR"]))

    def getParameter(self, key):
        return self.config[key]

    def setParameter(self, key, value):
        self.config[key] = value

    def display(self):
        for k in self.config:
            print(k, '=>', self.config[k])


if __name__ == '__main__':

    parser = Parser()
    parser.parse(parser)
    parser.display()
