#coding=utf-8
#-------------------------------------------------------------------------------------------
#作者：吴俊威  日期：2018年10月   内容：页面一，二，三，四阶段订单合同生成，新完成到单位信息页
#--------------------------------------------------------------------------------------------
from appium import webdriver
# import time
import unittest
from mobiletest.appcomm import *
from mobiletest.appclass import *
from common.fun_t import *
from common.mysql_pub import *
from common.mysql_pubtwo import *
from common.oracle_pub import *
from common.logger import Log
import os
# from common.adb_t import *
# import urllib.request
# from urllib.error import URLError
cpath = PATH("..\config\yaml\jyb\jybcase1.yaml")

class jyb_order(unittest.TestCase):
    log = Log()

    def __init__(self,con_name,driver,cpath,pc_type,pc_ip,getparam,i):
        # appclass.__init__(self,driver,cpath)
        self.com = appclass()
        self.con_name = con_name
        self.com.driver = driver
        self.cpath = cpath
        self.pc_type = pc_type
        self.pc_ip = pc_ip
        self.getparam = getparam
        self.i = i

    def test_connect(self,pc_type,pc_ip):
        u'''服务器连接'''
        driver = connecthub(pc_type,pc_ip)
        if driver:
            Log().info("连接服务器成功")
        else:
            Log().info("连接服务器失败")
        time.sleep(5)



    def test_login(self):
        u'''测试登录'''
        self.com.swipeleft(3)
        time.sleep(1)
        for x in range(4):
            self.com.elm_operate(x,"")
        time.sleep(1)
        Log().info("登录成功")

    def test_orderone(self):
        u'''订单页面一'''
        for z in range(4,7):
            self.com.elm_click(z)
        self.com.elm_operate(7,"")
        time.sleep(4)
        self.com.get_dbtext(1,self.getparam[self.i]['parama'])
        self.com.elm_operate(8,"")
        time.sleep(1)
        self.com.get_dbtext(0,self.getparam[self.i]['paramb'])
        self.com.elm_operate(9,"")
        time.sleep(1)
        self.com.get_dbtext(0,self.getparam[self.i]['paramc'])
        self.com.elm_operate(10,"")
        time.sleep(1)
        self.com.elm_operate(11,"")
        self.com.elm_allson_send(12,13,0,self.getparam[self.i]['paramd'])
        self.com.elm_allson_send(12,13,1,self.getparam[self.i]['parame'])
        self.com.elm_operate(14,"")
        Log().info("订单页面一完成")

    def test_ordertwo(self):
        u'''订单页面二'''
        bx_one= self.driver.find_elements_by_id("com.giveu.corder:id/switch_insurance")
        bbx= self.driver.find_elements_by_id("com.giveu.corder:id/switch_treasure")
        print(bx_one)
        if self.getparam[self.i] == '不参加' and len(bx_one) > 0:
            self.driver.find_element_by_id("com.giveu.corder:id/switch_insurance").click()
        elif self.getparam[self.i]['paramf'] == '免还大礼包' and len(bbx) > 0:
            self.driver.find_element_by_id("com.giveu.corder:id/switch_treasure").click()
        else:
            print("pass")
        time.sleep(2)
        self.com.get_dbtext(0,self.getparam[self.i]['paramg'])
        self.com.swipeup()
        self.com.elm_operate(17,"")
        Log().info("订单页面二完成")
        self.com.driver.quit()


    # def tearDown(self):
    #     self.driver.quit()
if __name__ == "__main__":
    unittest.main()



