# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-09 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lvsmanager', '0005_auto_20170209_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server_info',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u66f4\u65b0\u65e5\u671f'),
        ),
    ]
