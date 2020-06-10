# -*- encoding: utf-8 -*-
from settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class SendingMail():
    def __init__(self):
        self.subject = u'今天的学习强国完成了吗'
        self.text = u'今天的学习强国完成了吗？ 完成请忽略。\n这是一封自动发送的邮件，请勿回复。'
        self.sender = 'dicksonliuming@gmail.com'
        self.sender_head = u'学习强国引导助手'
        self.receivers = ['ylm1205@163.com']

    def send_mail_from_django(self):
        send_mail(self.subject, self.text, \
                  self.sender_head + " <" + self.sender + ">",
                  self.receivers)

    def send_mail_from_script(self):
        self.parse_settings()
        sender = 'dicksonliuming@gmail.com'
        receivers = ['ylm1205@163.com']

        text = MIMEText(self.text, 'plain', 'utf-8')
        text['From'] = Header(self.sender_head, 'utf-8')
        text['Subject'] = Header(self.subject, 'utf-8')

        server = smtplib.SMTP(self.host, self.port)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(self.user, self.pawd)
        server.sendmail(self.sender, self.receivers, text.as_string())
        server.quit()

    def parse_settings(self):
        self.host = EMAIL_HOST
        self.port = EMAIL_PORT
        self.user = EMAIL_HOST_USER
        self.pawd = EMAIL_HOST_PASSWORD
