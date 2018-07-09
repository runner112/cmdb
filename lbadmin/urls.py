import os
import sys

"""lbadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from lvsmanager import views
from ansiblemage import views as ansible

handler404 = "lvsmanager.views.page_not_found"
handler500 = "lvsmanager.views.page_error"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='homepage'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^add_server/$', views.add_server, name='add_server'),
    url(r'^add_vip/$', views.add_vip, name='add_vip'),
    url(r'^view_server/$', views.view_server, name='view_server'),
    #url(r'^cmd/$', views.getcmd_out, name='cmd'),
    #url(r'^$', include('lvsmanager.urls')),

    url(r'^layer7/', ansible.layer7),

] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
