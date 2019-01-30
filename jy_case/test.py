# -*- coding:utf-8 -*-

from appium.webdriver import *
import time
from mobiletest.models import *
from common.fun_t import *
from mobiletest.appcomm import *
# desired_caps = getcaps('android真机')
import os
import shutil
from selenium.webdriver import *
import re
import unittest
import requests
import json
from common.logger import Log
from mobiletest.appclass import *
from time import strftime, localtime
# for i in range(1):
#     # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     driver = connecthub('android真机','127.0.0.1')
#     time.sleep(5)
#     swipeleft(driver,3)
#     byType,cval,optype,index,text = case_val(1)
#     # print(byType,cval)
#     # get_elm(driver,byType,cval).click()
#     # driver.find_element_by_id("com.giveu.corder:id/tv_into").click()
#     print(elm_on(driver,0))
#     print(len(elms_on(driver,0)))
#     elm_operate(driver,0,"")
#
#     elm_operate(driver,1,"")
#     elm_operate(driver,2,"")
#     elm_operate(driver,3,"")
#
#     # get_elm(driver,byType,cval).send_keys(text)
#     # get_elm(driver,"id","com.giveu.corder:id/et_account").send_keys("842928")
#     # driver.find_element_by_id("com.giveu.corder:id/et_account").send_keys("842928")
#     # driver.find_element_by_id("com.giveu.corder:id/et_pwd").send_keys("123456")
#     # driver.find_element_by_id("com.giveu.corder:id/tv_login").click()
#     time.sleep(3)
#
#     if findItem(driver,"暂不"):
#         Log().info("登录成功！")
#     else:
#         Log().info("登录失败！")

# from run_main import *
# # class testa():
# #
# #     def testv(self,b):
# #         a=b+1
# #         return a
#
# for b in range(3):
#     b = b
#     all_case = add_case()
#     run_case(all_case)
#     # report_path = os.path.join(cur_path, "report")
#     # print(report_path)
#     # report_file = get_report_file(report_path)

# filep = PATH("../case/test_")+str(2)+"_"+str(0)+".py"
# # replace_string(filep,filep,"con_name=\"测试\"","con_name=\"自动化\"")
# # remove_lines(PATH("../jy_case/jyb_temp.py"),filep,"#默认误删")
# # remove_lines(filep,filep,"流程测试s合同")
# now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
# # now = time.strftime("%Y_%m_%d_%H_%M_%S")
# print(now)

