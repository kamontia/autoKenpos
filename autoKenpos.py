import os
import time
import datetime
import sys
import random
from pyvirtualdisplay import Display
from selenium import webdriver

def Init():
    print("Initialization...")
    global g_pass, g_id, g_max, g_min
    global display,browser, url, DRIVER_PATH, date, RandNum
    display = Display(visible=0,size=(800,600))
    display.start()
    browser = webdriver.Firefox()
    #DRIVER_PATH =os.path.join('/home/kamo/autoKenpos/chromedriver') 
    #print DRIVER_PATH
    #browser = webdriver.Chrome(DRIVER_PATH)
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
    print("Login...")
    url = "https://www.kenpos.jp/member/login"
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="authKenpos2012_login_id"]').send_keys(g_id)
    browser.find_element_by_xpath('//*[@id="authKenpos2012_password"]').send_keys(g_pass)
    browser.find_element_by_xpath('//*[@id="Center"]/div[3]/div/div[2]/form/button').click()

def Steps():
    print("Stepping...")
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

def Lifes():
    print("lifing...")
    try:
        url = "http://www.kenpos.jp/healthAction/statusInput"
        browser.get(url)
        browser.find_element_by_xpath('//*[@id="healthAction_1"]/a[1]/img').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="healthAction_2"]/a[1]/img').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="healthAction_59"]/a[1]/img').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="healthAction_72"]/a[1]/img').click()
        time.sleep(1)
    except Exception as e:
        ErrorCatch(e)



def ErrorCatch(e):
    print("type:{0}".format(type(e)))
    print("args:{0}".format(e.args))
    print("message:{0}".format(e.message))
    print("{0}".format(e))

if __name__ == '__main__':
    OptParse()
    Init()
    Login()
    Steps()
    Lifes()
    browser.quit()
    display.stop()
    print("Complete")


