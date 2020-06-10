# -*- encoding: utf-8 -*-
import sqlite3
from datetime import datetime, timedelta
from sending_mail import SendingMail as SM

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
    sm = SM()
    sm.send_mail_from_script()
    return False

if __name__ == "__main__":
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    daily_check(c)
    conn.close()


