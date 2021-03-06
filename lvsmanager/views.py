#-*- encoding:UTF-8 -*-

import MySQLdb,os,sys,json,subprocess,re
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from lvsmanager.models import MyUser, Server_info, Vip_info
from django.core.urlresolvers import reverse
from lvsmanager.utils import permission_check

def index(request):
    ##print "test is ok!"
    
    ##return render(request, 'hello.html', context)
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'homepage',
        'user': user,
    }
    return render(request, 'index.html', content)

#注册方法
def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password', '').strip()
        repeat_password = request.POST.get('repeat_password', '').strip()
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '').strip()
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                ###new_user = User.objects.create_user(username=username, password=password)
                ###new_user.save()
                #与django的auth模块User表关联用户名
                ###new_my_user = MyUser(user=new_user, nickname=request.POST.get('nickname', '').strip())
                ###new_my_user.save()
                state = 'success'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None,
    }
    return render(request, 'signup.html', content)


def getcmd_out(request):
    cmd = "hostname"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    c = p.stdout.read().strip()
    #c = "test"
    content = {
        'active_menu': 'homepage',
        'c': c,
        'user': None,
    }
    return render(request, 'cmd.html', content)

#登陆方法
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'login.html', content)

#服务器信息录入方法
@user_passes_test(permission_check)
def add_server(request):
    user = request.user
    state = None
    msg = ""
    msg1 = ""
    msg2 = ""
    msg3 = ""
    msg4 = ""
    msg5 = ""
    msg6 = ""
    msg7 = ""
    pattern_ip = re.compile("^(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|[1-9])\\.(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\.(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\.(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)$")
    #pattern_ip = re.compile("^([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])$")
    #pattern_ip = re.compile("^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
    if request.method == 'POST':
       new_server = Server_info(
               server_name=request.POST.get('server_name', '').strip(),
               pnb=request.POST.get('pnb', '').strip(),
               wip=request.POST.get('wip', '').strip(),
               nip=request.POST.get('nip', '').strip(),
               gip=request.POST.get('gip', '').strip(),
               role=request.POST.get('role', '').strip(),
               idc=request.POST.get('idc', '').strip(),
               online=request.POST.get('online', '').strip(),
               bondwidth=request.POST.get('bondwidth', '').strip(),
               server_groupname=request.POST.get('server_groupname','').strip(),
               mark=request.POST.get('mark', '').strip(),
               update_time=request.POST.get('update_time', '').strip(),
       )

       server_name = request.POST.get('server_name', '').strip()
       pnb = request.POST.get('pnb', '').strip()
       wip = request.POST.get('wip', '').strip()
       result = pattern_ip.match(wip)
       nip = request.POST.get('nip', '').strip()
       result1 = pattern_ip.match(nip)
       gip = request.POST.get('gip', '').strip()
       result2 = pattern_ip.match(gip)      

       if Server_info.objects.filter(server_name=server_name):
           msg = "主机名重复,请重新录入！"
       elif Server_info.objects.filter(pnb=pnb):
           msg4 = "盘点号重复,请重新录入！"
       elif Server_info.objects.filter(wip=wip):
           msg5 = "IP地址重复,请重新录入！"
       elif Server_info.objects.filter(nip=nip):
           msg6 = "IP地址重复,请重新录入！"
       elif Server_info.objects.filter(gip=gip):
           msg7 = "IP地址重复,请重新录入！"
       elif not result:
           msg1 = "IP地址格式不正确,请重新录入！"
       elif not result1:
           msg2 = "IP地址格式不正确,请重新录入！"
       elif not result2:
           msg3 = "IP地址格式不正确,请重新录入！"
       else:
           new_server.save()
           state = 'success'

    content = {
        'user': user,
        'active_menu': 'add_server',
        'state': state,
        'msg': msg,
        'msg1': msg1,
        'msg2': msg2,
        'msg3': msg3,
        'msg4': msg4,
        'msg5': msg5,
        'msg6': msg6,
        'msg7': msg7,
    }
    return render(request, 'add_server.html', content)

