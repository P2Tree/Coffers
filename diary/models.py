# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(u'标题', max_length=50)
    text = models.TextField(u'内容')
    created_date = models.DateTimeField(u'创建时间', default=timezone.now)
    published_date = models.DateTimeField(u'发布时间', blank=True, null=True)
    is_public = models.BooleanField(u'是否公开', default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
