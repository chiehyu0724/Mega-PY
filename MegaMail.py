import MegaLogger
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def SendMail( Subject, Content, ToUser ):
    gmail_user = 'pickman8992@gmail.com'
    gmail_password = 'Starcraft2'


    msg = MIMEMultipart()
    msg['Subject'] = Subject
    msg['From'] = gmail_user
    msg['To'] = ToUser
    part_text = MIMEText(Content)
    msg.attach(part_text)

    # files = ['MegaPic\\MegaPic-2019-8-28\\aimg_1.jpg','MegaPic\\MegaPic-2019-8-28\\aimg_2.jpg']
    #
    # with open('MegaPic\\MegaPic-2019-8-28\\aimg_1.jpg', 'rb') as f:
    #     # 設定附件的MIME和檔名，這裡是png型別:
    #     mime = MIMEBase('image', 'jpg', filename='tp.jpg')
    #     # 加上必要的頭資訊:
    #     mime.add_header('Content-Disposition', 'attachment', filename='tp.jpg')
    #     mime.add_header('Content-ID', '<0>')
    #     mime.add_header('X-Attachment-Id', '0')
    #     # 把附件的內容讀進來:
    #     mime.set_payload(f.read())
    #     # 用Base64編碼:
    #     encoders.encode_base64(mime)
    #     # 新增到MIMEMultipart:
    #     msg.attach(mime)
    #
    # # 正文顯示附件圖片
    # msg.attach(MIMEText('<html><body>' +
    #                     '<p><img src="cid:0"></p>' +
    #                     '</body></html>', 'html', 'utf-8'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, ToUser, msg.as_string());
        # server.send_message(msg);
        # 利用sendmail 這個method 來寄出電郵，SMTP.sendmail(from_addr, to_addrs, msg, mail_options=[], rcpt_options=[])
        server.quit()  # 關閉本地端對遠端郵件伺服器的連線

        MegaLogger.Write('Email sent...')
    except:
        MegaLogger.Write('Email sent wrong...')