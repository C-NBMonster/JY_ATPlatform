# -*- coding:utf-8 -*-
#------------------------------------
#作者：吴俊威  日期：2018年10月
#-----------------------------------

import urllib.request
from urllib.error import URLError
from common.logger import Log
from common.fun_t import *
import os
from common.adb_t import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import yaml
from appium import webdriver
from common.oracle_pub import *
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def getcaps(pc_type,n=1):
    if n==1:
        vala = getyaml(PATH("..\config\yaml\jyb\caps.yaml"))
    if n==2:
        vala = getyaml(PATH("..\config\yaml\jylive\capslive.yaml"))
    if n==3:
        vala = getyaml(PATH("..\config\yaml\jycash\capsloan.yaml"))
    capval = vala[pc_type][0]
    if pc_type.split('：')[0]=='android真机':
        Androidconect().call_adb("adb kill-server")
        Androidconect().call_adb("adb start-server")
    else:
        Androidconect().call_adb("connect 127.0.0.1:21503")#xiaoyao
    desired_caps = {}
    desired_caps['platformName'] = capval['platformName']
    desired_caps['platformVersion'] = capval['platformVersion']
    desired_caps['deviceName'] = capval['deviceName']   #真机端口5555
    desired_caps['appPackage'] = capval['appPackage']
    desired_caps['appActivity'] = capval['appActivity']
    desired_caps['unicodeKeyboard'] = capval['unicodeKeyboard']
    desired_caps['resetKeyboard'] = capval['resetKeyboard']
    # desired_caps['automationName'] = "Uiautomator2"
    return desired_caps


def connecthub(pc_type,pc_ip,n=1):
    url = 'http://'+pc_ip+':4723/wd/hub/status'
    desired_caps = getcaps(pc_type,n)
    try:
        res = urllib.request.urlopen(url, timeout=5)
        if str(res.getcode()).startswith("200"):
            driver = webdriver.Remote('http://'+pc_ip+':4723/wd/hub', desired_caps)
            return driver
        else:
            return False
    except URLError:
        return False


#单个
def get_elm(driver,byType,cval):
    try:
        elm = WebDriverWait(driver,10).until(lambda x:x.find_element(by = byType,value = cval))
    except selenium.common.exceptions.TimeoutException:
        Log().info("元素定位失败:'%s'"%cval)
        return False
    return elm

#多个
def get_elms(driver,byType,cval):
    try:
        elms = WebDriverWait(driver,10).until(lambda x:x.find_elements(by = byType,value = cval))
    except selenium.common.exceptions.TimeoutException:
        Log().info("元素定位失败:'%s'"%cval)
        return False
    return elms

#读参定位
def elm_on(driver,k):
    byType,cval,optype,index,text = case_val(k)
    elm_s = get_elm(driver,byType,cval)
    return elm_s

def elms_on(driver,k):
    byType,cval,optype,index,text = case_val(k)
    elms_s = get_elms(driver,byType,cval)
    return elms_s

#读参
def case_val(k):
    yamlval = getyaml(PATH("..\config\yaml\jyb\jybcase1.yaml"))[k]
    byType = yamlval['byType']
    cval = yamlval['cval']
    optype = yamlval['optype']
    text = yamlval['text']
    index = yamlval['index']
    print(yamlval)
    return byType,cval,optype,index,text

#操作
def elm_operate(driver,k,textnew):
    byType,cval,optype,index,text = case_val(k)
    if optype == 'click':
        if index == None:
            get_elm(driver,byType,cval).click()
        elif index is not None:
            get_elms(driver,byType,cval)[index].click()
    elif optype == 'send_keys':
        if text == None and index == None:
            get_elm(driver,byType,cval).send_keys(textnew)
        elif text is not None and index == None:
            get_elm(driver,byType,cval).send_keys(text)
        elif text is not None and index is not None:
            get_elms(driver,byType,cval)[index].send_keys(text)
        elif text == None and index is not None:
            get_elms(driver,byType,cval)[index].send_keys(textnew)


#存在判断
def elm_click(driver,k):
    byType,cval,optype,index,text = case_val(k)
    len_elms = len(get_elms(driver,byType,cval))
    if len_elms>0:
        get_elm(driver,byType,cval).click()
    else:
        pass

def elm_son_click(driver,m,n,c):
    try:
        byTypem,cvalm,optypem,indexm,textm = case_val(m)
        byTypen,cvaln,optypen,indexn,textn = case_val(n)
        elmson = driver.find_element_by_id(cvalm)
        elmsons = elmson.find_elements_by_class_name(cvaln)
        elmsons[c].click
    except Exception as e:
        print(e)
#通用子send
def elm_allson_send(driver,m,n,index,c):
    try:
        byTypem,cvalm,optypem,indexm,textm = case_val(m)
        byTypen,cvaln,optypen,indexn,textn = case_val(n)
        elmson = driver.find_element(by = byTypem,value = cvalm)
        elmsons = elmson.find_elements(by = byTypen,value = cvaln)
        elmsons[index].send_keys(c)
    except Exception as e:
        print(e)

