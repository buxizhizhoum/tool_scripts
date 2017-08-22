#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Send mail with smtplib, this need to supply the username and password of a
mailbox

When it is slow to send a mail with the service of linux, and it is not
possible to change the host name of the machine to accelerate it, or there are
other problems when sending mail with mail service on linux this method
may be an alternative solution.
"""
import json
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

reload(sys)
sys.setdefaultencoding('utf8')


class MailSender(object):
    """class used to send mail, smtplib is used"""
    def __init__(self, host, sender, password, port=None):
        """
        initializing
        :param host: smtp server
        :param sender: sender
        :param password: password， password or authentication code of client
        """
        self.host = host
        self.port = port if port is not None else 25
        self.sender = sender
        self.password = password

    def send_mail(self, receivers, subject, msg):
        """
        function used to send mail
        :param receivers: list contain "to", eg：["abc@126.com", "def@126.com"]
        :param subject: subject
        :param msg: content
        """
        # 3rd party SMTP service
        mail_host = self.host  # server
        mail_user = self.sender  # username
        mail_pass = self.password  # password

        # mail box of sender
        sender = str(self.sender)
        # address of receiver
        receivers = receivers

        # content
        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        # TODO 这里还有一个乱码问题
        print repr(json.dumps(receivers))
        # 这样解决了收件人乱码，有意思，居然要拼接字符串
        receivers_str = ",".join(str(item) for item in receivers)
        message['To'] = Header(receivers_str)
        # subject
        subject = subject
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 is the SMTP port
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.close()
            print "mail has been send successfylly!"
        except smtplib.SMTPException as e:
            print "Error: could not send the mail"
            raise e


if __name__ == "__main__":

    receivers = ['abc@126.com', "123@126.com"]

    mail_sender = MailSender(
        host="smtp.126.com",
        sender="username@126.com",
        password="password")
    # send mail
    mail_sender.send_mail(receivers=receivers, subject="test", msg="test_text")
