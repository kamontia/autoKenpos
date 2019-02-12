import os
import time
import datetime
import sys
import random
from selenium import webdriver
from configparser import ConfigParser


def Init():
    global g_pass, g_id, g_max, g_min
    global display, browser, url, DRIVER_PATH, date, RandNum, do_List
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome(
        '/usr/local/bin/chromedriver', chrome_options=chromeOptions)
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


def Login():
    url = "https://www.kenpos.jp/member/login"
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="authKenpos2012_login_id"]').send_keys(g_id)  # nopep8
    browser.find_element_by_xpath('//*[@id="authKenpos2012_password"]').send_keys(g_pass)  # nopep8
    browser.find_element_by_xpath('//*[@id="Center"]/div[3]/div/div[2]/form/button').click()  # nopep8


def Steps():
    try:
        url = "http://www.kenpos.jp/healthcare/stepCountInput"

        RandNum = random.randint(g_min, g_max)
        RandNum = str(RandNum)
        browser.get(url)

        browser.find_element_by_xpath('//*[@id="health_step_count_' + date + '_value"]').clear()  # nopep8
        browser.find_element_by_xpath('//*[@id="health_step_count_' + date + '_value"]').send_keys(RandNum)  # nopep8
        browser.find_element_by_xpath('//*[@id="input-ui-content-01"]/form/div[2]/input').click()  # nopep8
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
            browser.find_element_by_xpath(
                '//*[@id="' + id.get_attribute("id") + '"]/a[1]/img').click()
            time.sleep(1)

    except Exception as e:
        ErrorCatch(e)


def Lifes():
    try:
        url = "http://www.kenpos.jp/healthAction/statusInput"
        browser.get(url)
        browser.find_element_by_xpath(
            '//*[@id="healthAction_1"]/a[1]/img').click()
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="healthAction_2"]/a[1]/img').click()
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="healthAction_171"]/a[1]/img').click()
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="healthAction_72"]/a[1]/img').click()
        time.sleep(1)
    except Exception as e:
        ErrorCatch(e)


def ConfigParse():
    parser = ConfigParser(default_section="ACCOUNT")
    with open("./app/config.ini") as inp:
        parser.read_file(inp)

    global g_id, g_pass, g_min, g_max

    g_id = parser["ACCOUNT"]["USERID"]
    g_pass = parser["ACCOUNT"]["PASSWORD"]
    g_min = int(parser["PARAMETER"]["MIN_STEP"])
    g_max = int(parser["PARAMETER"]["MAX_STEP"])


def ErrorCatch(e):
    print("type:{0}".format(type(e)))
    print("args:{0}".format(e.args))
    print("message:{0}".format(e.message))
    print("{0}".format(e))


if __name__ == '__main__':
    ConfigParse()
    # OptParse()
    Init()
    Login()
    Parse()
    Steps()
#     Lifes()
    browser.quit()
