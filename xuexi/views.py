# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .check import check
from .models import XuexiRecord
from datetime import datetime, timedelta

def qiandao(request, complete):
    utcnow = datetime.utcnow()
    now = utcnow + timedelta(hours=8)
    today = now.date()
    records = XuexiRecord.objects.filter(record_date=today)
    ret_str = ""
    if complete != '1' and complete != '0':
        return HttpResponse("参数错误，请输入1或0")
    if not records:
        if complete == '1':
            new_record = XuexiRecord(is_complete=True, record_date=today)
            ret_str = "今日已完成"
        else:
            new_record = XuexiRecord(is_complete=False, record_date=today)
            ret_str = "今日未完成"
        new_record.save()
        return HttpResponse("状态已记录：" + ret_str)
    else:
        if complete == '1':
            records.update(is_complete=True, record_date=today)
            ret_str = "今日已完成"
        else:
            records.update(is_complete=False, record_date=today)
            ret_str = "今日未完成"
        records[0].save()
        return HttpResponse("状态已更新：" + ret_str)

def help(request):
    return HttpResponse("请访问子域名 ./xuexi/qiandao")

def manual_check(request):
    r = check()
    if r:
        return HttpResponse("今日已签到")
    else:
        return HttpResponse("今日未签到，已发送提醒邮件")