#VIP录入方法
@user_passes_test(permission_check)
def add_vip(request):
    user = request.user
    content= ""
    msg = ""
    msg1= ""
    msg2= ""
    state= ""
    pattern_ip = re.compile("^(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|[1-9])\\.(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\.(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\.(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)$")
    if request.method == 'POST':
        new_vip = Vip_info(
            vip_ip=request.POST.get('vip_ip', '').strip(),
            vip_port=request.POST.get('vip_port', '').strip(),
            vip_mode = request.POST.get('vip_mode', '').strip(),
            vip_groupname = request.POST.get('vip_groupname', '').strip(),
            vip_masterhostname = request.POST.get('vip_masterhostname', '').strip(),
            vip_slavehostname = request.POST.get('vip_slavehostname', '').strip(),
            app_name = request.POST.get('app_name', '').strip(),
            app_owner = request.POST.get('app_owner', '').strip(),
            rt_number = request.POST.get('rt_number', '').strip(),
            idc=request.POST.get('idc', '').strip(),
            online=request.POST.get('idc', '').strip(),
            update_time=request.POST.get('update_time', '').strip(),

        )
        vip_ip = request.POST.get('vip_ip', '').strip()
        result = pattern_ip.match(vip_ip)	    
        vip_groupname = request.POST.get('vip_groupname', '').strip()
        vip_masterhostname = request.POST.get('vip_masterhostname', '').strip()
        vip_slavehostname = request.POST.get('vip_slavehostname', '').strip()

        if Vip_info.objects.filter(vip_ip=vip_ip):
            msg = "VIP重复,请重新录入！"
	elif not result:
	    msg = "IP地址格式不正确,请重新录入！"
        elif not (Server_info.objects.filter(wip=vip_masterhostname) and Server_info.objects.filter(wip=vip_slavehostname) ):
            msg1 = "录入的主或备lvs的ip不存在！"

        elif not Server_info.objects.filter(server_groupname=vip_groupname):
            msg2 = "录入的集群组不存在！"
        else:
            new_vip.save()
            state = 'success'
        content = {
            'user': user,
            'state': state,
            'msg': msg,
            'msg1':msg1,
            'msg2': msg2
        }

    return render(request, 'add_vip.html',content)

'''
def view_server(request):
#    server_list = Server_info.objects.all()
    server_list_number = 6 
    server_list_paginator_num_pages = 3
    pass
    
    content = {
 #           'server_list':server_list,
            'server_list_number': server_list_number,
            'server_list_paginator_num_pages':server_list_paginator_num_pages,
    }    
    return render(request, 'view_server.html',content)
'''


def view_server(request):
    user = request.user if request.user.is_authenticated() else None
    server_list = Server_info.objects.all() #默认list取全部结果,每页5条数据

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        #server_list = Server_info.objects.filter(name__contains=keyword)
        server_list = Server_info.objects.filter(Q(server_name__icontains=keyword)|Q(wip__icontains=keyword)|Q(nip__icontains=keyword)|Q(gip__icontains=keyword)|Q(pnb__icontains=keyword)|Q(role__icontains=keyword)|Q(idc__icontains=keyword)|Q(online__icontains=keyword)|Q(bondwidth__icontains=keyword)|Q(server_groupname__icontains=keyword)|Q(mark__icontains=keyword))
        paginator = Paginator(server_list, 20) #每页显示5条记录
        page = request.GET.get('page') #从模板url中获取get的page参数页数
        try:
            server_list = paginator.page(page)
        except PageNotAnInteger:
            server_list = paginator.page(1) #page非整数显示第一页
        except EmptyPage:
            server_list = paginator.page(paginator.num_pages) #page为空显示最后一页
  

        content = {
            'user': user,
            'active_menu': view_server,
            'server_list': server_list,
            'keyword': keyword,
        }

        return render(request, 'view_server.html', content)


    if request.method == 'GET':
        keyword = request.GET.get('keyword', '')
        server_list = Server_info.objects.filter(Q(server_name__icontains=keyword)|Q(wip__icontains=keyword)|Q(nip__icontains=keyword)|Q(gip__icontains=keyword)|Q(pnb__icontains=keyword)|Q(role__icontains=keyword)|Q(idc__icontains=keyword)|Q(online__icontains=keyword)|Q(bondwidth__icontains=keyword)|Q(server_groupname__icontains=keyword)|Q(mark__icontains=keyword))
        paginator = Paginator(server_list, 20) 
        page = request.GET.get('page') 
        try:
            server_list = paginator.page(page)
        except PageNotAnInteger:
            server_list = paginator.page(1) #page非整数显示第一页
        except EmptyPage:
            server_list = paginator.page(paginator.num_pages) #page为空显示最后一页
  

        content = {
            'user': user,
            'active_menu': view_server,
            'server_list': server_list,
            'keyword': keyword,
        }

        return render(request, 'view_server.html', content)


    paginator = Paginator(server_list, 20) #每页显示5条记录
    page = request.GET.get('page') #从模板url中获取get的page参数页数
    try:
        server_list = paginator.page(page)
    except PageNotAnInteger:
        server_list = paginator.page(1) #page非整数显示第一页
    except EmptyPage:
        server_list = paginator.page(paginator.num_pages) #page为空显示最后一页
  
    content = {
        'user': user,
        'active_menu': view_server,
        'server_list': server_list,
    }

    return render(request, 'view_server.html', content)


def logout(request):

    #print "this is logout!"
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))



###

