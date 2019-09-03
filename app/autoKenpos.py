import os
import time
import datetime
import sys
import random

from selenium import webdriver
from configparser import ConfigParser
import pysnooper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

from config.parser import Parser


class autoKenpos(object):

    def __init__(self):
        self.g_pass = ""
        self.g_id = ""
        self.g_max_step = 0
        self.g_min_step = 0
        self.g_min_sleep = 0
        self.g_min_sleep = 0
        # global display, browser, url, DRIVER_PATH, date, RandNum, do_List
        # chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument('--headless')
        # chromeOptions.add_argument('--no-sandbox')
        # chromeOptions.add_argument('--disable-dev-shm-usage')
        # self.browser = webdriver.Chrome(options=chromeOptions)

        # browser = webdriver.Chrome(
        # '/usr/local/bin/chromedriver', chrome_options=chromeOptions)

        FirefoxOptions = webdriver.FirefoxOptions()
        FirefoxOptions.add_argument('--headless')
        FirefoxOptions.add_argument('--no-sandbox')
        FirefoxOptions.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Firefox(
            options=FirefoxOptions)

    def __del__(self):
        self.browser.close()

    @pysnooper.snoop()
    def Login(self):
        url = "https://pepup.life/users/sign_in"
        self.browser.get(url)

        self.browser.find_element_by_xpath('//*[@id="sender-email"]').send_keys(self.g_id)  # nopep8
        self.browser.find_element_by_xpath('//*[@id="user-pass"]').send_keys(self.g_pass)  # nopep8

        print(self.browser.find_element_by_xpath(
            '//*[@id="sender-email"]').get_attribute('value'))
        print(self.browser.find_element_by_xpath(
            '//*[@id="user-pass"]').get_attribute('value'))
        self.browser.find_element_by_xpath('//*[@id="new_user"]/div[2]/div[3]/input').click()  # nopep8

        self.browser.get('https://pepup.life/scsk_mileage_campaigns/')

        # self.browser.find_element_by_xpath(
        #     '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]')
        # print(self.browser.page_source)

        # print(self.browser.page_source)

        '''
        1.特定のクラス(クリック可能、入力済みでない)を検索
        2.該当のクラスの要素がクリック可能になるまで待つ
        3.モーダルウインドウに歩数を入力する
        4.記録ボタンをクリックする
        # .次の要素を探して1.~4.を繰り返す
        '''
        STEP_XPATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]//*[contains(@class, "jwSCmU")]'
        print("STEP START")
        random.random()
        while True:
            try:
                isFound = self.browser.find_element_by_xpath(STEP_XPATH)
            except exceptions.NoSuchElementException:
                break

            if isFound:
                isFound.click()
                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[2]/form/input').clear()
                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[2]/form/input').send_keys(random.randint(self.g_min_step, self.g_max_step))
                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[2]/form/div/button[1]').click()
                self.browser.implicitly_wait(5)
            else:
                break

        SLEEPTIME_PATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div[2]//*[contains(@class,"jwSCmU")]'

        while True:
            SLEEPTIME_RANDOM = random.uniform(
                self.g_min_sleep, self.g_max_sleep)
            SLEEPTIME_RANDOM = round(SLEEPTIME_RANDOM, 1)
            try:
                isFound = self.browser.find_element_by_xpath(SLEEPTIME_PATH)
            except exceptions.NoSuchElementException:
                break

            if isFound:
                isFound.click()
                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[2]/form/input').clear()
                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[2]/form/input').send_keys(str(SLEEPTIME_RANDOM))
                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[2]/form/div/button[1]').click()
                self.browser.implicitly_wait(5)
            else:
                break

        SLEEPCHECK_PATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[2]//*[contains(@class,"jwSCmU")]'
        while True:
            try:
                isFound = self.browser.find_element_by_xpath(SLEEPCHECK_PATH)
            except exceptions.NoSuchElementException:
                break
            print(isFound.text)
            if isFound:
                isFound.click()

                if not isFound.find_element_by_xpath(
                        '/html/body/div[4]/div[3]/div[3]/div[1]/label/input').is_selected():
                    isFound.find_element_by_xpath(
                        '/html/body/div[4]/div[3]/div[3]/div[1]/label/input').click()

                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[3]/div[2]/button').click()
                self.browser.implicitly_wait(5)
            else:
                break

        ALCOHOL_PATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[5]/div[2]/div[1]/div[2]/div[2]//*[contains(@class,"jwSCmU")]'
        while True:
            try:
                isFound = self.browser.find_element_by_xpath(ALCOHOL_PATH)
            except exceptions.NoSuchElementException:
                break
            print(isFound.text)
            if isFound:
                isFound.click()

                if not isFound.find_element_by_xpath(
                        '/html/body/div[4]/div[3]/div[3]/div[1]/label/input').is_selected():
                    isFound.find_element_by_xpath(
                        '/html/body/div[4]/div[3]/div[3]/div[1]/label/input').click()

                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[3]/div[2]/button').click()
                self.browser.implicitly_wait(5)
            else:
                break

        LIFEWORK_PATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[6]/div[2]/div[1]/div[2]/div[2]//*[contains(@class,"jwSCmU")]'
        while True:
            try:
                isFound = self.browser.find_element_by_xpath(LIFEWORK_PATH)
            except exceptions.NoSuchElementException:
                break

            if isFound:
                isFound.click()

                itemsFound = self.browser.find_elements_by_xpath(
                    '/html/body/div[4]/div[3]/div[3]//input[contains(@class,"bwykYp")]')

                for item in itemsFound:
                    print(item)
                    if not item.is_selected():
                        item.click()

                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[3]/div[6]/button').click()
                self.browser.implicitly_wait(5)
            else:
                break

        PLUS10_PATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[7]/div[2]/div[1]/div[2]/div[2]//*[contains(@class,"jwSCmU")]'
        while True:
            try:
                isFound = self.browser.find_element_by_xpath(PLUS10_PATH)
            except exceptions.NoSuchElementException:
                break
            print(isFound.text)
            if isFound:
                isFound.click()

                if not isFound.find_element_by_xpath(
                        '/html/body/div[4]/div[3]/div[3]/div[1]/label/input').is_selected():
                    isFound.find_element_by_xpath(
                        '/html/body/div[4]/div[3]/div[3]/div[1]/label/input').click()

                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[3]/div[3]/div[2]/button').click()
                self.browser.implicitly_wait(5)
            else:
                break

    @pysnooper.snoop()
    def ConfigParse(self):
        parser = Parser()
        parser.parse()
        parser.display()

        self.g_id = parser.getParameter("USERID")
        self.g_pass = parser.getParameter("PASSWORD")

        self.g_max_step = parser.getParameter("MAX_STEP")
        self.g_min_step = parser.getParameter("MIN_STEP")

        self.g_max_sleep = parser.getParameter("MAX_SLEEP_HOUR")
        self.g_min_sleep = parser.getParameter("MIN_SLEEP_HOUR")

    def ErrorCatch(self, e):
        print("type:{0}".format(type(e)))
        print("args:{0}".format(e.args))
        print("message:{0}".format(e.message))
        print("{0}".format(e))


if __name__ == '__main__':
    kenpos = autoKenpos()
    kenpos.ConfigParse()
    kenpos.Login()
