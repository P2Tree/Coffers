# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# 这个 model 用来保存学习强国的签到信息
class XuexiRecord(models.Model):
    is_complete = models.BooleanField(u'是否完成', default=False)
    record_date = models.DateField(u'签到时间', default=timezone.now)

    def __str__(self):
        if self.is_complete:
            return str(self.record_date) + ' 已签到'
        else:
            return str(self.record_date) + ' 未签到'
