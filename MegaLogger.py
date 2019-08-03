import MegaDate
import os

global gLogFile
def Init( ):
    if not os.path.exists( "MegaLog" ):
        os.makedirs( "MegaLog" )

    today = MegaDate.GetToday()
    global gLogFile
    gLogFile = open( "MegaLog/MegaLog-" + today + ".txt", "w", encoding="utf-8" )
    return

def Write( Str ):
    global gLogFile
    gLogFile.write( MegaDate.GetTime() + " : " + Str + "\n")
    return

def Close( ):
    global gLogFile
    gLogFile.close()
    return
