# -*- coding: utf8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

#import datetime
# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)

    def __unicode__(self):
        return self.user.username

class Server_info(models.Model):
    server_name = models.CharField(max_length=128,unique=True)
    pnb = models.CharField(max_length=64,unique=True)
    wip = models.CharField(max_length=128)
    nip = models.CharField(max_length=128)
    gip = models.CharField(max_length=128)
    role = models.CharField(max_length=64)
    idc = models.CharField(max_length=64)
    online = models.CharField(max_length=32)
    bondwidth = models.CharField(max_length=32,default="")
    server_groupname = models.CharField(max_length=128,default="")
    mark = models.CharField(max_length=128,default="")
    #update_time = models.DateField('保存日期',default = datetime.datetime.now())
    #update_time = models.DateField()
    update_time = models.DateTimeField(auto_now=True)
    #update_time = models.DateTimeField('更新日期',default = timezone.now)

    class META:
        ordering = ['server_name']

    def __unicode__(self):
        return self.server_name

class Vip_info(models.Model):
    vip_ip = models.CharField(max_length=128,unique=True)
    vip_port = models.CharField(max_length=64) #ip_port
    vip_mode = models.CharField(max_length=32,default="") 
    vip_groupname = models.CharField(max_length=128)
    vip_masterhostname = models.CharField(max_length=128)
    vip_slavehostname = models.CharField(max_length=128)
    app_name = models.CharField(max_length=128)
    app_owner = models.CharField(max_length=128,default="")
    rt_number = models.CharField(max_length=128,default="")
    idc = models.CharField(max_length=64)
    online = models.CharField(max_length=32)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.vip_ip

