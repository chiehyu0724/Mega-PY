import MegaLogger
import pandas as pd
import re
import MegaDate
import numpy as np

#import requests
from io import StringIO
import time

global gURLHead
global gURLTail
global gURLList
gURLHead = "http://www03.eyny.com/forum-205-"
gURLTail = ".html"
gURLList = ["3DN3CFFH",
            # "3W0P8JX0",
            # "42RLY2A3",
            # "2PKGH375",
            # "6VVWY3HI",
            # "22HTLHS3",
            # "9FJC8P4V",
            # "2JSJRQNM",
            # "C9NN8QCB",
            # "22HTMFFX",
            # "7L1GLMYY",
            # "2E1N3F54",
            # "HMFDIE74",
            # "3DN3FGJR",
            # "5QIKYKU2",
            # "5WAHP375",
            # "2PKGK4BF",
            # "8QESP4EK",
            # "3W0PCIP5",
            # "BA27YQ1X"
            ]

def GetEynyWeb( ):
    global gURLHead
    global gURLTail
    global gURLList
    MatchList = []
    #urlidx=0
    for urlidx in range(len(gURLList)):
        url = gURLHead + gURLList[urlidx] + gURLTail
        MegaLogger.Write("\n\n\n PAGE" + str(urlidx+1))
        MegaLogger.Write(url + "===========================")
        # 取得網頁內容置入dataframes
        dfs = pd.read_html(url)
        MegaLogger.Write("table num : " + str(len(dfs)))
        # 取得電影列table, table數量會變化，電影列table為最後一個，故以dfs長度做判斷
        if ( len(dfs) > 12 ):
            df = dfs[len(dfs) - 2]
        else:
            df = dfs[len(dfs) - 1]
        # 去掉第一列NaN
        df = df.drop(0)


        # print("df.shape ===== ")
        # print(df.shape)
        # print("df.describe() ===== ")
        # print(df.describe())
        # MegaLogger.Write("df.head() ===== ")
        # MegaLogger.Write(str(df.head()))
        # print("df.tail() ===== ")
        # print(df.tail())
        # print("df.columns ===== ")
        # print(df.columns)
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
                        # MegaLogger.Write("datestr = today")
                        MegaLogger.Write( "Movie Str =" + str(df.iloc[tableidx, 2]) )
                        MatchList.append(df.iloc[tableidx,2])
                    else :
                        # MegaLogger.Write("datestr != today")
                        MegaLogger.Write( "Not Movie Str =" + str(df.iloc[tableidx, 2]) )

        time.sleep(5)


    MegaLogger.Write( "\n\n\n" )
    for i in range(len(MatchList)):
         MegaLogger.Write( "Match Movie : " + MatchList[i] )

    return MatchList


# GetEynyWeb()