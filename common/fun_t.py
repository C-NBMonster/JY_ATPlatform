# -*- coding:utf-8 -*-
#------------------------------------
#作者：吴俊威  日期：2018年9月,12月
#-----------------------------------

import random
import os
from common.mysql_pub import *
import time
import yaml
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions

ch_t=['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十']
loginname = "300079"
loginpwd = "123456"
idcard = "150621198109199273"
mobilephone = "13300000000"
def chzw():#随机中文
    val1 = random.randint(0x4e00, 0x9fbf)
    val2 = random.randint(0x4e00, 0x9fbf)
    val=chr(val1)+chr(val2)
    return val

def swipeup(driver):
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    driver.swipe(width/2, height/4*3, width/2, height/4, 500)

def swipeleft(driver,snum):
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    for k in range(snum):
        driver.swipe(width/4*3, height / 2, width / 4 *1, height / 2, 500)
        time.sleep(1)

def log_file(log_path): #日志文件
    loglist = os.listdir(log_path)
    loglist.sort(key=lambda x: os.path.getmtime(os.path.join(log_path, x)))
    print (u'日志： '+loglist[-1])
    loginfo_file = os.path.join(log_path, loglist[-1])
    return loginfo_file

def param_db(uname):#即有宝参数设置
    try:
        A = MysqlUtil()
        param_data =A.mysql_getrows("SELECT param_one,param_two,param_three,param_four,param_five,param_six,param_seven,param_eight,param_nine,param_ten,param_eleven,param_twelve,case_no FROM mobiletest_paramdata  where username = '%s'"%uname)
        param_count =int(A.mysql_getrows("SELECT COUNT(*) FROM mobiletest_paramdata where username = '%s'"%uname)[0][0])
        param_list = []
        for pdata in param_data:
            dict = {'parama':pdata[0],'paramb':pdata[1],'paramc':pdata[2],'paramd':pdata[3],'parame':pdata[4],'paramf':pdata[5],'paramg':pdata[6],'paramh':pdata[7],'parami':pdata[8],'paramj':pdata[9],'paramk':pdata[10],'paraml':pdata[11],'paramm':pdata[12]}
            param_list.append(dict)
        return param_list,param_count
        print(param_list)
    except:
        return {}

def lparam_db(uname):#即有生活参数设置
    try:
        A = MysqlUtil()
        lparam_data =A.mysql_getrows("SELECT param_phone,param_pwd,param_name,param_ltype,param_bcard,param_cardNo,param_ppwd,case_no FROM jylive_liveparam  where username = '%s'"%uname)
        lparam_count =int(A.mysql_getrows("SELECT COUNT(*) FROM jylive_liveparam where username = '%s'"%uname)[0][0])
        lparam_list = []
        for pdata in lparam_data:
            dict = {'param_phone':pdata[0],'param_pwd':pdata[1],'param_name':pdata[2],'param_ltype':pdata[3],'param_bcard':pdata[4],'param_cardNo':pdata[5],'param_ppwd':pdata[6],'case_no':pdata[7]}
            lparam_list.append(dict)
        return lparam_list,lparam_count
        print(lparam_list)
    except:
        return {}

def getyaml(yamlpath): #读
    try:
        with open(yamlpath, encoding='utf-8') as f:
            val = yaml.load(f)
            return val
    except FileNotFoundError:
        print(u"读取异常")

def getrun_db(runid):#参数设置
    try:
        A = MysqlUtil()
        sql = "select * from mobiletest_mobiletest where id= %s"%runid
        app_list = A.mysql_getrows(sql)
        con_name=app_list[0][1] #合同名称
        con_num = int(app_list[0][2])  #合同数量
        pc_type = app_list[0][3] #类型
        pc_ip = app_list[0][4] #服务ip
        return con_name,con_num,pc_type,pc_ip
    except:
        return {}

