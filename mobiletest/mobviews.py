# -*- coding:utf-8 -*-
#------------------------------------
#作者：吴俊威  日期：2018年8月
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
from jy_case.jytest import app_run_test
from common.mysql_pub import *
import datetime
import json
import os
from django.http import JsonResponse
from anyjson import *
from mobiletest.appcomm import *
from time import strftime, localtime

@login_required
def run_apptest(request):
    username = request.session.get('user', '')
    print(username)
    gtid = request.POST['id']
    print(gtid)
    marknum = runnum_add(gtid,1)
    A = MysqlUtil()
    A.mysql_execute("UPDATE  mobiletest_mobiletest SET runstatus='%s' where id= '%s'"%("运行中",gtid))
    A.mysql_execute("UPDATE  mobiletest_mobiletest SET runnum='%s' where id= '%s'"%(marknum,gtid))
    rc,markval=app_run_test(gtid,username,marknum)
    print(rc,markval)
    t1="已运行"+"("+strftime('%Y-%m-%d %H:%M:%S',localtime())+")"
    t2="运行异常"+"("+strftime('%Y-%m-%d %H:%M:%S',localtime())+")"
    mtype='即有宝'
    param_list,param_count = param_db(username)
    con_name,con_num,pc_type,pc_ip = getrun_db(gtid)
    caseall = param_count*con_num
    runnum = con_num
    cpass = int(A.mysql_getstring("SELECT COUNT(*) FROM mobiletest_mobiledata WHERE  runnum='%s'"%markval))#待检查
    print(mtype,rc,caseall,cpass,runnum)
    if rc=="ok":
        A.mysql_execute("UPDATE  mobiletest_mobiletest SET runstatus='%s' where id= '%s'"%(t1,gtid))
        rundata(mtype,rc,caseall,cpass,runnum,markval)
        return HttpResponse("运行完成")
    else:
        A.mysql_execute("UPDATE  mobiletest_mobiletest SET runstatus='%s' where id= '%s'"%(t2,gtid))
        rundata(mtype,rc,caseall,cpass,runnum,markval)
        return HttpResponse("运行异常")


@login_required
def mobile_app(request):
    username = request.session.get('user', '')
    mob_list = Mobiletest.objects.all()
    print(mob_list)
    return render(request, "mobile_test.html", {"user": username,"mob_list": mob_list})

@login_required

def mobtest_report(request):
    username = request.session.get('user', '')
    return render(request, "result_mix.html",{"user": username})

@login_required

def envtest(request):
    username = request.session.get('user', '')
    env_list = Evnccdata.objects.all()
    return render(request, "djd_mix.html",{"user": username,"env_list": env_list})

@login_required

def param_app(request):
    username = request.session.get('user', '')
    A = MysqlUtil()
    param_list =list( A.mysql_getrows("SELECT param_one,param_two,param_three,param_four,param_five,param_six,param_seven,param_eight,param_nine,param_ten,param_eleven,param_twelve FROM mobiletest_paramdata where username = '%s'"%username))
    cap_list =list( A.mysql_getrows("SELECT capital_source, l_amount FROM mobiletest_capitallx"))
    return render(request, "paramc_mix.html",{"user": username,"param_list" :param_list,"cap_list" :cap_list})

@login_required

