# encoding=utf-8
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class Email:

    def send(self, attchment_file_name, fromaddr, password, toaddrs):

        # 发送文字
        content = 'hello, please enjoy it!.'
        textApart = MIMEText(content)


        # 发送压缩包附件
        zipFile = attchment_file_name
        zipApart = MIMEApplication(open(zipFile, 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

        m = MIMEMultipart()
        m.attach(textApart)
        m.attach(zipApart)
        m['Subject'] = attchment_file_name

        try:
            server = smtplib.SMTP('smtp.163.com')
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddrs, m.as_string())
            print('send email success')
            server.quit()
        except smtplib.SMTPException as e:
            print('error:', e)
