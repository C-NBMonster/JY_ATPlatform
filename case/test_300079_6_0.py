#coding=utf-8
#-------------------------------------------------------------------------------------------
#作者：吴俊威  日期：2018年10月   内容：页面一，二，三，四阶段订单合同生成，新完成到单位信息页
#--------------------------------------------------------------------------------------------
from appium import webdriver
import unittest
from mobiletest.appcomm import *
from mobiletest.appclass import *
from common.fun_t import *
from common.mysql_pub import *
from common.mysql_pubtwo import *
from common.oracle_pub import *
from common.logger import Log
import os
newcon_name="默认空箺"
con_name="测试自动化"
cpath=PATH("..\config\yaml\jyb\jybcase1.yaml")
pc_type="android模拟器"
pc_ip="127.0.0.1"
getparam={'parama': '54010000001', 'paramb': '手机', 'paramc': '即享贷D', 'paramd': '5000', 'parame': '2000', 'paramf': '保险', 'paramg': '12', 'paramh': '手机', 'parami': '华为', 'paramj': '全面保', 'paramk': '轮循', 'paraml': 's', 'paramm': 'case1'}
uname="300079"
markval="300079_6_94"
class jyb_order_300079_6_1(unittest.TestCase):
    @classmethod
    def setUpClass(cls): #运行一次
        # appclass.__init__(self,driver,cpath)
        # super(jyb_order, self).setUp()
        cls.con_name = con_name
        cls.cpath = cpath
        cls.pc_type = pc_type
        cls.pc_ip = pc_ip
        cls.getparam = getparam
        cls.uname = uname
        cls.driver = connecthub(cls.pc_type,cls.pc_ip)
        if cls.driver:
            Log().info("连接服务器成功")
        else:
            Log().info("连接服务器失败")

    @classmethod
    def tearDownClass(cls): #运行一次
        cls.driver.quit()
        pass

    def tests_pr(self):
        u'''即有宝流程测试pr合同'''
        Log().info("订单流程开始")
        time.sleep(5)
        com = appclass(self.driver,self.cpath)
        # com.capital_sel(getparam['paramk'])  #资金池--暂屏蔽
        com.swipeleft(3)
        time.sleep(1)
        com.elm_operate(0,"")
        com.elm_operate(1,self.uname)
        for x in range(2,4):
            com.elm_operate(x,"")
        time.sleep(3)
        if com.findItem("ok"):
            com.elm_operate(4,"")
        if com.findItem("开启手势密码"):
            # self.driver.tap([(0,60), (1080,210), (100, 100)], 100)
            com.elm_operate(5,"")
        if com.findItem("确定"):
            com.elm_operate(6,"")
        com.elm_operate(7,"")
        time.sleep(4)
        com.get_dbtext(1,self.getparam['parama'])
        com.elm_operate(8,"")
        time.sleep(1)
        com.get_dbtext(0,self.getparam['paramb'])
        com.elm_operate(9,"")
        time.sleep(1)
        com.get_dbtext(0,self.getparam['paramc'])

        etm=self.driver.find_element_by_id("com.giveu.corder:id/ll_item")
        etms=etm.find_elements_by_id("com.giveu.corder:id/tv_choose_right")
        time.sleep(1)
        etms[0].click()
        time.sleep(1)
        com.get_dbtext(0,self.getparam['paramh'])
        etms[1].click()
        time.sleep(1)
        com.get_dbtext(0,self.getparam['parami'])
        com.elm_operate(20,"")#商品型号
        com.elm_operate(12,self.getparam['paramd'])#商品金额
        com.elm_operate(13,self.getparam['parame']) #首付金额
        com.elm_operate(14,"")
        time.sleep(4)
        com.checkItem("选择分期","新建订单页面一下一步保存")
        #------------15,16
        if com.findItem(self.getparam['paramg']):
            com.get_dbtext(0,self.getparam['paramg'])
        else:
            com.swipeup()
            if com.findItem(self.getparam['paramg']):
                com.get_dbtext(0,self.getparam['paramg'])
            else:
                com.elm_operate(37,"")
        com.elm_operate(37,"")
        if com.findItem("请输入套餐信息"):
            com.elm_operate(84,"")
        #保险相关
        bx_one= self.driver.find_elements_by_id("com.giveu.corder:id/cb_insurance")
        bbx= self.driver.find_elements_by_id("com.giveu.corder:id/cb_treasure")
        print(bx_one)
        if getparam['paramf'] == '不参加' and len(bx_one) > 0:
            self.driver.find_element_by_id("com.giveu.corder:id/cb_insurance").click()
        elif getparam['paramf'] == '保险' and len(bbx) > 0:
            self.driver.find_element_by_id("com.giveu.corder:id/cb_treasure").click()
        else:
            print("pass")
        time.sleep(1)
        qmb= self.driver.find_elements_by_id("com.giveu.corder:id/cb_all_insurance")
        # wifi= self.driver.find_elements_by_id("com.giveu.corder:id/cb_wifi")
        sspa= self.driver.find_elements_by_id("com.giveu.corder:id/cb_broken")
        if self.getparam['paramj'] == '全面保' and len(qmb) > 0:
            self.driver.find_element_by_id("com.giveu.corder:id/cb_insurance").click()
        elif self.getparam['paramj'] == '碎碎平安' and len(sspa) > 0:
            self.driver.find_element_by_id("com.giveu.corder:id/cb_broken").click()
        else:
            print("pass")
        com.swipeup()
        com.elm_operate(23,"")
        time.sleep(4)
        com.checkItem("客户信息","新建订单页面二下一步保存")
        #拍照
        com.elm_operate(24,"")
        com.elm_operate(25,"")
        time.sleep(2)
        com.swipedown()
        com.elm_operate(26,con_name+chzw())
        textval = com.get_elm_textval(26)
        n={'name':textval}
        wryaml(PATH("..\config\yaml\jyb\dim.yaml"),n)
        time.sleep(2)
        textvall=getyaml(PATH("..\config\yaml\jyb\dim.yaml")).get('name')
        for s in range(27,41):
            com.elm_operate(s,"")
        time.sleep(1)
        com.swipeup()
        com.elm_operate(41,"")
        Log().info("订单名称：%s "%textval)
        V = OracleUtil(dbname)
        time.sleep(2)
        cnoval =V.oracle_getstring("select contract_no from cs_credit where id_person=(select id from (select * from cs_person where name like '%s%%' order by create_time desc) where rownum=1)"%textval)
        time.sleep(1)
        print(cnoval)
        A = MysqlUtil()
        time.sleep(2)
        if com.findItem("客户门店照片"):
            Log().info("订单pr合同号生成成功：%s"%cnoval)
            A.mysql_execute("INSERT INTO mobiletest_mobiledata (contract_no,con_name,con_ident,con_phone,create_time,capital_source,con_status,username,runnum,case_no) VALUES ('%s','%s','%s','%s',NOW(),'%s','%s','%s','%s','%s')"%(cnoval,textval,idcard,mobilephone,getparam['paramk'],'pr',uname,markval,getparam['paramm']))
        else:
            Log().info("订单pr合同号生成异常：%s"%cnoval)
            raise RunError('合同未生成')

    def tests_r(self): #流程测试r合同
        u'''即有宝流程测试r合同'''
        # textval = MysqlUtil().mysql_getstring("SELECT t.con_name FROM (SELECT * FROM mobiletest_mobiledata WHERE con_name LIKE '%s%%' ORDER BY create_time DESC) t LIMIT 1"%con_name) #流程测试r合同
        textvall=getyaml(PATH("..\config\yaml\jyb\dim.yaml")).get('name') #流程测试r合同
        Log().info("名称：%s"%textvall)    #流程测试r合同
        com = appclass(self.driver,self.cpath)     #流程测试r合同
        com.elm_operate(42,"")      #流程测试r合同
        time.sleep(1)    #流程测试r合同
        if self.pc_type.split('：')[0]=="android真机":      #流程测试r合同
            com.elm_operate(43,"")    #流程测试r合同
            time.sleep(2)    #流程测试r合同
            com.elm_operate(44,"")  #拍照确认   #流程测试r合同
        else:  #流程测试r合同
            com.elm_operate(82,"")  #流程测试r合同
            time.sleep(2)  #流程测试r合同
            com.elm_operate(83,"")  #拍照确认  #流程测试r合同
        com.elm_operate(54,"")  #流程测试r合同
        com.elm_operate(51,"")  #流程测试r合同
        com.elm_operate(45,"")  #流程测试r合同
        time.sleep(20)  #流程测试r合同
        com.checkItem("授权","客户信息页上传照片")  #流程测试r合同
        com.elm_operate(46,"")  #流程测试r合同
        time.sleep(10)      #等下最新验证码生成  #流程测试r合同
        if textvall.startswith('测试'):#流程测试r合同
            pcode = "741852" #流程测试r合同
        else:#流程测试r合同
            pcode =OracleUtil(dbname).oracle_getstring("select code from (select * from cs_sms_authority where mobile='%s' order by create_time desc) where rownum=1"%mobilephone)  #流程测试r合同
        time.sleep(3)  #流程测试r合同
        com.elm_operate(47,pcode) #输入验证码741852  #流程测试r合同
        com.elm_operate(48,"") #  征信授权页完成  #流程测试r合同
        time.sleep(5)  #流程测试r合同
        com.checkItem("PDF","征信授权页保存")  #流程测试r合同
        com.elm_operate(49,"")  #流程测试r合同
        time.sleep(12)  #流程测试r合同
        stpr = MysqlUtil().mysql_getstring("SELECT  con_status FROM  mobiletest_mobiledata WHERE con_name ='%s'"%textvall)#流程测试r合同
        if com.findItem("基本信息") and stpr=='pr':   #流程测试r合同
            Log().info("PDF列表页提交预审保存完成,r合同生成成功")    #流程测试r合同
            MysqlUtil().mysql_execute("UPDATE mobiletest_mobiledata SET con_status='r' WHERE con_name='%s'"%textvall)    #流程测试r合同
        else:   #流程测试r合同
            Log().info("PDF列表页提交预审,r合同生成失败")    #流程测试r合同
            raise RunError('r合同生成异常')

    def tests_s(self):  #流程测试s合同
        u'''即有宝流程测试s合同'''
        # textval = MysqlUtil().mysql_getstring("SELECT t.con_name FROM (SELECT * FROM mobiletest_mobiledata WHERE con_name LIKE '%s%%' ORDER BY create_time DESC) t LIMIT 1"%con_name)  #流程测试s合同
        textvall=getyaml(PATH("..\config\yaml\jyb\dim.yaml")).get('name')#流程测试s合同
        Log().info("名称：%s"%textvall)    #流程测试s合同
        com = appclass(self.driver,self.cpath)   #流程测试s合同
        for a in range(54,67):  #流程测试s合同
            com.elm_operate(a,"")  #流程测试s合同
        com.swipeup()  #流程测试s合同
        com.elm_operate(67,"")  #流程测试s合同
        time.sleep(4)  #流程测试s合同
        com.checkItem("单位信息","基本信息页下一步保存")  #流程测试s合同
        for b in range(68,77):  #流程测试s合同
            com.elm_operate(b,"")  #流程测试s合同
        com.swipeup()  #流程测试s合同
        for v in range(77,82):  #流程测试s合同
            com.elm_operate(v,"")  #流程测试s合同
        time.sleep(4)  #流程测试s合同
        com.checkItem("联系人","单位信息页下一步保存")  #流程测试s合同
        #-----Begin----填写联系人信息 --20181015 chenjingxu  #流程测试s合同
        #填写文本框内容 #流程测试s合同
        Log().info("开始填写联系人信息")  #流程测试s合同
        HF = "未婚"  #流程测试s合同
        com3 = appclass(self.driver, PATH("..\config\yaml\jyb\jybcase2.yaml"))  #流程测试s合同
        #填写姓名和手机号  #流程测试s合同
        if HF == "已婚":  #流程测试s合同
            for h in range(0, 7):  #流程测试s合同
                com3.elm_operate(h, "")  #流程测试s合同
        else:  #流程测试s合同
            for h in range(0, 5):  #流程测试s合同
                com3.elm_operate(h, "")  #流程测试s合同
        #选择与本人关系  #流程测试s合同
        r = 0  #流程测试s合同
        for s in range(9, 11):  #流程测试s合同
            lis = [12, 48]  #流程测试s合同
            com3.elm_operate(s, "")  #流程测试s合同
            print("没有点击打开弹窗")  #流程测试s合同
            time.sleep(0.5)  #流程测试s合同
            com3.elm_operate(lis[r], "")  #流程测试s合同
            r = r + 1  #流程测试s合同
        #提交  #流程测试s合同
        com3.elm_operate(13,"")  #流程测试s合同
        Log().info("恭喜，填写联系人信息成功！！！")  #流程测试s合同
        #第一步 填写银行卡号 #流程测试s合同
        self.driver.activate_ime_engine("com.sohu.inputmethod.sogou.xiaomi/.SogouIME")  #流程测试s合同
        com3.elm_operate(21, "")  #流程测试s合同
        self.driver.activate_ime_engine("io.appium.android.ime/.UnicodeIME")  #流程测试s合同
        com3.elm_operate(52, "")  #流程测试s合同
        com3.elm_operate(53, "")  #流程测试s合同
        time.sleep(3)  #流程测试s合同
        MysqlUtiltwo().mysql_execute("INSERT INTO credit_bankcard_four (`name`,bank_card,mobile,id_number,check_result,check_msg,sp_code,create_time,service_id,extra) VALUES ('%s','6228481359515816576','13300000000','511000198506020031','2000','全匹配','BAIRONG',NOW(),'10000',NULL)"%textvall)  #流程测试s合同
        time.sleep(2)  #流程测试s合同
        com3.elm_operate(55, "")  #流程测试s合同
        time.sleep(2)  #流程测试s合同
        send_codee =MysqlUtiltwo().mysql_getstring("SELECT t.sms_code  FROM (SELECT * FROM sms_verify_info WHERE phone = '%s' ORDER BY sent_time DESC) t  LIMIT 1"%mobilephone)  #流程测试s合同
        print(send_codee)  #流程测试s合同
        time.sleep(10)  #流程测试s合同
        c = getyaml(PATH("..\config\yaml\jyb\dim.yaml")).get('name')#流程测试s合同
        if c.startswith('测试'):#流程测试s合同
            com3.elm_operate(54,"123456")  #流程测试s合同
        else:#流程测试s合同
            com3.elm_operate(54,send_codee)  #流程测试s合同
        com3.elm_operate(15, "")  #流程测试s合同
        com3.checkItem("其他信息","绑定银行卡页保存")#流程测试s合同
        #------------------------------------断 #流程测试s合同
        #进入其他信息页  #流程测试s合同
        com3.elm_operate(32, "")  #流程测试s合同
        com3.elm_operate(33, "")  #流程测试s合同
        com3.elm_operate(34, "")  #流程测试s合同
        com3.elm_operate(15, "")  #流程测试s合同
        time.sleep(1)  #流程测试s合同
        com3.checkItem("授权","其他信息页保存")#流程测试s合同
        #跳过授权 #流程测试s合同
        com3.elm_operate(15, "")  #流程测试s合同
        com3.checkItem("小问卷","跳过授权保存")#流程测试s合同
        #小问卷 #流程测试s合同
        # com3.elm_operate(36, "")  #流程测试s合同
        com3.elm_operate(37, "")  #流程测试s合同
        com3.elm_operate(51, "")  #流程测试s合同
        com3.checkItem("影像证明","小问卷保存")#流程测试s合同
        #上传影像证明 #流程测试s合同
        com3.swipedown() #流程测试s合同
        com3.elm_operate(38, "")  #流程测试s合同
        com3.elm_operate(39, "")  #流程测试s合同
        com3.elm_operate(40, "")  #流程测试s合同
        time.sleep(2)  #流程测试s合同
        self.driver.wait_activity("com.giveu.corder.ordercreate.activity.PhotoCertificateActivity", 20, 1)  #流程测试s合同
        com3.swipeup()  #流程测试s合同
        com3.elm_operate(41, "")  #提交 #流程测试s合同
        com3.elm_operate(42, "")  #流程测试s合同
        com3.elm_operate(43, "")  #流程测试s合同
        time.sleep(2)  #流程测试s合同
        sta = MysqlUtil().mysql_getstring("SELECT  con_status FROM  mobiletest_mobiledata WHERE con_name ='%s'"%textvall)#流程测试s合同
        if com3.findItem("成功提交") and sta=='r':   #流程测试s合同
            Log().info("即有宝S合同生成成功")    #流程测试s合同
            MysqlUtil().mysql_execute("UPDATE mobiletest_mobiledata SET con_status='s' WHERE con_name='%s'"%textvall)    #流程测试s合同
        else:   #流程测试s合同
            Log().info("即有宝S合同生成失败")    #流程测试s合同






if __name__ == "__main__":
    unittest.main()