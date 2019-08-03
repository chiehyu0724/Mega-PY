import MegaLogger
import smtplib
from email.mime.text import MIMEText
#import socks


def SendMail( Subject, Content, ToUser ):
    gmail_user = 'pickman8992@gmail.com'
    gmail_password = 'Starcraft2'

    #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '10.160.3.88', 8080)
    #socks.wrap_module(smtplib)

    msg = MIMEText(Content)
    msg['Subject'] = Subject
    msg['From'] = gmail_user
    msg['To'] = ToUser

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.send_message(msg);
        # 利用sendmail 這個method 來寄出電郵，SMTP.sendmail(from_addr, to_addrs, msg, mail_options=[], rcpt_options=[])
        server.quit()  # 關閉本地端對遠端郵件伺服器的連線

        MegaLogger.Write('Email sent...')
    except:
        MegaLogger.Write('Something went wrong...')