def param_save(request):
    username = request.session.get('user', '')
    if request.is_ajax() and request.method == 'POST':
        dataDict = {}
        for key in request.POST:
            valuelist = request.POST.getlist(key)
            dataDict[key] = valuelist[0]
    print(dataDict)
    A = MysqlUtil()
    A.mysql_execute("DELETE FROM mobiletest_paramdata where username = '%s'"%username)
    for i in range(0, int(dataDict["trLength"])):
        casei = "case"+str((int(i)+1))
        f = lambda x:x=="" and 0 or x.strip()
        try:
            A.mysql_execute(u"insert into mobiletest_paramdata (param_one, param_two,param_three, param_four, param_five, param_six,param_seven,param_eight,param_nine,param_ten,param_eleven,param_twelve,username,case_no) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%\
                (dataDict["tr"+str(i)+"[0][td]"].strip(), f(dataDict["tr"+str(i)+"[1][td]"]), f(dataDict["tr"+str(i)+"[2][td]"]),f(dataDict["tr"+str(i)+"[3][td]"]),f(dataDict["tr"+str(i)+"[4][td]"]),f(dataDict["tr"+str(i)+"[5][td]"]),f(dataDict["tr"+str(i)+"[6][td]"]),f(dataDict["tr"+str(i)+"[7][td]"]),f(dataDict["tr"+str(i)+"[8][td]"]),f(dataDict["tr"+str(i)+"[9][td]"]),f(dataDict["tr"+str(i)+"[10][td]"]), dataDict["tr"+str(i)+"[11][td]"].strip(),username,casei))
        except Exception as e:
            print(e)
    param_list =list( A.mysql_getrows("SELECT param_one,param_two,param_three,param_four,param_five,param_six,param_seven,param_eight,param_nine,param_ten,param_eleven,param_twelve FROM mobiletest_paramdata where username = '%s'"%username))
    print(param_list)
    return render(request, "paramc_mix.html",{"user": username,"param_list" : param_list})

@login_required
def medit_app(request):
    username = request.session.get('user', '')
    A = MysqlUtil()
    cno_list=A.mysql_getrows("SELECT * FROM mobiletest_mobiledata order by create_time desc")
    cno_list=list(cno_list)
    cno_count = int(A.mysql_getrows("SELECT COUNT(*) FROM mobiletest_mobiledata")[0][0])
    print(cno_count)
    paginator = Paginator(cno_list, 18)
    page = request.GET.get('page',1)
    page=int(page)
    try:
        cno_list = paginator.page(page)
    except PageNotAnInteger:
        cno_list = paginator.page(1)
    except EmptyPage:
        cno_list = paginator.page(paginator.num_pages)
    return render(request, "menu.html",{"user": username,"cno_list": cno_list,"cno_count": cno_count})

# 查询提单数据生成情况
@login_required
def cnosearch(request):
    username = request.session.get('user', '') # 读取浏览器登录session
    search_cno1 = request.GET.get("datea", "")
    search_cno2 = request.GET.get("dateb", "")
    print(search_cno1,search_cno2)
    A = MysqlUtil()
    if search_cno1!='' and search_cno1!='':
        cno_list=A.mysql_getrows("SELECT * FROM mobiletest_mobiledata WHERE  create_time  BETWEEN  '%s' AND  '%s'"%(search_cno1,search_cno2))
        cno_list=list(cno_list)
        print(cno_list)
    else:
        cno_list=list(A.mysql_getrows("SELECT * FROM mobiletest_mobiledata order by create_time desc"))
    paginator = Paginator(cno_list, 18)
    page = request.GET.get('page',1)
    page=int(page)
    try:
        cno_list = paginator.page(page)
    except PageNotAnInteger:
        cno_list = paginator.page(1)
    except EmptyPage:
        cno_list = paginator.page(paginator.num_pages)
    return render(request,'menu.html', {"user": username,"cno_list": cno_list})

@login_required

def log_info(request):
    username = request.session.get('user', '')
    a_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"..")
    log_path = os.path.join(a_path, "logs")
    lpath = log_file(log_path)
    logfile = open(lpath,'r', encoding='UTF-8').readlines()
    return render(request, "loginfo.html",{"user": username,"logfile":logfile})

@login_required
def cap_save(request):  #资金池
    p_list = []
    if request.POST:
        for i in range(11):  #优化
            zjf = request.POST.get("zjf"+str(i+1))
            zj = request.POST.get("zj"+str(i+1))
            p_list.append((zjf,zj))
        print(p_list)
        B = MysqlUtil()
        B.mysql_execute("DELETE FROM  mobiletest_capitallx")
        for j in range(11):
            try:
                B.mysql_execute(u"insert into mobiletest_capitallx (capital_source, l_amount) values ('%s','%s')"%(p_list[j][0],p_list[j][1]))
            except Exception as e:
                print(e)
        cap_list =list( B.mysql_getrows("SELECT capital_source, l_amount FROM mobiletest_capitallx"))
        param_list =list( B.mysql_getrows("SELECT param_one,param_two,param_three,param_four,param_five,param_six,param_seven,param_eight,param_nine,param_ten,param_eleven,param_twelve FROM mobiletest_paramdata"))
    return render(request, "paramc_mix.html",{"cap_list" : cap_list,"param_list" : param_list})