# ------------------------
# a=['挖财-)达飞 放款回单大萨达所(','是是是挖财-达飞( 放款回单羊肉汤犹太人)','范德萨发生发的)-挖财-达飞-- )(放款回单)','达飞发顺丰的挖财搜索放款回单']
# a_list=[]
# for i in a:
#     if re.findall('.*挖财.*达飞.*放款回单.*',i) or re.findall('.*达飞.*挖财.*放款回单.*',i):
#         a_list.append(i)
# print(a_list)
# --------------------
# for i in range(3):
#     lval=list(filter(lambda x:x!=a[i],a))
#     print(lval)
#------------------------
# http://10.10.11.132:8030/api/Redis/SetValueByKey
#
# Host: 10.10.11.132:8030
# Connection: keep-alive
# Content-Length: 80
# Accept: application/json
# Origin: http://10.10.11.132:8030
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
# Content-Type: application/json
# Referer: http://10.10.11.132:8030/swagger/ui/index
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
# Cookie: ASP.NET_SessionId=gxbdcnylxpwfu5hk0h03eshk; .AspNet.Bearer=iEDWbreiOjbaZUqSInJc53ubNB2SCfdEBWZ-IMjiY0adj-5ODgNZ3L1sI-v0oJKcAAzAbqB_xvrKxuBo9eDZTkQRJUbU8NdS2tkZZh3TGU6LpMGKwJlziuPLLz1ib1Op7PmPYkrLshUntdlWludi-CD56a8UwXxx9y6bHEuqmmuk0V5jDtEmVDFbjrVOLnirQvOLjgXvnZG6m-OgdW6mYwc3SlsPJBaiwb3b4Yfx9rVBBnND3wPTXDj6JbGHsszO8kNnzJLeASivG1DFUcjmrR7to59MHFptyKIQ7C6W41nQkaKy7c20yLqwXqviKuQx6brkAhHOKWdlh-uAJN9U99QoVTpMxzaJuApOl2R-0MWq-x7TdW6PfdsaYxBRWOhY0itm1Q
# {
#   "key": "Sales_App_PartnerPollingConfig",
#   "value": "",
#   "minutes": 0
# }
#------------------------
#	ASP.NET_SessionId=gxbdcnylxpwfu5hk0h03eshk
#	.AspNet.Bearer=iEDWbreiOjbaZUqSInJc53ubNB2SCfdEBWZ-IMjiY0adj-5ODgNZ3L1sI-v0oJKcAAzAbqB_xvrKxuBo9eDZTkQRJUbU8NdS2tkZZh3TGU6LpMGKwJlziuPLLz1ib1Op7PmPYkrLshUntdlWludi-CD56a8UwXxx9y6bHEuqmmuk0V5jDtEmVDFbjrVOLnirQvOLjgXvnZG6m-OgdW6mYwc3SlsPJBaiwb3b4Yfx9rVBBnND3wPTXDj6JbGHsszO8kNnzJLeASivG1DFUcjmrR7to59MHFptyKIQ7C6W41nQkaKy7c20yLqwXqviKuQx6brkAhHOKWdlh-uAJN9U99QoVTpMxzaJuApOl2R-0MWq-x7TdW6PfdsaYxBRWOhY0itm1Q
# def capital_refresh():
#     url = "http://10.10.11.132:8030/api/Redis/SetValueByKey"
#     header = {"Accept": "application/json",
#               "Content-Type": "application/json",
#               "Cookie":"ASP.NET_SessionId=gxbdcnylxpwfu5hk0h03eshk; .AspNet.Bearer=iEDWbreiOjbaZUqSInJc53ubNB2SCfdEBWZ-IMjiY0adj-5ODgNZ3L1sI-v0oJKcAAzAbqB_xvrKxuBo9eDZTkQRJUbU8NdS2tkZZh3TGU6LpMGKwJlziuPLLz1ib1Op7PmPYkrLshUntdlWludi-CD56a8UwXxx9y6bHEuqmmuk0V5jDtEmVDFbjrVOLnirQvOLjgXvnZG6m-OgdW6mYwc3SlsPJBaiwb3b4Yfx9rVBBnND3wPTXDj6JbGHsszO8kNnzJLeASivG1DFUcjmrR7to59MHFptyKIQ7C6W41nQkaKy7c20yLqwXqviKuQx6brkAhHOKWdlh-uAJN9U99QoVTpMxzaJuApOl2R-0MWq-x7TdW6PfdsaYxBRWOhY0itm1Q"}
#     json_data = {
#           "key": "Sales_App_PartnerPollingConfig",
#           "value": "",
#           "minutes": 0
#                  }
#     requests.post(url, headers=header, data=json.dumps(json_data) , verify=False)
# capital_refresh()
# def test_CY():
#     u'''测试CY合同贷款申请单'''
#     url = "http://10.10.11.132:8030/api/Redis/SetValueByKey"
#     header = {"Host": "10.10.11.132:8030",
#             "Connection": "keep-alive",
#             "Content-Length": "80",
#             "Accept": "application/json",
#             "Origin": "http://10.10.11.132:8030",
#             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
#             "Content-Type": "application/json",
#             "Referer": "http://10.10.11.132:8030/swagger/ui/index",
#             "Accept-Encoding": "gzip, deflate",
#             "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#               "Cookie":"ASP.NET_SessionId=gxbdcnylxpwfu5hk0h03eshk; .AspNet.Bearer=iEDWbreiOjbaZUqSInJc53ubNB2SCfdEBWZ-IMjiY0adj-5ODgNZ3L1sI-v0oJKcAAzAbqB_xvrKxuBo9eDZTkQRJUbU8NdS2tkZZh3TGU6LpMGKwJlziuPLLz1ib1Op7PmPYkrLshUntdlWludi-CD56a8UwXxx9y6bHEuqmmuk0V5jDtEmVDFbjrVOLnirQvOLjgXvnZG6m-OgdW6mYwc3SlsPJBaiwb3b4Yfx9rVBBnND3wPTXDj6JbGHsszO8kNnzJLeASivG1DFUcjmrR7to59MHFptyKIQ7C6W41nQkaKy7c20yLqwXqviKuQx6brkAhHOKWdlh-uAJN9U99QoVTpMxzaJuApOl2R-0MWq-x7TdW6PfdsaYxBRWOhY0itm1Q"}
#     json_data = {
#           "key": "Sales_App_PartnerPollingConfig",
#           "value": "",
#           "minutes": 0
#                  }
#     requests.post(url, headers=header, data=json.dumps(json_data) , verify=False)
# test_CY()


