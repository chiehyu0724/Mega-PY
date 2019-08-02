import MegaLogger
import MegaCrawler
import MegaMail

def main( ):
    MegaLogger.Init()
    MegaLogger.Write("=== Game Start ===")
    MegaMail.SendMail( "Testmail0802", "TestContent0802", "zjyu0724@gmail.com" )
    #MegaCrawler.GetEynyWeb()

    MegaLogger.Close()
    return 0

main()


