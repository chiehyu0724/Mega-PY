import MegaLogger
import MegaCrawler
import MegaMail

def main( ):
    MegaLogger.Init()
    MegaLogger.Write("=== Game Start ===")

    MatchList = MegaCrawler.GetEynyWeb()
    Content = ""
    for i in range(len(MatchList)):
        Content = Content + MatchList[i] + "\n"
    print(Content)
    #if (len(MatchList) != 0):
    #    MegaMail.SendMail( "[Mega-PY]!!! 伊莉有新的電影了，快去看看 !!!", Content, "zjyu0724@gmail.com" )


    MegaLogger.Close()
    return 0

main()


