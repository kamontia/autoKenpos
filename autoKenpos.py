import os
import time
import datetime
import sys
import random
from pyvirtualdisplay import Display
from selenium import webdriver
from configparser import ConfigParser
import pysnooper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions


def Init():
    global g_pass, g_id, g_max, g_min
    global display, browser, url, DRIVER_PATH, date, RandNum, do_List
    # chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument('--headless')
    # chromeOptions.add_argument('--no-sandbox')
    # chromeOptions.add_argument('--disable-dev-shm-usage')

    # browser = webdriver.Chrome(
    # '/usr/local/bin/chromedriver', chrome_options=chromeOptions)

    FirefoxOptions = webdriver.FirefoxOptions()
    # FirefoxOptions.add_argument('--headless')
    FirefoxOptions.add_argument('--no-sandbox')
    FirefoxOptions.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Firefox(
        firefox_options=FirefoxOptions)

    # browser = webdriver.Firefox()
    date = datetime.date.today()
    date.strftime('%y-%m-%d')
    date = str(date)


def OptParse():
    global usage
    usage = 'Usage: python {} FILE [--verbose] [--cat <file>] [--help]'\
            .format(__file__)

    arguments = sys.argv
    if len(arguments) == 1:
        return usage

    arguments.pop(0)
    options = [option for option in arguments if option.startswith('-')]

    if '-h' in options:
        return usage
    if '-id' in options:
        cat_position = arguments.index('-id')
        global g_id
        g_id = arguments[cat_position + 1]
    if '-pass' in options:
        cat_position = arguments.index('-pass')
        global g_pass
        g_pass = arguments[cat_position + 1]
    if '-g_min' in options:
        cat_position = arguments.index('-g_min')
        global g_min
        g_min = arguments[cat_position + 1]
        g_min = int(g_min)
    if '-g_max' in options:
        cat_position = arguments.index('-g_max')
        global g_max
        g_max = arguments[cat_position + 1]
        g_max = int(g_max)


@pysnooper.snoop()
def Login():
    url = "https://pepup.life/users/sign_in"
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="sender-email"]').send_keys(g_id)  # nopep8
    browser.find_element_by_xpath('//*[@id="user-pass"]').send_keys(g_pass)  # nopep8

    print(browser.find_element_by_xpath(
        '//*[@id="sender-email"]').get_attribute('value'))
    print(browser.find_element_by_xpath(
        '//*[@id="user-pass"]').get_attribute('value'))
    browser.find_element_by_xpath('//*[@id="new_user"]/div[2]/div[3]/input').click()  # nopep8

    browser.get('https://pepup.life/scsk_mileage_campaigns')

    print("---CLICK---")
    # browser.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]')
    # print(browser.page_source)

    # print(browser.page_source)

    '''
    1.特定のクラス(クリック可能、入力済みでない)を検索
    2.該当のクラスの要素がクリック可能になるまで待つ
    3.モーダルウインドウに歩数を入力する
    4.記録ボタンをクリックする
    # .次の要素を探して1.~4.を繰り返す
    '''
    # STEP_XPATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]//*[contains(@class, "kpAgVi")]'

    # while True:
    #     isFound = browser.find_element_by_xpath(STEP_XPATH)
    #     print(isFound.text)
    #     if isFound:
    #         isFound.click()
    #         isFound.find_element_by_xpath(
    #             '/html/body/div[4]/div[2]/div[2]/form/input').clear()
    #         isFound.find_element_by_xpath(
    #             '/html/body/div[4]/div[2]/div[2]/form/input').send_keys('20000')
    #         isFound.find_element_by_xpath(
    #             '/html/body/div[4]/div[2]/div[2]/form/div/button[1]').click()
    #         browser.implicitly_wait(5)
    #     else:
    #         break

    SLEEPTIME_PATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div[2]//*[contains(@class,"kpAgVi")]'

    while True:
        try:
            isFound = browser.find_element_by_xpath(SLEEPTIME_PATH)
        except exceptions.NoSuchElementException:
            break

        if isFound:
            isFound.click()
            isFound.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[2]/form/input').clear()
            isFound.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[2]/form/input').send_keys('6.5')
            isFound.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[2]/form/div/button[1]').click()
            browser.implicitly_wait(5)
        else:
            break

    SLEEPCHECK_PATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[2]//*[contains(@class,"kpAgVi")]'
    while True:
        try:
            isFound = browser.find_element_by_xpath(SLEEPCHECK_PATH)
        except exceptions.NoSuchElementException:
            break
        print(isFound.text)
        if isFound:
            isFound.click()

            if not isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div[3]/div[1]/label/input').is_selected():
                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div[3]/div[1]/label/input').click()

            isFound.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[3]/div[2]/button').click()
            browser.implicitly_wait(5)
        else:
            break

    ALCOHOL_PATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[5]/div[2]/div[1]/div[2]/div[2]//*[contains(@class,"kpAgVi")]'
    while True:
        try:
            isFound = browser.find_element_by_xpath(ALCOHOL_PATH)
        except exceptions.NoSuchElementException:
            break
        print(isFound.text)
        if isFound:
            isFound.click()

            if not isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div[3]/div[1]/label/input').is_selected():
                isFound.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div[3]/div[1]/label/input').click()

            isFound.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[3]/div[2]/button').click()
            browser.implicitly_wait(5)
        else:
            break

    LIFEWORK_PATH = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[6]/div[2]/div[1]/div[2]/div[2]//*[contains(@class,"kpAgVi")]'
    while True:
        try:
            isFound = browser.find_element_by_xpath(LIFEWORK_PATH)
        except exceptions.NoSuchElementException:
            break

        if isFound:
            isFound.click()

            itemsFound = browser.find_elements_by_xpath(
                '/html/body/div[4]/div[2]/div[3]//input[contains(@class,"sc-eXEjpC")]')

            for item in itemsFound:
                print(item)
                if not item.is_selected():
                    item.click()

            isFound.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[3]/div[6]/button').click()
            browser.implicitly_wait(5)
        else:
            break
    # WebDriverWait(browser, 10).until(
    #     By.XPATH, STEP_XPATH)
    # print(browser.find_element_by_xpath(STEP_XPATH))
    # print(type(browser.find_element_by_xpath(STEP_XPATH)))
    # for target_list in browser.find_elements_by_xpath(STEP_XPATH):
    #     # Push day
    #     print(target_list)
    #     print(target_list.text)
    #     if expected_conditions.element_to_be_clickable(target_list):
    #         try:
    #             target_list.click()
    #             browser.find_element_by_xpath(
    #                 '/html/body/div[4]/div[2]/div[2]/form/input').clear()
    #             browser.find_element_by_xpath(
    #                 '/html/body/div[4]/div[2]/div[2]/form/input').send_keys('20000')
    #             browser.find_element_by_xpath(
    #                 '/html/body/div[4]/div[2]/div[2]/form/div/button[1]').click()
    #             # WebDriverWait(browser, 10).until(
    #             #     By.XPATH, STEP_XPATH)
    #             browser.implicitly_wait(10)
    #             time.sleep(3)
    #         except exceptions.StaleElementReferenceException:
    #             pass

    # Seach text area on modal window

    # Validate whether text area is filled or not
    # Input steps

    # Push recode button

