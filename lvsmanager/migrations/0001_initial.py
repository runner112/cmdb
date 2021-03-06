# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-09 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=128)),
                ('pnb', models.CharField(max_length=64)),
                ('wip', models.CharField(max_length=128)),
                ('nip', models.CharField(max_length=128)),
                ('gip', models.CharField(max_length=128)),
                ('role', models.CharField(max_length=64)),
                ('idc', models.CharField(max_length=64)),
                ('online', models.CharField(max_length=32)),
                ('update_time', models.DateField()),
            ],
        ),
    ]
