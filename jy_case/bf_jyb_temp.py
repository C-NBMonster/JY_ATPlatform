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
cpath = PATH("..\config\yaml\jyb\jybcase1.yaml")   #默认误删
con_name="回归" #默认误删
pc_type="android真机" #默认误删
pc_ip="127.0.0.1" #默认误删
getparam={'parama': '42010000200', 'paramb': '电脑', 'paramc': '即享贷A', 'paramd': '4000', 'parame': '1000', 'paramf': '百宝箱', 'paramg': '6', 'paramh': '台式电脑', 'parami': '苹果', 'paramj': '不参加'} #默认误删
class jyb_order(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # appclass.__init__(self,driver,cpath)
        # super(jyb_order, self).setUp()
        cls.con_name = con_name
        cls.cpath = cpath
        cls.pc_type = pc_type
        cls.pc_ip = pc_ip
        cls.getparam = getparam
        cls.driver = connecthub(cls.pc_type,cls.pc_ip)
        if cls.driver:
            Log().info("连接服务器成功")
        else:
            Log().info("连接服务器失败")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def tests_pr(self):
        u'''即有宝流程测试pr合同'''
        Log().info("订单流程开始")
        time.sleep(5)
        com = appclass(self.driver,self.cpath)
        com.swipeleft(3)
        time.sleep(1)
        for x in range(4):
            com.elm_operate(x,"")
        time.sleep(3)
        for z in range(4,7):   #300079wei4 842928wei5
            com.elm_click(z)
            time.sleep(0.5)
        com.elm_operate(7,"")
        time.sleep(4)
        com.get_dbtext(1,self.getparam['parama'])
        com.elm_operate(8,"")
        time.sleep(1)
        com.get_dbtext(0,self.getparam['paramb'])
        com.elm_operate(9,"")
        time.sleep(1)
        com.get_dbtext(0,self.getparam['paramc'])
        com.elm_operate(10,"")
        time.sleep(1)
        com.elm_operate(11,"")
        com.elm_allson_send(12,13,0,self.getparam['paramd'])
        com.elm_allson_send(12,13,1,self.getparam['parame'])
        com.elm_operate(14,"")
        time.sleep(4)
        com.checkItem("选择分期","新建订单页面一下一步保存")
        #------------15,16
        bx_one= self.driver.find_elements_by_id("com.giveu.corder:id/switch_insurance")
        bbx= self.driver.find_elements_by_id("com.giveu.corder:id/switch_treasure")
        print(bx_one)
        if getparam['paramf'] == '不参加' and len(bx_one) > 0:
            self.driver.find_element_by_id("com.giveu.corder:id/switch_insurance").click()
        elif getparam['paramf'] == '保险' and len(bbx) > 0:
            self.driver.find_element_by_id("com.giveu.corder:id/switch_treasure").click()
        else:
            print("pass")
        time.sleep(2)
        com.get_dbtext(0,self.getparam['paramg'])
        com.swipeup()
        com.elm_operate(17,"")
        time.sleep(4)
        com.checkItem("商品类型","新建订单页面二下一步保存")
        etm=self.driver.find_element_by_id("com.giveu.corder:id/ll_item")
        etms=etm.find_elements_by_id("com.giveu.corder:id/tv_choose_right")
        time.sleep(1)
        # com.elm_allson_click(18,19,0)
        etms[0].click()
        time.sleep(1)
        com.get_dbtext(0,self.getparam['paramh'])
        # com.elm_allson_click(18,19,1)
        etms[1].click()
        time.sleep(1)
        com.get_dbtext(0,self.getparam['parami'])
        com.elm_operate(20,"")
        #预留21,22
        qmb= self.driver.find_elements_by_id("com.giveu.corder:id/cb_insurance")
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
        com.checkItem("身份证","新建订单页面三下一步保存")
        #拍照
        com.elm_operate(24,"")
        com.elm_operate(25,"")
        time.sleep(2)
        com.elm_operate(26,con_name+chzw())
        textval = com.get_elm_textval(26)
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
        A.mysql_execute("INSERT INTO mobiletest_mobiledata (contract_no,con_name,con_ident,con_phone,create_time) VALUES ('%s','%s','%s','%s',NOW())"%(cnoval,textval,idcard,mobilephone))
        if cnoval==None:
            Log().info("订单pr合同号生成异常：%s"%cnoval)
        else:
            Log().info("订单pr合同号生成成功：%s"%cnoval)
        # return textval

    def tests_s(self):
        u'''即有宝流程测试s合同'''
        # textval = self.tests_pr()
        textval = MysqlUtil().mysql_getstring("SELECT t.con_name FROM (SELECT * FROM mobiletest_mobiledata WHERE con_name LIKE '%s%%' ORDER BY create_time DESC) t LIMIT 1"%con_name)
        print(textval)
        com = appclass(self.driver,self.cpath)
        com.elm_operate(42,"")
        time.sleep(1)
        if self.pc_type=="android真机":
            com.elm_operate(43,"")
            time.sleep(2)
            com.elm_operate(44,"")  #拍照确认
        else:
            com.elm_operate(82,"")
            time.sleep(2)
            com.elm_operate(83,"")  #拍照确认
        com.elm_operate(45,"")
        time.sleep(20)
        com.checkItem("授权","客户信息页上传照片")
        com.elm_operate(46,"")
        time.sleep(10)      #等下最新验证码生成
        pcode =OracleUtil(dbname).oracle_getstring("select code from (select * from cs_sms_authority where mobile='%s' order by create_time desc) where rownum=1"%mobilephone)
        time.sleep(3)
        com.elm_operate(47,pcode) #输入验证码
        com.elm_operate(48,"") #  征信授权页完成
        time.sleep(4)
        com.checkItem("签章","征信授权页下一步保存")
        com.elm_operate(49,"")
        time.sleep(3)
        com.checkItem("其他信息","PDF列表页下一步保存")
        com.elm_operate(50,"")
        com.elm_operate(51,"")
        com.elm_operate(52,"")
        com.elm_operate(53,"")
        time.sleep(4)
        com.checkItem("基本信息","其他信息页下一步保存")
        for a in range(54,67):
            com.elm_operate(a,"")
        com.swipeup()
        com.elm_operate(67,"")
        time.sleep(4)
        com.checkItem("单位信息","基本信息页下一步保存")
        for b in range(68,77):
            com.elm_operate(b,"")
        com.swipeup()
        for v in range(77,82):
            com.elm_operate(v,"")
        time.sleep(4)
        com.checkItem("联系人","单位信息页下一步保存")
        #预留2
        #-----Begin----填写联系人信息 --20181015 chenjingxu
        #PS:新增联系人此处不做处理,但需要上一步提供婚否信息
        #填写文本框内容
        Log().info("开始填写联系人信息")
        HF = "未婚"
        com3 = appclass(self.driver, PATH("..\config\yaml\jyb\jybcase2.yaml"))
        #填写姓名和手机号
        if HF == "已婚":
            for h in range(0, 7):
                com3.elm_operate(h, "")
        else:
            for h in range(0, 5):
                com3.elm_operate(h, "")
        #选择与本人关系
        #relation = ["兄弟", "同事-1"]
        r = 0
        for s in range(9, 11):
            lis = [12, 48]
            com3.elm_operate(s, "")
            print("没有点击打开弹窗")
            time.sleep(0.5)
            com3.elm_operate(lis[r], "")
            r = r + 1
        #提交
        com3.elm_operate(13,"")
        Log().info("恭喜，填写联系人信息成功！！！")
        #----End --填写联系人信息 -------------20181020 chenjingxu
        #---Begin 绑定银行卡-------------------20181020 chenjingxu
        #第一步 填写银行卡号
        self.driver.activate_ime_engine("com.sohu.inputmethod.sogou.xiaomi/.SogouIME")
        com3.elm_operate(14, "6228481359515816576")
        self.driver.activate_ime_engine("io.appium.android.ime/.UnicodeIME")
        com3.elm_operate(15, "")
        Log().info("恭喜，绑定银行卡1成功！！！")
        #第二步 先只填写支行，其它信息不校验
        com3.elm_operate(23, "")
        time.sleep(0.5)
        com3.elm_operate(49, "")
        com3.elm_operate(50, "")
        com3.elm_operate(15, "")
        time.sleep(4)
        # sql = "update credit_bankcard_four set check_result=2000 where mobile=13300000000 and name like'回归%' and check_result=2008"
        MysqlUtiltwo().mysql_execute("update credit_bankcard_four set check_result=2000 where name='%s'"%textval)
        time.sleep(2)
        com3.elm_operate(15, "")
        Log().info("恭喜，绑定银行卡2成功！！！")
        #判断手机号跟银行预留手机号是否一致，然后执行SQL语句
        #第四步，填写验证码
        send_codee =MysqlUtiltwo().mysql_getstring("SELECT t.sms_code  FROM (SELECT * FROM sms_verify_info WHERE phone = '%s' ORDER BY sent_time DESC) t  LIMIT 1"%mobilephone)
        print(send_codee)
        time.sleep(10)
        com3.elm_operate(31,send_codee)
        time.sleep(1)
        com3.elm_operate(15, "")
        time.sleep(5)
        if com3.findItem("绑定银行卡"):
            send_codee2 =MysqlUtiltwo().mysql_getstring("SELECT t.sms_code  FROM (SELECT * FROM sms_verify_info WHERE phone = '%s' ORDER BY sent_time DESC) t  LIMIT 1"%mobilephone)
            com3.elm_operate(31,send_codee2)
            time.sleep(1)
            com3.elm_operate(15, "")
            Log().info("恭喜，绑定银行卡3成功！！！")
        else:
            Log().info("恭喜，绑定银行卡3成功！！！")
        # ---End 绑定银行卡-------------------20181020 chenjingxu
        # ---Begin 其它信息-------------------20181020 chenjingxu
        com3.elm_operate(32, "")
        com3.elm_operate(33, "")
        com3.elm_operate(34, "")
        com3.elm_operate(15, "")
        Log().info("恭喜，填写其它信息成功！！！")
        # ---End 其它信息-------------------20181020 chenjingxu
        #跳过京东认证,富数认证，运营商认证--20181020 chenjingxu
        com3.elm_operate(35, "")
        com3.elm_operate(35, "")
        com3.elm_operate(35, "")
        Log().info("恭喜，跳过京东，富数，运营商认证成功！！！")
        # ---Begin 小问卷-------------------20181020 chenjingxu
        com3.elm_operate(36, "")
        #单选写死，后续通过字典来实现动态选择
        com3.elm_operate(37, "")
        com3.elm_operate(51, "")
        Log().info("恭喜，填写小问卷成功！！！")
        # ---End 小问卷---------------------20181020 chenjingxu
        #等待页面跳转完毕
        time.sleep(2)
        # ---Begin 影像证明-----------------20181020 chenjingxu
        Log().info("上传影像证明")
        com3.swipeup()
        com3.swipeup()
        com3.elm_operate(38, "")
        time.sleep(1)
        # ---start 影像证明-------------------20181020 chenjingxu
        #act_camera = "com.android.camera/com.android.camera.Camera"
        #driver.wait_activity(act_camera, 20, 1)
        com3.elm_operate(39, "")
        com3.elm_operate(40, "")
        time.sleep(2)
        self.driver.wait_activity("com.giveu.corder.ordercreate.activity.PhotoCertificateActivity", 20, 1)
        com3.elm_operate(41, "")
        Log().info("恭喜，上传影像证明成功！！！")
        # ---End 影像证明-------------------20181020 chenjingxu
        # ---Begin 输入登录密码进行验证-------------------20181020 chenjingxu
        com3.elm_operate(42, "")
        com3.elm_operate(43, "")
        time.sleep(2)
        com3.checkItem("成功提交","即有宝S合同生成")

if __name__ == "__main__":
    unittest.main()