def runnum_add(getid,t=1):#运行次数
    try:
        A = MysqlUtil()
        if t==1:
            sql = "SELECT runnum FROM  mobiletest_mobiletest WHERE id= %s"%getid
        if t==2:
            sql = "SELECT livenum FROM  mobiletest_mobiletest WHERE id= %s"%getid
        if t==3:
            sql = "SELECT cashnum FROM  mobiletest_mobiletest WHERE id= %s"%getid
        runnuma = A.mysql_getrows(sql)
        runnumadd=int(runnuma[0][0])+1
        return runnumadd
    except:
        return {}

def rundata(mtype,rc,caseall,cpass,runnum,runmark):#运行数据
    try:
        A = MysqlUtil()
        # if mtype=='即有宝' and rc=='ok':
        if  rc=='ok':
            cpass=cpass
            caserun=caseall
            cfail=int(caserun)-int(cpass)
            runrate=round(int(caserun)/int(caseall),4)
            runrate=format(runrate, '.2%')
            passrate=round(int(cpass)/int(caserun),4)
            passrate=format(passrate, '.2%')
        else:
            caserun=0
            cpass=0
            cfail=0
            runrate=format(0, '.2%')
            passrate=format(0, '.2%')
        A.mysql_execute("INSERT INTO mobiletest_detaildata (mtype,caseall,caserun,cpass,cfail,runrate,passrate,runnum,create_time,runmark) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',NOW(),'%s')"%(mtype,caseall,caserun,cpass,cfail,runrate,passrate,runnum,runmark))
    except Exception as e:
        print(e)


def wryaml(yamlpath,val): #写
    try:
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(val,f)
    except Exception as e:
        print(e)

def swipeUp(Driver, sd=0,  x1=0, y1=0, x2=0, y2=0, t=500, n=1):
    """
    向上滑动屏幕
    :param t: 滑动持续时间
    :param n: 滑动的次数
    :sd:标记为自定义坐标：0表示根据屏幕来算，默认点在中间； 1表示自定义坐标
    :return:
    """
    if sd == 1:
        for i in range(n):
            Driver.swipe(x1, y1, x2, y2, t)
            time.sleep(0.5)
    else:
        l_winSize = Driver.get_window_size()
        x1 = l_winSize['width'] * 0.5  # x坐标
        y1 = l_winSize['height'] * 0.75  # 起始y坐标
        y2 = l_winSize['height'] * 0.25  # 终点y坐标
        for i in range(n):
            Driver.swipe(x1, y1, x1, y2, t)
            time.sleep(0.5)

# 随机生成手机号码
def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "176", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

# 随机生成身份证号码
def makeIDNo():
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    u''' 随机生成新的18为身份证号码 '''
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                          random.randint(1, 99),
                                          random.randint(1, 99),
                                          random.randint(t - 80, t - 18),
                                          random.randint(1, 12),
                                          random.randint(1, 28),
                                          random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' % (x, LAST[y % 11])


if __name__ == "__main__":
    pass
    # cur_path = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".")
    # log_path = os.path.join(cur_path, "logs")
    # yapath = os.path.join(cur_path, "config\yaml\jyb\dim.yaml")
    # p='自动化'
    # n={'name':p}
    # # with open(yapath, "w", encoding="utf-8") as f:
    # #     yaml.dump(n,f)
    # wryaml(yapath,n)
    # print(getyaml(yapath).get('name'))
    # c=log_file(log_path)
    # d,o=param_db()
    # print(type(d[0]['paramf']))
    # print(d[0]['paramf'],o)
    # print(type('dd'))
    # vala = getyaml(yapath)
    # print(vala['android真机'][0]['platformName'])
    # print(vala['android真机'])
    # p = {'a':lambda:log_path}
    # print(p['a'])
    # PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    # # print(PATH("..\config\yaml\jyb\caps.yaml"))
    # vala = getyaml(PATH("..\config\yaml\jyb\jybcase1.yaml"))
    # print(vala)
    # print(vala['订单页面一'][1]['cType'])
    # print(vala['android真机'][0]['platformName'])
    # print(runnum_add(2))
    # runrate=format(0, '.2%')
    # print(runrate)
    # caserun=0
    # cpass=0
    # passrate=round(int(cpass)/int(caserun),4)
    # print(passrate)