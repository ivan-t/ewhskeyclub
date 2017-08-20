# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 02:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]