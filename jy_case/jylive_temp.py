# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: jysh_test.py
@time: 2018/12/18 14:03
@desc:
"""
from appium import webdriver
import time
from mobiletest.appcomm import *
from mobiletest.appclass import *
from common.fun_t import *
from common.logger import Log
from jy_case.businessCode import C_JYSH_BusinessCode
import unittest
cpath1 = PATH("..\config\yaml\jylive\capslive.yaml")
cpath2 = PATH("..\config\yaml\jylive\jysh_case1.yaml")
cpath3 = PATH("..\config\yaml\jylive\jysh_case2.yaml")
pc_type = "android真机：小米6.0.1MX" #默认误删
pc_ip = "127.0.0.1" #默认误删
lgetparam={'param_phone': '13300000000', 'param_pwd': '123456', 'param_name': '测试', 'param_ltype': '110102198506020034', 'param_bcard': '工商银行', 'param_cardNo': '6217000333344440001', 'param_ppwd': '111111', 'case_no': 'case1'}#默认误删
class jyliveCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global C_JYSH_BCode
        C_JYSH_BCode = C_JYSH_BusinessCode()
        #初始化及其信息
        global driver
        driver = C_JYSH_BCode.driver  #driver()
        Log().info("开始执行即有生活自动化测试用例")


    def test_0_app_jysh_register(self):
        """注册测试用例"""
        C_JYSH_BCode.register_1_vCode()
        C_JYSH_BCode.register_2_setPWD()
        b_result = C_JYSH_BCode.register_3_checkResult()
        self.assertEquals(b_result, u"注册成功", "注册失败")
        #关闭登录页，方便后面的测试
        C_JYSH_BCode.common_close_loginPage()

    def test_1_app_jysh_login(self):
        """登录测试用例"""
        # account = 13410342891
        # vCode = "123456"
        # password = 'abc12345'
        # L_type=1
        tText = C_JYSH_BCode.login()
        self.assertEqual(tText, "登录成功", "登录失败")

        # 关闭登录页，方便后面的测试
        C_JYSH_BCode.logout()

    def test_2_app_jysh_activate(self):
        """激活测试用例"""
        # account = 13877412744
        # vCode = "123456"
        # password = "abc12345"
        # pPassword = "111111"
        C_JYSH_BCode.login()

        #跳转激活页面
        C_JYSH_BCode.activate_0_jump()
        #第一个页面填写身份证信息
        C_JYSH_BCode.activate_1()
        C_JYSH_BCode.activate_1_submit()
        #第二个页面，OCR采集身份证信息
        C_JYSH_BCode.activate_2_takeIDCard_fontPic()
        C_JYSH_BCode.activate_2_takeIDCard_address()
        C_JYSH_BCode.activate_2_takeIDCard_backPic()
        C_JYSH_BCode.activate_2_takeIDCard_date()
        C_JYSH_BCode.activate_2_takeIDCard_submit()
        #绑定银行卡（验证四要素）
        C_JYSH_BCode.activate_3_bankcarFour()
        C_JYSH_BCode.activate_3_get_Vcode()
        #验证绑定结果是否成功
        tResult = C_JYSH_BCode.check_bidingResult(83, u"绑定成功")
        self.assertEquals(tResult, True, u"身份证四要素绑定失败！")
        #设置交易密码
        C_JYSH_BCode.set_pay_password()
        tResult = C_JYSH_BCode.check_bidingResult(86, u"设置成功")
        self.assertEquals(tResult, True, u"设置交易密码失败！")

        # 关闭登录页，方便后面的测试
        #C_JYSH_BCode.logout()

    # def test_3_app_jysh_order(self):
    #     """下单测试，场景：支付宝；即有钱包：首付为0，首付不为0"""
    #     account = 13410342891
    #     sContents = "小米8SE全网通6G+64G"
    #     dpayment = "零首付"
    #     stages = "6期"
    #     Ppassword = "111111"
    #     sms = "123456"
    #     #登录
    #     C_JYSH_BCode.login(account, vCode=123456, password='abc12345')
    #     #查找商品
    #     C_JYSH_BCode.homepage_search(sContents)
    #     #下单第一步，选择商品参数
    #     C_JYSH_BCode.buy_proccess_1(sContents)
    #     C_JYSH_BCode.buy_proccess_1(sContents)
    #     C_JYSH_BCode.buy_proccess_2_submit()
    #     # 下单第二步，选择首付与分期
    #     C_JYSH_BCode.buy_proccess_dowmpayment(dpayment)
    #     C_JYSH_BCode.buy_proccess_stages(stages)
    #     C_JYSH_BCode.buy_process_2_submit()
    #     #提交订单
    #     C_JYSH_BCode.buy_process_3_submitOrder()
    #     #输入交易密码
    #     C_JYSH_BCode.buy_process_inputPayPassword(Ppassword)
    #     #输入短信验证码
    #     C_JYSH_BCode.buy_process_inputSMS(sms)
    #     #如果是零首付，这里就不需要走支付接口，所以这里需要判断一下
    #     t = C_JYSH_BCode.buy_process_4_changeOrderStatus(account, dpayment)
    #     self.assertEquals(t, True, u"合同状态没有改变，现行不成功")



    @classmethod
    def tearDownClass(cls):
        driver.quit()


if __name__ == "__main__":
    unittest.main()
