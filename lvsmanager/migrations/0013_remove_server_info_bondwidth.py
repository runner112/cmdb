# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-05 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lvsmanager', '0012_server_info_bondwidth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server_info',
            name='bondwidth',
        ),
    ]
