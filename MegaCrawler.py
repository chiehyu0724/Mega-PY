import MegaLogger
import pandas as pd
import re
import MegaDate
#import requests
from io import StringIO
import time

global gURLHead
global gURLTail
global gURLList
gURLHead = "http://www03.eyny.com/forum-205-"
gURLTail = ".html"
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
            "7L1GLMYY",
            "2E1N3F54",
            "HMFDIE74",
            "3DN3FGJR",
            "5QIKYKU2"]


def GetEynyWeb( ):
    global gURLHead
    global gURLTail
    global gURLList


    for i in range(len(gURLList)):
        url = gURLHead + gURLList[i] + gURLTail
        MegaLogger.Write(url)
        # 取得網頁內容置入dataframes
        dfs = pd.read_html(url)
        MegaLogger.Write("table num : " + str(len(dfs)))
        # 取得電影列table, table數量會變化，電影列table為最後一個，故以dfs長度做判斷
        df = dfs[len(dfs)-1]
        # 去掉第一列NaN
        df = df.drop(0)

        # print("df.shape ===== ")
        # print(df.shape)
        # print("df.describe() ===== ")
        # print(df.describe())
        # print("df.head() ===== ")
        # print(df.head())
        # print("df.tail() ===== ")
        # print(df.tail())
        # print("df.columns ===== ")
        # print(df.columns)
        # print("df.index ===== ")
        # print(df.index)
        # print("df.info() ===== ")
        # print(df.info())
        # print(df)

        # print(df.iloc[:,3])
        # print(df.iloc[1, 3])
        match = re.search(r'201.-*',df.iloc[1,3])
        # print(match)
        datestr = match.string[match.start(0)::1]
        MegaLogger.Write( datestr )
        today = MegaDate.GetToday()

        if ( datestr == today ) :
            MegaLogger.Write("datestr = today")
        else :
            MegaLogger.Write("datestr != today")

    # 偽停頓
    # time.sleep(5)

    return


# GetEynyWeb()