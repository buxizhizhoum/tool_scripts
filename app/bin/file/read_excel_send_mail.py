#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import json
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from prettytable import PrettyTable

import pandas as pd
reload(sys)
sys.setdefaultencoding('utf8')


filename = "/home/buxizhizhoum/Downloads/工资表模板.xlsx"


class MailSender(object):
    """class used to send mail, smtplib is used"""
    def __init__(self, host, sender, password, port=None):
        """
        initializing
        :param host: smtp server
        :param sender: sender
        :param password: password, password or authentication code of client
        """
        self.host = host
        self.port = port if port is not None else 25
        self.sender = sender
        self.password = password

    def send_mail(self, receiver, subject, msg):
        """
        function used to send mail
        :param receiver: "abc@126.com"
        :param subject: subject
        :param msg: content
        """
        # 3rd party SMTP service
        mail_host = self.host  # server
        mail_user = self.sender  # username
        mail_pass = self.password  # password

        # mail box of sender
        sender = str(self.sender)

        # content
        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        # TODO 这里还有一个乱码问题
        print repr(json.dumps(receiver))
        message['To'] = Header(receiver)
        # subject
        subject = subject
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 is the SMTP port
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receiver, message.as_string())
            smtpObj.close()
            print "mail has been send successfully!"
        except smtplib.SMTPException as e:
            print "Error: could not send the mail"
            raise e


def read_excel(filename):
    df = pd.read_excel(filename)

    columns = df.iloc[0]
    data = df.iloc[1:]  # remove first line
    data.columns = columns
    # print(data)
    return data, columns


def main():
    now = datetime.datetime.now()
    month = now.month
    subject = "%s月工资单" % month

    data, columns = read_excel(filename)
    for index in range(0, data.shape[0]):
        table = PrettyTable(list(columns))

        row = data.iloc[index]

        mail_box = row[-1]
        table.add_row(row)
        print table

        # print mail_box
        mail_sender.send_mail(mail_box, subject, str(table))


# def main():
#     now = datetime.datetime.now()
#     month = now.month
#     subject = "%s月工资单" % month
#
#     data, columns = read_excel(filename)
#     for index in range(0, data.shape[0]):
#         row = data.iloc[index]
#
#         mail_box = row[-1]
#         table = make_table(columns, row)
#         print table
#
#         # print mail_box
#         mail_sender.send_mail(mail_box, subject, str(table))


# def make_table(columns, row):
#     table = PrettyTable(["项目", "值"])
#     for col, value in zip(columns, row):
#         table.add_row([col, value])
#
#     return table

# def make_table(columns, row):
#     table = ""
#     for col, value in zip(columns, row):
#         line = "%s\t: %s\n" % (col, value)
#         table += line
#
#     return table


if __name__ == "__main__":
    mail_sender = MailSender(
        host="smtp.126.com",
        sender="test@126.com",
        password="test")

    main()


