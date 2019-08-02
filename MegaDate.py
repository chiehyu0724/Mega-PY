import datetime
import time

def GetToday( ):
    # 取得今天日期
    today = datetime.date.today()
    year = str(int(today.strftime('%Y')))
    month = str(int(today.strftime('%m')))
    day = str(int(today.strftime('%d')))
    today = year + '-' + month + '-' + day

    return today

def GetTime( ):
    mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
    return mtime