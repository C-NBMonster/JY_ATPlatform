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
import requests
import json
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class appclass(object):
    def __init__(self,driver,cpath):
        self.driver = driver
        self.cpath = cpath

    #单个
    def get_elm(self,byType,cval):
        try:
            elm = WebDriverWait(self.driver,30).until(lambda x:x.find_element(by = byType,value = cval))
        except selenium.common.exceptions.TimeoutException:
            Log().info("元素定位失败:'%s'"%cval)
            return False
        return elm

    #多个
    def get_elms(self,byType,cval):
        try:
            elms = WebDriverWait(self.driver,30).until(lambda x:x.find_elements(by = byType,value = cval))
        except selenium.common.exceptions.TimeoutException:
            Log().info("元素定位失败:'%s'"%cval)
            return False
        return elms

    #读参
    def case_val(self,k):
        yamlval = getyaml(self.cpath)[k]
        byType = yamlval['byType']
        cval = yamlval['cval']
        optype = yamlval['optype']
        text = yamlval['text']
        index = yamlval['index']
        return byType,cval,optype,index,text

    #读参定位
    def elm_on(self,k):
        byType,cval,optype,index,text = self.case_val(k)
        elm_s = self.get_elm(byType,cval)
        return elm_s

    def elms_on(self,k):
        byType,cval,optype,index,text = self.case_val(k)
        elms_s = self.get_elms(byType,cval)
        return elms_s



    #操作
    def elm_operate(self,k,textnew):
        byType,cval,optype,index,text = self.case_val(k)
        if optype == 'click':
            if index == None:
                self.get_elm(byType,cval).click()
            elif index is not None:
                self.get_elms(byType,cval)[index].click()
        elif optype == 'send_keys':
            if text == None and index == None:
                self.get_elm(byType,cval).send_keys(textnew)
            elif text is not None and index == None:
                self.get_elm(byType,cval).send_keys(text)
            elif text is not None and index is not None:
                self.get_elms(byType,cval)[index].send_keys(text)
            elif text == None and index is not None:
                self.get_elms(byType,cval)[index].send_keys(textnew)


    #存在判断
    def elm_click(self,k):
        byType,cval,optype,index,text = self.case_val(k)
        len_elms = len(self.get_elms(byType,cval))
        if len_elms>0:
            self.get_elm(byType,cval).click()
        else:
            pass

    def elm_son_click(self,m,n,c):
        try:
            byTypem,cvalm,optypem,indexm,textm = self.case_val(m)
            byTypen,cvaln,optypen,indexn,textn = self.case_val(n)
            elmson = self.driver.find_element_by_id(cvalm)
            elmsons = elmson.find_elements_by_class_name(cvaln)
            elmsons[c].click
        except Exception as e:
            print(e)
    #通用子send
    def elm_allson_send(self,m,n,index,c):
        try:
            byTypem,cvalm,optypem,indexm,textm = self.case_val(m)
            byTypen,cvaln,optypen,indexn,textn = self.case_val(n)
            elmson = self.driver.find_element(by = byTypem,value = cvalm)
            elmsons = elmson.find_elements(by = byTypen,value = cvaln)
            elmsons[index].send_keys(c)
        except Exception as e:
            print(e)

    def elm_son_send(self,m,n,index,c):
        try:
            byTypem,cvalm,optypem,indexm,textm = self.case_val(m)
            byTypen,cvaln,optypen,indexn,textn = self.case_val(n)
            elmson = self.driver.find_element_by_id(cvalm)
            elmsons = elmson.find_elements_by_class_name(cvaln)
            elmsons[index].send_keys(c)
        except Exception as e:
            print(e)
    #通用子click
    def elm_allson_click(self,m,n,index):
        try:
            byTypem,cvalm,optypem,indexm,textm = self.case_val(m)
            byTypen,cvaln,optypen,indexn,textn = self.case_val(n)
            elmson = self.driver.find_element(by = byTypem,value = cvalm)
            elmsons = elmson.find_elements(by = byTypen,value = cvaln)
            print(elmson,elmsons)
            elmsons[index].click
        except Exception as e:
            print(e)


    def get_dbtext(self,gnum,tval):
        try:
            if gnum == 0:
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%tval).click()
            elif gnum == 1:
                self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("%s")'%tval).click()
        except Exception as e:
            Log().info("元素定位失败:'%s'"%tval)
            print(e)

    #取文本值
    def get_elm_textval(self,k):
        textvala =self.elm_on(k).text
        tesval=[]
        tesval.append(textvala.strip())
        textval=tesval[0]
        return textval

    #向上滑
    def swipeup(self):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        self.driver.swipe(width/2, height/4*3, width/2, height/4, 500)
    def swipeUp(self, Driver, sd=0, x1=0, y1=0, x2=0, y2=0, t=500, n=1):
        """
        向上滑动屏幕
        :param t: 滑动持续时间
        :param n: 滑动的次数
        :sd:标记为自定义坐标：0 表示根据屏幕来算，默认点在中间； 1 表示自定义坐标
        :return:
        """
        if sd == 1:
            for i in range(n):
                Driver.swipe(x1, y1, x2, y2, t)
                time.sleep(0.3)
        else:
            l_winSize = Driver.get_window_size()
            x1 = l_winSize['width'] * 0.5  # x坐标
            y1 = l_winSize['height'] * 0.75  # 起始y坐标
            y2 = l_winSize['height'] * 0.25  # 终点y坐标
            for i in range(n):
                Driver.swipe(x1, y1, x1, y2, t)
                time.sleep(0.3)

    def swipeDown(self, Driver, sd=0, x1=0, y1=0, x2=0, y2=0, t=500, n=1):
        """
        向下滑动屏幕
        :param t:  滑动持续时间
        :param n: 滑动的次数
        :sd:标记为自定义坐标：0表示根据屏幕来算，默认点在中间； 1表示自定义坐标
        :return:
        """
        if sd == 1:
            for i in range(n):
                Driver.swipe(x1, y1, x2, y2, t)
                time.sleep(0.3)
        else:
            l_winSize = Driver.get_window_size()
            x1 = l_winSize['width'] * 0.5  # x坐标
            y1 = l_winSize['height'] * 0.25  # 起始y坐标
            y2 = l_winSize['height'] * 0.75  # 终点y坐标
            for i in range(n):
                Driver.swipe(x1, y1, x1, y2, t)
                time.sleep(0.3)
    #向下滑
    def swipedown(self):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        self.driver.swipe(width/2, height/4, width/2, height/4*3, 500)

    #左滑
    def swipeleft(self,snum):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        for k in range(snum):
            self.driver.swipe(width/4*3, height / 2, width / 4 *1, height / 2, 500)
            time.sleep(1)

    def findItem(self,el):
        time.sleep(1)
        source = self.driver.page_source
        if el in source:
            return True
        else:
            return False

    def checkItem(self,el,ea):
        if self.findItem(el):
            Log().info(ea+u"成功！")
        else:
             Log().info(ea+u"失败或超时！")

    def toast_check(self, text):
        """提示语检查"""
        try:
            message = '//*[@text=\'{}\']'.format(text)
            element = WebDriverWait(self.driver, 20, 0.1).until(lambda x: x.find_element_by_xpath(message))
            print('可以找到这个toast')
            return element.text
        except:
            print('找不到这个toast')

    # def capital_login(self):
    #     url = "http://10.10.11.132:8030/api/Test/GetLogin"
    #     header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #               "Cookie":"ASP.NET_SessionId=gxbdcnylxpwfu5hk0h03eshk; .AspNet.Bearer=iEDWbreiOjbaZUqSInJc53ubNB2SCfdEBWZ-IMjiY0adj-5ODgNZ3L1sI-v0oJKcAAzAbqB_xvrKxuBo9eDZTkQRJUbU8NdS2tkZZh3TGU6LpMGKwJlziuPLLz1ib1Op7PmPYkrLshUntdlWludi-CD56a8UwXxx9y6bHEuqmmuk0V5jDtEmVDFbjrVOLnirQvOLjgXvnZG6m-OgdW6mYwc3SlsPJBaiwb3b4Yfx9rVBBnND3wPTXDj6JbGHsszO8kNnzJLeASivG1DFUcjmrR7to59MHFptyKIQ7C6W41nQkaKy7c20yLqwXqviKuQx6brkAhHOKWdlh-uAJN9U99QoVTpMxzaJuApOl2R-0MWq-x7TdW6PfdsaYxBRWOhY0itm1Q"}
    #     requests.get(url, headers=header, verify=False)

    def capital_refresh(self):
        url = "http://10.10.11.132:8030/api/Redis/SetValueByKey"
        cookie_val = MysqlUtil().mysql_getrows("SELECT l_amount FROM `mobiletest_capitallx` WHERE capital_source='资金cookie'")
        cookie_val = cookie_val[0][0].strip()
        print(cookie_val)
        header = {"Accept": "application/json",
                  "Content-Type": "application/json",
                  "Cookie":cookie_val}
        json_data = {
              "key": "Sales_App_PartnerPollingConfig",
              "value": "",
              "minutes": 0
                     }
        requests.post(url, headers=header, data=json.dumps(json_data) , verify=False)

    # def capital_refresh(self):  # 写死
    #     url = "http://10.10.11.132:8030/api/Redis/SetValueByKey"
    #     header = {"Accept": "application/json",
    #               "Content-Type": "application/json",
    #               "Cookie":"ASP.NET_SessionId=wsp25de0s0lfuowg3jfq0n5o; .AspNet.Bearer=9bozPTSuQ6Jvb5GNygeosNNF8QYTSlYRzIx_Q6HcDKdPC6EhfOzpUWEuMtOghzYolnub9n6mk_lfAalvVUI-O5FSbNjr3jxqr-RJObmhi5rNN06uVIHLNRMV-fvzzBMlYfjd9g__HKa0ft4WdLUrWhH1Dv_f9cBaeacbCsGnJ3XTj2e4nkLXMPUCj_D952t8DGH0jZSqHC6kN_d3pNgTC-xJkPfgTM3Nsi-UX1mEPpaOb9W3Zz9ulncwudSngfe6wIdpb27M73YUherhktdE_53IrhnxBkkeuaAWXz7XMgHcFBmxnSBS3087rglB_KOyPON0Ca5_yr9KP6cPfj2t8qi-GLy7ZOlsgkpWGjmz4OIgM6ql33Krpnd_te0zIV3MPMTtjA"}
    #     json_data = {
    #           "key": "Sales_App_PartnerPollingConfig",
    #           "value": "",
    #           "minutes": 0
    #                  }
    #     requests.post(url, headers=header, data=json.dumps(json_data) , verify=False)

    def capital_sel(self,capital_val):
        try:
            if capital_val == '轮循':
                print("资金模式取数据库当前存储值，轮循切换")
                capval = MysqlUtil().mysql_getrows("SELECT t.capital_source,t.l_amount FROM mobiletest_capitallx t WHERE t.capital_source<>'资金cookie'")
                for i in range(10):
                    OracleUtil(dbname).oracle_sql("update dafy_sales.Partner_Polling_Config set limit_amount='%s' where credit_model='%s'"%(capval[i][1],capval[i][0]))
            else:
                OracleUtil(dbname).oracle_sql("update dafy_sales.Partner_Polling_Config set limit_amount=200000000 where credit_model='%s'"%capital_val)
                OracleUtil(dbname).oracle_sql("update dafy_sales.Partner_Polling_Config set limit_amount=0 where credit_model<>'%s'"%capital_val)
            self.capital_refresh()
        except Exception as e:
            Log().info("资金池刷新异常")

class RunError(ValueError): #继承ValueError
    pass