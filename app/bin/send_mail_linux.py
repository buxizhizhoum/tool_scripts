#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
send mail with the service of server instead of register an mailbox to send it.
"""
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
import commands


class MailSender(object):
    def __init__(self):
        pass

    def send_mail(self, sender, recevier, subject, msg):
        msg = MIMEText(msg, 'html', 'utf-8')
        msg["From"] = sender
        msg["To"] = recevier
        msg["Subject"] = subject
        p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
        p.communicate(msg.as_string())

mail_sender = MailSender()
mail_sender.send_mail(
    "sender@126.com",
    "receiver@126.com",
    "topic",
    "content")

print "finished!"