def Steps():
    try:
        url = "http://www.kenpos.jp/healthcare/stepCountInput"
        RandNum = random.randint(g_min, g_max)
        RandNum = str(RandNum)
        browser.get(url)

        browser.find_element_by_xpath('//*[@id="health_step_count_' + date + '_value"]').clear()
        browser.find_element_by_xpath('//*[@id="health_step_count_' + date + '_value"]').send_keys(RandNum)
        browser.find_element_by_xpath('//*[@id="input-ui-content-01"]/form/div[2]/input').click()
    except Exception as e:
        ErrorCatch(e)


def Parse():
    try:
        url = "http://www.kenpos.jp/healthAction/statusInput"
        browser.get(url)
                
        elements = browser.find_elements_by_class_name('target')
        elements = browser.find_elements_by_css_selector(".jhover>p")      
        IDs = browser.find_elements_by_css_selector(".jhover")
        for element in elements:
            print(element.text)
            
        for id in IDs:
            print(id.get_attribute("id"))
            browser.find_element_by_xpath('//*[@id="'+ id.get_attribute("id") +'"]/a[1]/img').click()
            time.sleep(1)

    except Exception as e:
         ErrorCatch(e)
            

def Lifes():
    try:
        url = "http://www.kenpos.jp/healthAction/statusInput"
        browser.get(url)
        browser.find_element_by_xpath('//*[@id="healthAction_1"]/a[1]/img').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="healthAction_2"]/a[1]/img').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="healthAction_171"]/a[1]/img').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="healthAction_72"]/a[1]/img').click()
        time.sleep(1)
    except Exception as e:
        ErrorCatch(e)


def ConfigParse():
    parser = ConfigParser(default_section="ACCOUNT")
    with open("./app/config.ini") as inp:
        parser.read_file(inp)

    global g_id, g_pass, g_min, g_max

    g_id = parser["ACCOUNT"]["USERID"]
    g_id = g_id[1:-1]
    g_pass = parser["ACCOUNT"]["PASSWORD"]
    g_pass = g_pass[1:-1]
    g_min = int(parser["PARAMETER"]["MIN_STEP"])
    g_max = int(parser["PARAMETER"]["MAX_STEP"])


def ErrorCatch(e):
    print("type:{0}".format(type(e)))
    print("args:{0}".format(e.args))
    print("message:{0}".format(e.message))
    print("{0}".format(e))


if __name__ == '__main__':
    OptParse()
    Init()
    Login()
    # Parse()
    # Steps()
#     Lifes()
    browser.quit()
    display.stop()