# def app_run_test(getid):
#     Log().info("即有宝提单开始执行")
#     try:
#         con_name,con_num,pc_type,pc_ip = getrun_db(getid)
#         for j in range(con_num):
#             try:
#                 getparam,paramcount = param_db()
#                 print("统计行:%s"%paramcount)
#                 for i in range(paramcount):
#                     try:
#                         driver = connecthub(pc_type,pc_ip)
#                         if driver:
#                             Log().info("连接服务器成功")
#                         else:
#                             Log().info("连接服务器失败")
#                         time.sleep(5)
#                         com = appclass(driver,cpath)
#                         com.swipeleft(3)
#                         time.sleep(1)
#                         for x in range(4):
#                             com.elm_operate(x,"")
#                         time.sleep(1)
#                         for z in range(4,7):
#                             com.elm_click(z)
#                         com.elm_operate(7,"")
#                         time.sleep(4)
#                         com.get_dbtext(1,getparam[i]['parama'])
#                         com.elm_operate(8,"")
#                         time.sleep(1)
#                         com.get_dbtext(0,getparam[i]['paramb'])
#                         com.elm_operate(9,"")
#                         time.sleep(1)
#                         com.get_dbtext(0,getparam[i]['paramc'])
#                         com.elm_operate(10,"")
#                         time.sleep(1)
#                         com.elm_operate(11,"")
#                         com.elm_allson_send(12,13,0,getparam[i]['paramd'])
#                         com.elm_allson_send(12,13,1,getparam[i]['parame'])
#                         com.elm_operate(14,"")
#                         Log().info("订单页面一完成")
#                         #------------15,16
#                         bx_one= driver.find_elements_by_id("com.giveu.corder:id/switch_insurance")
#                         bbx= driver.find_elements_by_id("com.giveu.corder:id/switch_treasure")
#                         print(bx_one)
#                         if getparam[i]['paramf'] == '不参加' and len(bx_one) > 0:
#                             driver.find_element_by_id("com.giveu.corder:id/switch_insurance").click()
#                         elif getparam[i]['paramf'] == '免还大礼包' and len(bbx) > 0:
#                             driver.find_element_by_id("com.giveu.corder:id/switch_treasure").click()
#                         else:
#                             print("pass")
#                         time.sleep(2)
#                         com.get_dbtext(0,getparam[i]['paramg'])
#                         com.swipeup()
#                         com.elm_operate(17,"")
#                         Log().info("订单页面二完成")
#                         etm=driver.find_element_by_id("com.giveu.corder:id/ll_item")
#                         etms=etm.find_elements_by_id("com.giveu.corder:id/tv_choose_right")
#                         time.sleep(1)
#                         # com.elm_allson_click(18,19,0)
#                         etms[0].click()
#                         time.sleep(1)
#                         com.get_dbtext(0,getparam[i]['paramh'])
#                         # com.elm_allson_click(18,19,1)
#                         etms[1].click()
#                         time.sleep(1)
#                         com.get_dbtext(0,getparam[i]['parami'])
#                         com.elm_operate(20,"")
#                         #预留21,22
#                         qmb= driver.find_elements_by_id("com.giveu.corder:id/cb_insurance")
#                         sspa=driver.find_elements_by_id("com.giveu.corder:id/cb_broken")
#                         if getparam[i]['paramj'] == '全面保' and len(qmb) > 0:
#                             driver.find_element_by_id("com.giveu.corder:id/cb_insurance").click()
#                         elif getparam[i]['paramj'] == '碎碎平安' and len(sspa) > 0:
#                             driver.find_element_by_id("com.giveu.corder:id/cb_broken").click()
#                         else:
#                             print("pass")
#                         com.swipeup()
#                         com.elm_operate(23,"")
#                         Log().info("订单页面三完成")
#                         #拍照
#                         com.elm_operate(24,"")
#                         com.elm_operate(25,"")
#                         time.sleep(2)
#                         com.elm_operate(26,con_name+chzw())
#                         textval = com.get_elm_textval(26)
#                         for s in range(27,41):
#                             com.elm_operate(s,"")
#                         time.sleep(1)
#                         com.swipeup()
#                         com.elm_operate(41,"")
#                         Log().info("订单：%s  已生成"%textval)
#                         V = OracleUtil(dbname)
#                         time.sleep(2)
#                         cnoval =V.oracle_getstring("select contract_no from cs_credit where id_person=(select id from (select * from cs_person where name like '%s%%' order by create_time desc) where rownum=1)"%textval)
#                         time.sleep(1)
#                         print(cnoval)
#                         A = MysqlUtil()
#                         time.sleep(2)
#                         A.mysql_execute("INSERT INTO mobiletest_mobiledata (contract_no,con_name,con_ident,con_phone,create_time) VALUES ('%s','%s','%s','%s',NOW())"%(cnoval,textval,idcard,mobilephone))
#                         Log().info("订单合同号：%s"%cnoval)
#                         #预留1
#                         com.elm_operate(42,"")
#                         time.sleep(1)
#                         com.elm_operate(43,"")
#                         time.sleep(2)
#                         com.elm_operate(44,"")  #拍照确认
#                         com.elm_operate(45,"")
#                         Log().info("客户门店照片页完成")
#                         com.elm_operate(46,"")
#                         time.sleep(10)      #等下最新验证码生成
#                         pcode =V.oracle_getstring("select code from (select * from cs_sms_authority where mobile='%s' order by create_time desc) where rownum=1"%mobilephone)
#                         time.sleep(2)
#                         com.elm_operate(47,pcode) #输入验证码
#                         com.elm_operate(48,"") #  征信授权页完成
#
#                         Log().info("征信授权页完成")
#
#                         com.elm_operate(49,"")
#                         Log().info("PDF列表页面完成")
#                         com.elm_operate(50,"")
#                         com.elm_operate(51,"")
#                         com.elm_operate(52,"")
#                         com.elm_operate(53,"")
#
#                         Log().info("其他信息页完成")
#                         for a in range(54,67):
#                             com.elm_operate(a,"")
#
#                         swipeup(driver)
#                         com.elm_operate(67,"")
#                         Log().info("基本信息页完成")
#
#                         for b in range(68,77):
#                             com.elm_operate(b,"")
#                         swipeup(driver)
#                         for v in range(77,82):
#                             com.elm_operate(v,"")
#
#                         Log().info("单位信息页完成")
#
#                         driver.quit()
#                     except Exception as e:
#                         print(e)
#             except Exception as e:
#                 print(e)
#         A.mysql_close()
#     except Exception as e:
#         print(e)
