# -*- encoding: utf-8 -*-
from django.core.mail import send_mail
from .models import XuexiRecord
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
import logging
import requests

logging.basicConfig()

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')

@register_job(scheduler, 'cron', id='daily_check', hour=23, minute=10)
def daily_check():
    check()

register_events(scheduler)
scheduler.start()

def check():
    utcnow = datetime.utcnow()
    now = utcnow + timedelta(hours=8)
    today = now.date()
    records = XuexiRecord.objects.filter(record_date=today)
    if records:
        if records[0].is_complete == True:
            return True
    else:
        new_record = XuexiRecord(is_complete=False, record_date=today)
        new_record.save()
    send_mail(u'学习强国提醒', u'今天忘记学习强国了！', 'Coffers Reminder <dicksonliuming@gmail.com>', ['ylm1205@163.com'])

    return False
