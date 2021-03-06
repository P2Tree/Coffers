# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-03 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20190303_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('question', models.TextField(primary_key=True, serialize=False, verbose_name='提问')),
                ('answer', models.TextField(blank=True, verbose_name='回答')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='post',
            name='question',
        ),
        migrations.AddField(
            model_name='post',
            name='dialog',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='diary.Dialog'),
            preserve_default=False,
        ),
    ]
