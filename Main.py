import MegaLogger
import MegaCrawler
import MegaMail

def main( ):
    MegaLogger.Init()
    MegaLogger.Write("=== Mega-PY Start ===")

    MatchList = MegaCrawler.GetEynyWeb()
    Content = ""
    for i in range(len(MatchList)):
        Content = Content + MatchList[i] + "\n"

    if (len(MatchList) != 0):
        MegaLogger.Write( "Toady Movie List: \n" + Content )
        MegaMail.SendMail( "[Mega-PY]!!! 伊莉有新的電影了，快去看看 !!!", Content, "zjyu0724@gmail.com" )

    MegaLogger.Close()
    return 0

main()


