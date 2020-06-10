# -*- encoding: utf-8 -*-
from .models import XuexiRecord
from datetime import datetime, timedelta
import logging
import requests
from sending_mail import SendingMail as SM

logging.basicConfig()

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

    sm = SM()
    sm.send_mail_from_django()
    return False