# import os,re
# pdf_list = os.listdir("../ccc")
# for temp in pdf_list:
#     for t in os.listdir("../ccc/"+temp):
#         if re.findall('证据7',t):
#             os.rename("../ccc/"+temp+"/"+t,"../ccc/"+temp+"/"+'证据7：挖财到达飞放款回单'+'.pdf')
#         if re.findall('证据8',t):
#             os.rename("../ccc/"+temp+"/"+t,"../ccc/"+temp+"/"+'证据8：达飞到挖财代偿回单'+'.pdf')
#         if re.findall('证据10',t):
#             os.rename("../ccc/"+temp+"/"+t,"../ccc/"+temp+"/"+'证据10：达飞VS挖财网合作协议'+'.pdf')
#         print(t)
#cookie
#	ASP.NET_SessionId=1x2i4gynzq0scqyk3f2svdab
#	.AspNet.Bearer=9qJDVTkxq2WP7R6_iaiRmqahYD9hF6wCutGzXMzqs-J0w5fzw8Ajn6jKm4AqL1AdmfLeFqIVrQWpjwTHgcOnqEl6apa37l4IXfyCc4DEqLCsgVoO0BuBWGeTyksc5-MOUy6wh8HeS8NEBijrQMKct2-NBVsz16UQUS95lpiuNKulsCaB3vuS5Y9BcGNfqGT4rYutptsvak9NuHtJfj7CSacK5LfyGUB57XWllVihfNaAT4Aj5oxCElsUQN5JemfXOCJL1uOZEeEa8fIIlk-qO2XNG5L9B3n_ZJbXVXKPM5jxr3qWrTfgEXM8FD6LIGtES2i84sXkBBrBqOFtmOxLroExzzw
#验证码
#	ASP.NET_SessionId=1x2i4gynzq0scqyk3f2svdab
#	.AspNet.Bearer=asx6XBbVrGbYUJ-apiS7AYZOWUFZ-Zg__aJJdbJJ51wuhJVLQjwcA7e94uLcVHkQ3PQCRrhQ1Up5jiihMG5N8YpahnNwvD_FmDifCYQAgQOg7Z9f80hxHhBzqdsy7LuCI-53SBhpNGlRgEjobjtrCw2expxHwCYD7XLIMp-HDo2aNdggGMMcu4H7w3Jp28Ocy4gLfq9QULyItL1WXVdkHd4RLjdOd7n1neNkhGSc2nIrHZkbkRwRsotpIgQpRs9KHES-raAMGV3Jkeln1ziBqmBvku5F7oadZ9xJMT4vQU94qkRok3HgX2vhQy15GcMSRySjEc2Hb6v4syprtri1mseLnSQMBh1AA5VcxuH6MDjjusfGvYp7cPMkrntDZv10wBsQBZMsvGtQLzhWMF0Zc6fnJQ8

