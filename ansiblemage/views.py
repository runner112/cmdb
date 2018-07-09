from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from tengine7 import NgninxUpstream,Showupstream,UpdateUpstream,Contrastupstream
from lvsmanager.utils import permission_check

# Create your views here.


@user_passes_test(permission_check)
def layer7(request):
    idc = request.GET['idc']
    upstream_infor = NgninxUpstream(idc)
    return render(request,'layer7.html',{'upstream_infor':upstream_infor})
