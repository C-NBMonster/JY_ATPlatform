# -*- coding:utf-8 -*-
#------------------------------------
#作者：吴俊威  日期：2018年8月
#-----------------------------------
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import json
from django.template import RequestContext
from django.http import JsonResponse
@login_required
def map_app(request):
    username = request.session.get('user', '')
    return render(request, "index.html", {"user": username})

