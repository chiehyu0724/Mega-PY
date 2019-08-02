import MegaDate

global gLogFile
def Init( ):
    today = MegaDate.GetToday()
    global gLogFile
    gLogFile = open( "MegaLog/MegaLog-" + today + ".txt", "w" )
    return

def Write( Str ):
    global gLogFile
    gLogFile.write( MegaDate.GetTime() + " : " + Str + "\n")
    return

def Close( ):
    global gLogFile
    gLogFile.close()
    return