#	ASP.NET_SessionId=1x2i4gynzq0scqyk3f2svdab
#	.AspNet.Bearer=mOrCSrTjL4rR3DdnIc-usjBus_hLM9ZQoKQah0RCerMXQQ5xeVsg4zFz2VNs9mHB2kz0CposS9LCfofsa7vEPTFLVwn9gfH61mYZGNXMe0i4U9-M3fCHfvAy-KAU_u92vZGGs8H0z6tBAi0vOtgxx3kzED91izbocH5u-2dAsYWu8uYiEtt8caw61cmC-m7wCBZFNoUBY8yNYTQUsQfwxOUxb5FyF0Fh3PHSgUT_hAULM2_DdcErMV39R2pYfo2pwU7wqOjXi76slilHT1P2fcsOPjuFJt-mJcc_AK9cHXK5FoR86mHNsziXHjIaWjw3jb0n_bgf-QYVChK-U78ZuQ-QJZ4ZyfP_lb4J542LUcDiuwuPYaC9F2sYqzn0Fl_ZEe9Yzw


# def capital_login():
#     url = "http://10.10.11.132:8030/api/Test/GetLogin"
#     header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
#               "Cookie": "ASP.NET_SessionId=3f4t3ss2tkte2f1a4moth4ey; .AspNet.Bearer=YbLU5kBbgoggUfXUW97_p9lTwtKFDrTULy3NEkGp3MgUSx3pdOXrjEpjQsNSoFtSy24Xr8ua90uSXpqZBfXE3nUAAxPKIuaaGENammg61_vsLZrA14KbKkKseUNaJo3xvgDjhnXygaBqyJc0qI8fqG6jUYZCzpp8v101rpDGy6NSvu7s6IObhzDK0TSh8aUPopDIbp6K5N3KyEBDeoYW8FSV0tiMQGKE38ekPlqRjnAlVTbcjxA_yI1fLMLH_z35AIV4lIFmvu82EzDGIs7gelTMeP7bfGhLj26Bp2PkIEN_TzfQT1xWyIakpPtRBXHM9wvm1A3bEAaDHOCufTU89YONpG1aXFUKfXkZw-EeLQUk9sWZck2LXcnHnnkjMaBXAzzYRA"
# }
#     r=requests.get(url, headers=header, verify=False)
#     print(r.content)
#
# def capital_refresh():
#     url = "http://10.10.11.132:8030/api/Redis/SetValueByKey"
#     header = {"Accept": "application/json",
#               "Content-Type": "application/json"}
#               # "Cookie":"ASP.NET_SessionId=gxbdcnylxpwfu5hk0h03eshk; .AspNet.Bearer=iEDWbreiOjbaZUqSInJc53ubNB2SCfdEBWZ-IMjiY0adj-5ODgNZ3L1sI-v0oJKcAAzAbqB_xvrKxuBo9eDZTkQRJUbU8NdS2tkZZh3TGU6LpMGKwJlziuPLLz1ib1Op7PmPYkrLshUntdlWludi-CD56a8UwXxx9y6bHEuqmmuk0V5jDtEmVDFbjrVOLnirQvOLjgXvnZG6m-OgdW6mYwc3SlsPJBaiwb3b4Yfx9rVBBnND3wPTXDj6JbGHsszO8kNnzJLeASivG1DFUcjmrR7to59MHFptyKIQ7C6W41nQkaKy7c20yLqwXqviKuQx6brkAhHOKWdlh-uAJN9U99QoVTpMxzaJuApOl2R-0MWq-x7TdW6PfdsaYxBRWOhY0itm1Q"}
#     json_data = {
#           "key": "Sales_App_PartnerPollingConfig",
#           "value": "",
#           "minutes": 0
#                  }
#     r=requests.post(url, headers=header, data=json.dumps(json_data) , verify=False)
#     print(r.raw)
#
#
# # capital_login()
#
# capital_refresh()
#

