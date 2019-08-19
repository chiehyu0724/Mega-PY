import MegaLogger
import pandas as pd
import re
import MegaDate
from bs4 import BeautifulSoup
import time
from selenium import webdriver

global gURLHead
global gURLTail
global gURLList
gURLHead = "http://www03.eyny.com/forum-205-"
gURLTail = ".html"
# 檢查10頁內容
gURLList = ["3DN3CFFH",
            "3W0P8JX0",
            "42RLY2A3",
            "2PKGH375",
            "6VVWY3HI",
            "22HTLHS3",
            "9FJC8P4V",
            "2JSJRQNM",
            "C9NN8QCB",
            "22HTMFFX",
            # "7L1GLMYY",
            # "2E1N3F54",
            # "HMFDIE74",
            # "3DN3FGJR",
            # "5QIKYKU2",
            ]


def TestEynyWeb():
    url = gURLHead + gURLList[1] + gURLTail
    dfs = pd.read_html(url)
    MegaLogger.Write("table num : " + str(len(dfs)))
    # df = dfs[len(dfs)-1]
    df = GetMovieTableDF(dfs)
    # print(df)
    print(len(df.columns))
    print(df.iloc[:, 0])


# 取得電影列table, table數量會變化，故以條件判斷
def GetMovieTableDF(dfs):
    for tableidx in range(len(dfs)):
        df = dfs[tableidx]
        if ( len(df.columns) == 6 ):
            match = re.search(r'201.-*', df.iloc[2,3])
            if ( match is not None ):
                return df
            else:
                continue
        else:
            continue

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
    time.sleep(10)
    MegaLogger.Write("登入完成")

    return driver


def GetEynyWeb( ):
    global gURLHead
    global gURLTail
    global gURLList
    MatchList = []

    driver = LoginWeb()

    for urlidx in range(len(gURLList)):
        url = gURLHead + gURLList[urlidx] + gURLTail
        MegaLogger.Write("\n\n\n PAGE" + str(urlidx+1))
        MegaLogger.Write(url + "===========================")

        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 取得網頁內容置入dataframes
        dfs = pd.read_html(soup.prettify())
        MegaLogger.Write("table num : " + str(len(dfs)))
        # 防止抓不到table意外狀況發生
        if ( len(dfs) < 8 ):
            continue
        df = GetMovieTableDF(dfs)
        # 去掉第一列NaN
        df = df.drop(0)

        # MegaLogger.Write("df.index ===== ")
        # MegaLogger.Write(str(df.index))
        # MegaLogger.Write("df.info() ===== ")
        # MegaLogger.Write(str(df.info()))
        # MegaLogger.Write("df ===== ")
        # MegaLogger.Write(str(df))
        # print(df.iloc[:,3])
        # print(df.iloc[1, 3])
        # MegaLogger.Write( "df.index = " + str(df.index) )

        #tableidx=0
        for tableidx in range(len(df.index)):
            # print(df.iloc[tableidx,3])
            if ( str(df.iloc[tableidx,3]) == 'nan' ):
                 MegaLogger.Write("作者日期 is nan")
                 continue
            else:
                MegaLogger.Write("作者日期 :" + str(df.iloc[tableidx,3]))
                match = re.search(r'201.-*', df.iloc[tableidx,3])
                # print(match)
                if ( match is not None ):
                    datestr = match.string[match.start(0)::1]
                    # MegaLogger.Write( datestr )
                    today = MegaDate.GetToday()

                    if ( datestr == today ) :
                        MegaLogger.Write( "Movie Str =" + str(df.iloc[tableidx, 2]) )
                        MatchList.append(str(df.iloc[tableidx,2])+"\n")
                    else :
                        MegaLogger.Write( "Not Movie Str =" + str(df.iloc[tableidx, 2]) )

        time.sleep(5)


    MegaLogger.Write( "\n\n\n" )
    for i in range(len(MatchList)):
         MegaLogger.Write( "Match Movie : " + MatchList[i] )

    return MatchList


# GetEynyWeb()