@login_required
def run_dataform(request):#运行数据
    username = request.session.get('user', '')
    A = MysqlUtil()
    rundata_list=A.mysql_getrows("SELECT mtype,caseall,caserun,cpass,cfail,runrate,passrate,runnum,create_time,runmark FROM mobiletest_detaildata order by create_time desc")
    rundata_list=list(rundata_list)
    rundata_count = int(A.mysql_getrows("SELECT COUNT(*) FROM mobiletest_detaildata")[0][0])
    print(rundata_count)
    all_list=A.mysql_getrows("SELECT mtype,SUM(caseall),SUM(caserun),SUM(cpass),SUM(cfail),CONCAT(ROUND(SUM(caserun)/SUM(caseall)*100,2), '%'),CONCAT(ROUND(SUM(cpass)/SUM(caserun)*100,2), '%'),SUM(runnum)  FROM mobiletest_detaildata GROUP BY  mtype")
    all_list=list(all_list)
    paginator = Paginator(rundata_list, 16)
    page = request.GET.get('page',1)
    page=int(page)
    try:
        rundata_list = paginator.page(page)
    except PageNotAnInteger:
        rundata_list = paginator.page(1)
    except EmptyPage:
        rundata_list = paginator.page(paginator.num_pages)
    return render(request, "run_dataform_mix.html",{"user": username,"rundata_list": rundata_list,"rundata_count": rundata_count,"all_list": all_list})


@login_required
def Data_Verify(request):
    username = request.session.get('user', '')
    mark_list = list(MysqlUtil().mysql_getrows("SELECT  DISTINCT  runnum FROM  mobiletest_mobiledata  WHERE username='%s' ORDER BY create_time DESC LIMIT 10 "%username))
    case_list = list(MysqlUtil().mysql_getrows("SELECT case_no  FROM mobiletest_paramdata  WHERE username='%s' ORDER BY id "%username))
    check_list =list( MysqlUtil().mysql_getrows("SELECT casename,casecno,dbname,sqlval,checkone,checkmath,checktwo,markone FROM mobiletest_data_check where username = '%s'"%username))
    print(check_list)
    check_run_list =list( MysqlUtil().mysql_getrows("SELECT  mtype,runmark,casename,casecno,valone,checkmath,valtwo,status,create_time FROM  mobiletest_detail_check WHERE create_time=(SELECT t.create_time FROM (SELECT * FROM mobiletest_detail_check WHERE username = '%s' ORDER BY create_time DESC) t LIMIT 1)"%username))
    return render(request, "DataVerify.html",{"user": username,"mark_list": mark_list,"case_list": case_list,"check_list" : check_list,"check_run_list": check_run_list,"check_lists": json.dumps(check_list)})

@login_required
def ajax_c(request):
    username = request.session.get('user', '')
    if request.method == 'GET':
        id = request.GET.get('id', None)
        runcaseid = request.GET.get('runid', None)
        print(id,runcaseid)
        if id:
            data =list(MysqlUtil().mysql_getrows("SELECT contract_no FROM mobiletest_mobiledata WHERE username='%s' AND case_no='%s' AND runnum='%s'"%(username,id,runcaseid)))
            print(data)
            return JsonResponse(data,safe=False)

