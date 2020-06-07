# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.
class Ask(models.Model):
    question = models.TextField(u'问题')
    answer = models.TextField(u'回答')
    created_date = models.DateTimeField(u'创建时间', default=timezone.now)

    def __str__(self):
        return self.question