def elm_son_send(driver,m,n,index,c):
    try:
        byTypem,cvalm,optypem,indexm,textm = case_val(m)
        byTypen,cvaln,optypen,indexn,textn = case_val(n)
        elmson = driver.find_element_by_id(cvalm)
        elmsons = elmson.find_elements_by_class_name(cvaln)
        elmsons[index].send_keys(c)
    except Exception as e:
        print(e)
#通用子click
def elm_allson_click(driver,m,n,index):
    try:
        byTypem,cvalm,optypem,indexm,textm = case_val(m)
        byTypen,cvaln,optypen,indexn,textn = case_val(n)
        elmson = driver.find_element(by = byTypem,value = cvalm)
        elmsons = elmson.find_elements(by = byTypen,value = cvaln)
        print(elmson,elmsons)
        elmsons[index].click
    except Exception as e:
        print(e)


def get_dbtext(driver,gnum,tval):
    try:
        if gnum == 0:
            driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%tval).click()
        elif gnum == 1:
            driver.find_element_by_android_uiautomator('new UiSelector().textContains("%s")'%tval).click()
    except Exception as e:
        Log().info("元素定位失败:'%s'"%tval)
        print(e)

#取文本值
def get_elm_textval(driver,k):
    textvala =elm_on(driver,k).text
    tesval=[]
    tesval.append(textvala.strip())
    textval=tesval[0]
    return textval

def remove_lines(a,b,val): #移除标记行
    with open(a, "r",encoding='UTF-8') as s_r:
        lines = s_r.readlines()
    with open(b, "w",encoding='UTF-8') as s_w:
        for line in lines:
            if val in line:
                continue
            s_w.write(line)

def copy_lines(a,b): #复制
    with open(a, "r",encoding='UTF-8') as s_r:
        lines = s_r.readlines()
    with open(b, "w",encoding='UTF-8') as s_w:
        for line in lines:
            s_w.write(line)

def replace_string(a,b,val_a,val_b): #替换字符
    with open(a, "r",encoding='UTF-8') as s_r:
        lines = s_r.readlines()
    with open(b, "w",encoding='UTF-8') as s_w:
        for line in lines:
            if val_a in line:
                line = line.replace(val_a,val_b)
            s_w.write(line)

def del_files(path,filename):
        for root,dirs,files in os.walk(path):#（使用 os.walk ,这个方法返回的是一个三元tupple(dirpath(string), dirnames(list), filenames(list)), 其中第一个为起始路径， 第二个为起始路径下的文件夹, 第三个是起始路径下的文件.）
                for name in files:
                    if filename in name:#判断某一字符串是否具有某一字串，可以使用in语句
                        os.remove(os.path.join(root,name))##os.move语句为删除文件语句

def findItem(driver,el):
    source = driver.page_source
    if el in source:
        return True
    else:
        return False

def change_name(pathcname,nameval):#con_name全称
    with open(pathcname,'r',encoding='UTF-8') as ui:
        data = ui.readlines()
    for inx,line in enumerate(data):
        if inx == 14:
            val = str("newcon_name=")+"\""+str(nameval)+"\""+"\n"
            data[inx] = val
    with open(pathcname,'w',encoding='UTF-8') as oi:
        oi.writelines(data)

def sel_db(dname,sql):#选择数据库执行
    try:
        if dname == "oracle":
            orc_val = OracleUtil(dbname).oracle_getrows(sql)
            if orc_val:
                return orc_val
        if dname == "mysql":
            mysql_val = MysqlUtil().mysql_getrows(sql)
            if mysql_val:
                return mysql_val
        else:
            return False
    except Exception as e:
        print(e)

def checkdb(first,second,ctype):
    if first==second and '='==ctype:
        return True
    if first!=second and '!='==ctype:
        return True
    if first>second and '>'==ctype:
        return True
    if str(first)<str(second) and '<'==ctype:
        return True
    if '=='==ctype and first==second:
        return True
    else:
        return False


if __name__=='__main__':
    path=r'D:\www\auto\jytest\case'#此为需要删除的路径
    # filename = 'test_2_'
    # # del_files(path,filename)#调用函数
    # vala = getyaml(PATH("..\config\yaml\jyb\caps.yaml"))
    # pc_type='android真机：小米6.0.1'
    # capval = vala[pc_type][0]
    # print(capval)
    # c=sel_db("mysql","SELECT * FROM mobiletest_mobiledata WHERE contract_no='21094010001'")
    # print(c[0][1])
    # p = MysqlUtil().mysql_getstring(" SELECT * FROM mobiletest_data_check ")
    # p = MysqlUtil().mysql_getrows(" SELECT * FROM mobiletest_data_check ")
    # print(len(sel_db('mysql'," SELECT contract_no FROM mobiletest_mobiledata WHERE contract_no='21094010001'")[0]))
    # print(len(sel_db('mysql',"SELECT casecno,checktwo FROM `mobiletest_data_check` WHERE checktwo=2")[0]))
    # checkval = [('','')]
    # print(len(checkval[0]))
    # copy_lines(PATH("../jy_case/jylive_temp.py"),PATH("../livecase/test_sh_300079_4_0.py"))

# byType,cval,optype,index,text = case_val(0)
# print(byType,cval,optype,index,text)