@login_required
def check_save(request):
    username = request.session.get('user', '')
    if request.is_ajax() and request.method == 'POST':
        dataDict = {}
        for key in request.POST:
            valuelist = request.POST.getlist(key)
            dataDict[key] = valuelist[0]
    print(dataDict)
    MysqlUtil().mysql_execute("DELETE FROM mobiletest_data_check where username = '%s'"%username)
    for i in range(0, int(dataDict["trLength"])):
        f = lambda x:x=="" and 0 or x.strip()
        try:
            tt = strftime('%Y-%m-%d %H:%M:%S',localtime())
            MysqlUtil().mysql_execute(u"insert into mobiletest_data_check (casename,casecno,dbname,sqlval,checkone,checkmath,checktwo,markone,create_time,username) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%\
                (dataDict["tr"+str(i)+"[0][td]"].strip(), f(dataDict["tr"+str(i)+"[1][td]"]), f(dataDict["tr"+str(i)+"[2][td]"]),pymysql.escape_string(f(dataDict["tr"+str(i)+"[3][td]"])),f(dataDict["tr"+str(i)+"[4][td]"]),f(dataDict["tr"+str(i)+"[5][td]"]),f(dataDict["tr"+str(i)+"[6][td]"]),pymysql.escape_string(f(dataDict["tr"+str(i)+"[7][td]"])),tt,username))
        except Exception as e:
            print(e)
    check_list =list( MysqlUtil().mysql_getrows("SELECT casename,casecno,dbname,sqlval,checkone,checkmath,checktwo,markone FROM mobiletest_data_check where username = '%s'"%username))
    print(check_list)
    return render(request, "DataVerify.html",{"user": username,"check_list" : check_list})

@login_required
def check_run(request):
    username = request.session.get('user', '')
    if request.method == 'GET':
        runcaseid = request.GET.get('mkid', None)
        if runcaseid == "选择运行源":
            runcaseid = username+'_auto'
        print(runcaseid)
    r_count = int(MysqlUtil().mysql_getrows("SELECT COUNT(*) FROM mobiletest_data_check WHERE username = '%s'"%username)[0][0])
    print(r_count)
    cpass = 0
    for i in range(r_count):
        p = MysqlUtil().mysql_getrows("SELECT * FROM mobiletest_data_check WHERE username = '%s' ORDER BY id"%username)
        if sel_db(p[i][3],p[i][4]) and sel_db(p[i][3],p[i][4]) is not None:
            checkval = sel_db(p[i][3],p[i][4])
        else:
            checkval = [('','')]
        if len(checkval[0])>1:
            s = checkval[0][0]
            k = checkval[0][1]
        elif len(checkval[0])==1:
            s = checkval[0][0]
            k = ''
        else:
            s = ''
            k = ''
        print(s,k)
        if p[i][6]=='==':
            c = p[i][7]
        else:
            c = k
        print(c,p[i][6])
        tt = strftime('%Y-%m-%d %H:%M:%S',localtime())
        if checkdb(s,c,p[i][6]):
            MysqlUtil().mysql_execute(u"insert into mobiletest_detail_check (mtype,runmark,casename,valone,valtwo,status,create_time,username,casecno,checkmath) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%\
                ('即有宝',runcaseid,p[i][1],s,c,'pass',tt,username,p[i][2],p[i][6]))
            cpass+=1
        else:
            MysqlUtil().mysql_execute(u"insert into mobiletest_detail_check (mtype,runmark,casename,valone,valtwo,status,create_time,username,casecno,checkmath) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%\
                ('即有宝',runcaseid,p[i][1],s,c,'fail',tt,username,p[i][2],p[i][6]))
    mtype = '即有宝'
    rc = 'ok'
    caseall = r_count
    markval = runcaseid+'_db'
    rundata(mtype,rc,caseall,cpass,1,markval)
    check_run_list =list( MysqlUtil().mysql_getrows("SELECT  mtype,runmark,casename,casecno,valone,checkmath,valtwo,status,create_time FROM  mobiletest_detail_check WHERE create_time=(SELECT t.create_time FROM (SELECT * FROM mobiletest_detail_check WHERE username = '%s' ORDER BY create_time DESC) t LIMIT 1)"%username))
    data = {'da':'运行完成,请查看报告','check_run_list':check_run_list}
    print(data)
    return JsonResponse(data,safe=False)

