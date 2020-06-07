# -*- encoding: utf-8 -*-
from django.core.mail import send_mail
from .models import XuexiRecord
import datetime

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
    send_mail(u'学习强国提醒', u'今天忘记学习强国了！', 'axelylm@163.com', ['ylm1205@163.com'])
    return False
