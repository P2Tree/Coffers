# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import XuexiRecord

class XuexiRecordAdmin(admin.ModelAdmin):
    list_display = ('record_date', 'is_complete')

admin.site.register(XuexiRecord, XuexiRecordAdmin)
