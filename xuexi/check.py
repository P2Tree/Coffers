# -*- encoding: utf-8 -*-
#  from django.core.mail import send_mail
from .models import XuexiRecord
import datetime
import requests

# crontab method
def daily_check():
    # crontab settings can found in settings.py
    check()

def check():
    today = datetime.date.today()
    records = XuexiRecord.objects.filter(record_date=today)
    if records:
        if records[0].is_complete == True:
            return True
    else:
        new_record = XuexiRecord(is_complete=False, record_date=today)
        new_record.save()
    #  send_mail(u'学习强国提醒', u'今天忘记学习强国了！', 'axelylm@163.com', ['ylm1205@163.com'])
    sendmail()

    return False

def sendmail():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox80006fd6dd344a349f7f4b333fe6c088.mailgun.org/messages",
        auth=("api", "3c1cc10fccd132c25d16589d4cde3558-a2b91229-7bbf2d29"),
        data={"from": "学习强国引导助手 <mailgun@sandbox80006fd6dd344a349f7f4b333fe6c088.mailgun.org>",
              "to"  : ["ylm1205@163.com"],
              "subject": "[ 今天学习强国完成了吗]",
              "text": "请检查今天的学习强国是否完成，完成请忽略本邮件。\n这是一封自动发送的邮件。"
             }
        )
