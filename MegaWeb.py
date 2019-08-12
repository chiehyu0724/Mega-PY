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


def LoginWeb():
    MegaLogger.Init()

    USER = 'zjyu0724'
    PASSWORD = 'diablo111'
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
    time.sleep(10)
    MegaLogger.Write("登入完成")

    driver.get('http://www06.eyny.com/forum-205-3W0P8JX0.html')

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    MegaLogger.Write(soup.prettify())
    # driver.close

    # session_requests = requests.session()
    # result = session_requests.get(LOGIN_URL)
    # tree = html.fromstring(result.text)
    # authenticity_token = list(set(tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')))[0]
    MegaLogger.Close()

LoginWeb()

def GetImg():
    url = 'http://www06.eyny.com/forum-205-3W0P8JX0.html'

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')

    MegaLogger.Init()
    MegaLogger.Write(soup.prettify())

    items = soup.find_all("img", class_="p_pre")
    MegaLogger.Write(str(items))

    folder_name = "MegaPic"
    if not os.path.exists( folder_name ):
        os.makedirs( folder_name )
    today = MegaDate.GetToday()
    folder_path = folder_name + "/" + folder_name + "-" + today + "/"
    if not os.path.exists( folder_path ):
        os.makedirs( folder_path )

    for idx, item in enumerate (items):

        if ( idx > 16 and idx < 18 ):

            # html = requests.get(item.get('src')) # use 'get' to get photo link path , requests = send request
            print( item.get('src') )
            img_name = folder_path + str(idx) + '.jpg'
            print(img_name)
            # urllib.request.urlretrieve(str(item.get('src')), str(img_name))

            # r = requests.get(item.get('src'), stream=True, headers={'User-agent': 'Mozilla/5.0'})
            r = requests.get("https://blog.gtwang.org/wp-content/uploads/2018/01/python-beautiful-soup-module-scrape-web-pages-tutorial-20180130-1-816x539.png",
                             stream=True)
            print(r.status_code)
            if r.status_code == 200:
                with open(img_name, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)

            # with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入
            #
            #     file.write(html.content)
            #
            #     file.flush()
            #
            # file.close() #close file

            print('第 %d 張' % (idx + 1))

            time.sleep(1)

            MegaLogger.Close()
# print(soup.prettify())

