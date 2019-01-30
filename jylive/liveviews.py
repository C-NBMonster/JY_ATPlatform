# -*- coding:utf-8 -*-
#------------------------------------
#作者：吴俊威 日期：2019年1月
#-----------------------------------
from django.shortcuts import render
from mobiletest.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import taceback
# from run_main import run_app
from common.fun_t import *
from jy_case.livetest import live_run_test
from common.mysql_pub import *
import datetime
import json
import os
from django.http import JsonResponse
from anyjson import *
from mobiletest.appcomm import *
from time import strftime, localtime

@login_required

def livetest_report(request):
    username = request.session.get('user', '')
    return render(request, "result_live_mix.html",{"user": username})

@login_required
def live_run(request):
    username = request.session.get('user', '')
    mob_list = Mobiletest.objects.all()
    return render(request, "run.html", {"user": username,"mob_list": mob_list})

@login_required

def live_param(request):
    username = request.session.get('user', '')
    A = MysqlUtil()
    lparam_list =list( A.mysql_getrows("SELECT param_phone,param_pwd,param_name,param_ltype,param_bcard,param_cardNo,param_ppwd FROM jylive_liveparam where username = '%s'"%username))
    return render(request, "live_param_mix.html",{"user": username,"lparam_list" :lparam_list})

@login_required

def live_param_save(request):
    username = request.session.get('user', '')
    if request.is_ajax() and request.method == 'POST':
        dataDict = {}
        for key in request.POST:
            valuelist = request.POST.getlist(key)
            dataDict[key] = valuelist[0]
    print(dataDict)
    A = MysqlUtil()
    A.mysql_execute("DELETE FROM jylive_liveparam where username = '%s'"%username)
    for i in range(0, int(dataDict["trLength"])):
        casei = "case"+str((int(i)+1))
        f = lambda x:x=="" and 0 or x.strip()
        try:
            A.mysql_execute(u"insert into jylive_liveparam (username,case_no,param_phone,param_pwd,param_name,param_ltype,param_bcard,param_cardNo,param_ppwd) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%\
                (username,casei,dataDict["tr"+str(i)+"[0][td]"].strip(), f(dataDict["tr"+str(i)+"[1][td]"]), f(dataDict["tr"+str(i)+"[2][td]"]),f(dataDict["tr"+str(i)+"[3][td]"]),f(dataDict["tr"+str(i)+"[4][td]"]),f(dataDict["tr"+str(i)+"[5][td]"]),f(dataDict["tr"+str(i)+"[6][td]"])))
        except Exception as e:
            print(e)
    lparam_list =list( A.mysql_getrows("SELECT param_phone,param_pwd,param_name,param_ltype,param_bcard,param_cardNo,param_ppwd FROM jylive_liveparam where username = '%s'"%username))
    print(lparam_list)
    return render(request, "live_param_mix.html",{"user": username,"lparam_list" : lparam_list})

@login_required
def run_livetest(request):
    username = request.session.get('user', '')
    print(username)
    gtid = request.POST['id']
    print(gtid)
    marknum = runnum_add(gtid,2)
    A = MysqlUtil()
    A.mysql_execute("UPDATE  mobiletest_mobiletest SET runstatus='%s' where id= '%s'"%("运行中",gtid))
    A.mysql_execute("UPDATE  mobiletest_mobiletest SET livenum='%s' where id= '%s'"%(marknum,gtid))
    rc,markval=live_run_test(gtid,username,marknum)
    print(rc,markval)
    t1="已运行"+"("+strftime('%Y-%m-%d %H:%M:%S',localtime())+")"
    t2="运行异常"+"("+strftime('%Y-%m-%d %H:%M:%S',localtime())+")"
    mtype='即有生活'
    param_list,lparam_count = lparam_db(username)
    # param_count = 1#暂时写1
    con_name,con_num,pc_type,pc_ip = getrun_db(gtid)
    con_num = 1#设置为运行一次
    caseall = lparam_count*con_num
    runnum = con_num
    # cpass = int(A.mysql_getstring("SELECT COUNT(*) FROM mobiletest_mobiledata WHERE  runnum='%s'"%markval))#待检查
    cpass = 1#待更新
    print(mtype,rc,caseall,cpass,runnum)
    if rc=="ok":
        A.mysql_execute("UPDATE  mobiletest_mobiletest SET runstatus='%s' where id= '%s'"%(t1,gtid))
        rundata(mtype,rc,caseall,cpass,runnum,markval)
        return HttpResponse("运行完成")
    else:
        A.mysql_execute("UPDATE  mobiletest_mobiletest SET runstatus='%s' where id= '%s'"%(t2,gtid))
        rundata(mtype,rc,caseall,cpass,runnum,markval)
        return HttpResponse("运行异常")