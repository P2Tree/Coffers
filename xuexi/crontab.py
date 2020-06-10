# -*- encoding: utf-8 -*-
import sqlite3
from datetime import datetime, timedelta

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 本文件不属于 Coffers Django 后台的一部分
# 因为目前预备部署在 pythonanywhere 上，但免费账户限制比较多
# 主要受影响的功能有：
# 1. SMTP 服务只支持 GMAIL
# 2. 不支持自己配置的日程，比如 crontab, apscheduler
#    平台提供了一个免费的 task 接口，但无法直接和 Django 对接
#
# 为了和 Coffers Django 能正确对接，并且还能实现日程功能
# 使用平台的 task 接口调用该文件，并检查数据库
# Coffers Django 签到接口继续保留


def daily_check(c):
    utcnow = datetime.utcnow()
    now = utcnow + timedelta(hours=8)
    today = now.date()
    print(today)

    cursor = c.execute("select is_complete from xuexi_xuexirecord where record_date = \"" + str(today) + "\"")
    #  cursor = c.execute("select is_complete, record_date from xuexi_xuexirecord")
    for row in cursor:
        if row[0] == 1:
            return True

    send_mail()
    return False

def send_mail():
    mail_host = "smtp.gmail.com"
    mail_user =
    mail_pass =

    sender = 'dicksonliuming@gmail.com'
    receivers = ['ylm1205@163.com']

    message = MIMEText('今天的学习强国完成了吗？ 完成请忽略。\n这是一封自动发送的邮件，请勿回复。', 'plain', 'utf-8')
    message['From'] = Header("学习强国引导助手", 'utf-8')

    subject = '今天的学习强国完成了吗'
    message['Subject'] = Header(subject, 'utf-8')

    server = smtplib.SMTP(mail_host, 25)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(mail_user, mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    server.quit()
    #  smtpObj = smtplib.SMTP()
    #  smtpObj.connect(mail_host, 587)
    #  smtpObj.login(mail_user, mail_pass)
    #  smtpObj.sendmail(sender, receivers, message.as_string())


if __name__ == "__main__":
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    daily_check(c)
    conn.close()