# print(u"\u8fd0\u884c\u5b8c\u6210")
# pc_type='android真机:小米6.0.1'
# pc_type=pc_type.split(':')[0]
# print(pc_type)
# #文件路径
# print("获取当前文件路径——" + os.path.realpath(__file__))  # 获取当前文件路径
# parent = os.path.dirname(os.path.realpath(__file__))
# print("获取其父目录——" + parent)  # 从当前文件路径中获取目录
# garder = os.path.dirname(parent)
# print("获取父目录的父目录——" + garder)
# print("获取文件名" + os.path.basename(os.path.realpath(__file__)))  # 获取文件名
# # 当前文件的路径
# pwd = os.getcwd()
# print("当前运行文件路径" + pwd)
# # 当前文件的父路径
# father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
# print("运行文件父路径" + father_path)
# # 当前文件的前两级目录
# grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
# print("运行文件父路径的父路径" + grader_father)

#
    # pathcname=os.path.realpath(__file__)
    # print(pathcname)
    # remove_lines(PATH(pathcname),PATH(pathcname),"#待修改con_name")
    # with open(pathcname,'r',encoding='UTF-8') as ui:
    #     data = ui.readlines()
    # for inx,line in enumerate(data):
    #     if inx == 15:
    #         val = str("con_name=")+"\""+str("自动化测试地点")+"\""+"\n"
    #         data[inx] = val
    # with open(pathcname,'w',encoding='UTF-8') as oi:
    #     oi.writelines(data)
# print(getyaml(PATH("..\config\yaml\jyb\dim.yaml")).get('name'))
# x="=="
# print(x)
#
# c="SELECT con_name,con_phone FROM mobiletest_mobiledata WHERE contract_no='21094010001'"
#
# c.replace('\'','\"')
# re.sub(r'[\']','a',c)
# print(c)

# class IntegerArithmeticTestCase(unittest.TestCase):
#     def testAdd(self):  # test method names begin with 'test'
#         self.assertEqual((1 + 2), 3)
#         self.assertEqual(0 + 1, 1)
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 40)
#
# if __name__ == '__main__':
#     unittest.main()


# def vv(b):
#     list=['=','!=','>','<']
#     c=[x for x in list if x==b]
#     print(c[0])
#!=  assertNotEqual   > assertGreater < assertLess
# def checkdb(first,second,ctype):
#     if first==second and '='==ctype:
#         return True
#     if first!=second and '!='==ctype:
#         return True
#     if first>second and '>'==ctype:
#         return True
#     if first<second and '<'==ctype:
#         return True
#     if '=='==ctype and first==second:
#         return True
#     else:
#         return False
#
# def sel_db(dname,sql):#选择数据库执行
#     if dname == "oracle":
#         orc_val = OracleUtil(dbname).oracle_getrows(sql)
#         return orc_val
#     if dname == "mysql":
#         mysql_val = MysqlUtil().mysql_getrows(sql)
#         return mysql_val
#     else:
#         return False
# tt = strftime('%Y-%m-%d %H:%M:%S',localtime())
# print(tt)
# print (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# lgetparam={'param_phone': '13300000000', 'param_pwd': '123456', 'param_name': '测试', 'param_idNo': '110102198506020034', 'param_bcard': '工商银行', 'param_cardNo': '6217000333344440001', 'param_ppwd': '111111', 'case_no': 'case1'}#默认误删
# print(lgetparam['param_phone'])
# lgetparam['param_phone']  lgetparam['param_pwd'] lgetparam['param_name'] lgetparam['param_idNo'] lgetparam['param_bcard'] lgetparam['param_cardNo'] lgetparam['param_ppwd']

vala = getyaml(PATH("..\config\yaml\jycash\capsloan.yaml"))
capval = vala[pc_type][0]