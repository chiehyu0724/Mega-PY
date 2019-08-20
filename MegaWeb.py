from bs4 import BeautifulSoup
import requests
import urllib.request
import MegaLogger
import time
import os
import MegaDate
import lxml
import shutil
import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd
import pickle
import pyautogui

MegaLogger.Init()

def GetWeb():
    r = requests.get("http://www06.eyny.com/thread-12125929-1-3W0P8JX0.html", auth=('zjyu0724', 'diablo111'))
    
    soup = BeautifulSoup(r.text, 'html.parser')
    MegaLogger.Write( soup.prettify() )

def GetImg( Driver, IMG_URL ):

    WorkDir = os.getcwd()

    folder_name = "MegaPic"
    if not os.path.exists( folder_name ):
        os.makedirs( folder_name )
    today = MegaDate.GetToday()
    folder_path = folder_name + "\\" + folder_name + "-" + today + "\\"
    if not os.path.exists( folder_path ):
        os.makedirs( folder_path )

    # html = requests.get(item.get('src')) # use 'get' to get photo link path , requests = send request
    img_name = WorkDir + '\\' + folder_path + 'aimg.jpg'
    print(img_name)


    # Obtain session id from Selenium cookies
    # cookies = {
    #     'sessionhash': Driver.get_cookie('sessionhash'),
    # }
    # cookies = Driver.get_cookies()
    # s = requests.session()
    # c = requests.cookies.RequestsCookieJar()
    # for item in cookies:
    #     c.set(item["name"], item["value"])
    # s.cookies.update(c)

    # User agent must match user agent used to create session
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    # }
    # r = s.get(IMG_URL, headers=headers)

    # 保存 Cookies
    pickle.dump( Driver.get_cookies(), open("cookies.pkl", "wb"))

    # 载入 Cookies
    Driver.get(IMG_URL)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.press('shift')
    pyautogui.typewrite(img_name)
    pyautogui.hotkey('enter')
    # cookies = pickle.load(open("cookies.pkl", "rb"))
    #
    # s = requests.Session()
    # for cookie in cookies:
    #     s.cookies.set(cookie['name'], cookie['value'])
    # r = s.get(IMG_URL)
    # bodyStr = r.text

    # r = requests.get(item.get('src'), stream=True, headers={'User-agent': 'Mozilla/5.0'})
    # r = requests.get(IMG_URL, stream=True, auth=('zjyu0724', 'Starcraft2'))
    # print("IMG_URL=" + IMG_URL)
    # print(r.status_code)
    # if r.status_code == 200:
    #     with open(img_name, 'wb') as f:
    #         r.raw.decode_content = True
    #         shutil.copyfileobj(r.raw, f)


    time.sleep(1)
# print(soup.prettify())

def LoginWeb():


    USER = 'zjyu0724'
    PASSWORD = 'Starcraft2'
    LOGIN_URL = 'http://www06.eyny.com/member.php?mod=logging&action=login'

    driver = webdriver.Chrome('./chromedriver')
    driver.get(LOGIN_URL)
    elem = driver.find_element_by_name('username')
    elem.clear()
    elem.send_keys(USER)
    password = driver.find_element_by_name('password')
    password.clear()
    password.send_keys(PASSWORD)
    elem.submit()
    # print(driver.page_source)
    # time.sleep(10)
    MegaLogger.Write("登入完成")

    # driver.get('http://www06.eyny.com/forum-205-3W0P8JX0.html')
    driver.get('http://www06.eyny.com/thread-12125929-1-3W0P8JX0.html')

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    MegaLogger.Write(soup.prettify())

    dfs = pd.read_html(soup.prettify())
    print( len(dfs) )


    imgtags = soup.find_all(id=re.compile("aimg_*"))
    print(imgtags[0].get('file'))
    GetImg(driver, imgtags[0].get('file'))
    driver.close

    time.sleep(5)
    # session_requests = requests.session()
    # result = session_requests.get(LOGIN_URL)
    # tree = html.fromstring(result.text)
    # authenticity_token = list(set(tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')))[0]


LoginWeb()
# GetWeb()

MegaLogger.Close()
