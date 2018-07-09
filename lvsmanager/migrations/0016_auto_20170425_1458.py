# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-25 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lvsmanager', '0015_server_info_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='server_info',
            name='server_groupname',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='vip_info',
            name='vip_mode',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='vip_ip',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='vip_port',
            field=models.CharField(max_length=64),
        ),
    ]