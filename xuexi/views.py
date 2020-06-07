# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import XuexiRecord
import datetime

def qiandao(request, complete):
    today = datetime.date.today()
    records = XuexiRecord.objects.filter(record_date=today)
    if complete != '1' and complete != '0':
        return HttpResponse("参数错误，请输入1或0")
    if not records:
        if complete == '1':
            new_record = XuexiRecord(is_complete=True, record_date=today)
        else:
            new_record = XuexiRecord(is_complete=False, record_date=today)
        new_record.save()
    elif records:
        if complete == '1':
            records.update(is_complete=True, record_date=today)
        else:
            records.update(is_complete=False, record_date=today)
        records[0].save()

    return HttpResponse("签到成功, 状态：" + complete)

def help(request):
    return HttpResponse("请访问子域名 ./xuexi/qiandao")

