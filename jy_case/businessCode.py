# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: businessCode.py
@time: 2019/1/2 16:07
@desc: JYSH self.common buseness codes
"""
from selenium.common.exceptions import NoSuchElementException
from mobiletest.appcomm import *
from mobiletest.appclass import *
from common.fun_t import *
from common.mysql_pubtwo import *
from common.oracle_pub import *
cpath1 = PATH("..\config\yaml\jylive\capslive.yaml")
cpath2 = PATH("..\config\yaml\jylive\jysh_case1.yaml")
cpath3 = PATH("..\config\yaml\jylive\jysh_case2.yaml")
pc_type = "android真机：小米6.0.1MX"#默认误删
pc_ip = "127.0.0.1"#默认误删
lgetparam={'param_phone': '13300000000', 'param_pwd': 'abc123456', 'param_name': '测试', 'param_ltype': '验证码', 'param_bcard': '工商银行', 'param_cardNo': '6217000333344440001', 'param_ppwd': '111111', 'case_no': 'case1'}#默认误删
class C_JYSH_BusinessCode():

    def __init__(self):
        #初始化设备信息
        try:
            self.driver = connecthub(pc_type,pc_ip,2)
            if self.driver:
                Log().info("连接服务器成功")
            else:
                Log().info("连接服务器失败")
        except Exception as e:
            Log().info(e)
        #登录相关
        self.com1 = appclass(self.driver, cpath2)
        #订单相关
        self.com2 = appclass(self.driver, cpath3)

    def register_1_vCode(self):
        if self.com1.findItem("允许"):
            self.com1.elm_operate(89, "")
            self.com1.swipeleft(3)
            self.com1.elm_operate(88, "")
        """注册逻辑1:获取短信验证码"""
        self.com1.elm_operate(4, "")
        time.sleep(1)
        self.com1.elm_operate(17, "")  # 跳转登录页
        self.com1.elm_operate(12, "")
        newPhone = createPhone()
        self.com1.elm_operate(38, newPhone)
        self.com1.elm_operate(39, "")
        #等两秒再去填验证码
        time.sleep(2)
        self.com1.elm_operate(40, "")
        self.com1.elm_operate(43, "")

    def register_2_setPWD(self):
        """注册逻辑2:设置密码"""
        #password = "abc12345"
        self.com1.elm_operate(45, lgetparam['param_pwd'])
        self.com1.elm_operate(46, lgetparam['param_pwd'])
        self.com1.elm_operate(47, "")

    def register_3_checkResult(self):
        """注册逻辑2:验证是否注册成功"""
        return self.com1.toast_check("注册成功")

    def login(self, l_name=lgetparam['param_phone'], l_type=u"验证码"):
        """
        登录
        :param account: 登录账号
        :param vCode: 验证码
        :param password: 密码
        :param L_type: 登录类型:0,短信验证码  1，密码
        :return:
        """
        vCode= '123456'
        Log().info("登录即有生活账号:%s" % l_name)
        if lgetparam['param_ltype'] != '':
            l_type = lgetparam['param_ltype']
        try:
            for i in range(1):
                self.com1.elm_operate(4, "")
                time.sleep(1)
                self.com1.elm_operate(17, "")  # 跳转登录页
                self.com1.elm_operate(6, l_name)
                if l_type == u"验证码":
                    self.com1.elm_operate(8, "")
                    time.sleep(2)
                    self.com1.elm_operate(7, vCode)
                elif l_type == u"密码":
                    self.com1.elm_operate(10, "")
                    self.com1.elm_operate(7, lgetparam['param_pwd'])
                else:
                    #后续这里需要完善东西。。。。。。
                    print("无法识别的登录类型！")
                    return
                self.com1.elm_operate(9, "")
                tText = self.com1.toast_check(u"登录成功")
                self.com1.elm_operate(54, "")  # 设置手势密码页取消按钮
                return tText
        except Exception as e:
            Log().info(e)
    
    def logout(self):
        """
        退出登录
        :return:
        """
        self.com1.elm_operate(4, "")
        self.com1.elm_operate(36, "")
        self.com1.elm_operate(53, "")
        self.com1.elm_operate(71, "")

    def common_close_loginPage(self):
        # self.driver.press_keycode(4)
        self.com1.elm_operate(13, "")


    """
    #####################################################################################
    ## start 激活20190119 mirrorchen
    #####################################################################################
    """
    def activate_0_jump(self):
        """从个人中心滚动条出进入激活"""
        #判断是否滚动到激活入口，是则点击；找不到。。。
        self.com1.get_dbtext("您还未开通钱包")
        #self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("您还未开通钱包")').click()
        Log().info("成功跳转激活页面")

    def activate_1(self):
        """第一个页面填写身份证+姓名"""
        #name = "测试者"
        idNo = makeIDNo()  # 自动生成身份证号
        self.com1.elm_operate(56, lgetparam['param_name'])
        self.com1.elm_operate(57, idNo)

    def activate_1_submit(self):
        self.com1.elm_operate(58, "")
        Log().info("第一次填写身份证信息提交成功")

    def activate_2_takeIDCard_fontPic(self):
        """拍身份证正面照片"""
        #三次OCR识别不了身份证，改用普通相机拍照
        for i in range(0, 3):
            self.com1.elm_operate(59, "")
            time.sleep(1)
            self.driver.press_keycode(4)
        self.com1.elm_operate(59, "")
        self.com1.elm_operate(61, "")
        self.com1.elm_operate(62, "")
        Log().info("成功拍照身份证正面")

    def activate_2_takeIDCard_address(self):
        """填写地址"""
        l_addr = ["江西", "九江", "九江县"]
        s_addr = "江西九江九江县第九大道108号"
        self.com1.elm_operate(67, "")
        self.com1.get_dbtext(1, l_addr[0])
        self.com1.get_dbtext(1, l_addr[1])
        self.com1.get_dbtext(1, l_addr[2])
        self.com1.elm_operate(68, s_addr)
        Log().info("成功填写地址")


    def activate_2_takeIDCard_backPic(self):
        """拍身份证反面照片"""
        # 三次OCR识别不了身份证，改用普通相机拍照
        policeDart = "即有公安局"
        for i in range(0, 3):
            self.com1.elm_operate(60, "")
            time.sleep(1)
            self.driver.press_keycode(4)
        self.com1.elm_operate(60, "")
        self.com1.elm_operate(61, "")
        self.com1.elm_operate(62, "")
        self.com1.elm_operate(65, policeDart)
        Log().info("成功拍照身份证反面")

    def activate_2_takeIDCard_date(self):
        """选择有效日期"""
        self.com1.elm_operate(69, "")
        for i in range(0, 2):
            self.com1.swipeDown(self.driver, 1, 220, 988, 220, 1156)
            time.sleep(0.5)
        self.com1.elm_operate(71, "")
        self.com1.elm_operate(70, "")
        for i in range(0, 2):
            self.com1.swipeUp(self.driver, 1, 220, 988, 220, 820)
            time.sleep(0.5)
        self.com1.elm_operate(71, "")
        Log().info("成功选择身份证有效日期")

    def activate_2_takeIDCard_submit(self):
        """提交"""
        self.com1.elm_operate(66, "")
        Log().info("第二次填写身份证信息成功提交")

    #绑定银行（验证四要素）
    def activate_3_bankcarFour(self):
        bcard = u"工商银行"
        cardNo = "6212811809000043602"
        phone = "13410342899"
        self.com1.elm_operate(73, "")
        self.com1.get_dbtext(1, lgetparam['param_bcard'])
        self.com1.elm_operate(74, lgetparam['param_cardNo'])
        self.com1.elm_operate(75, lgetparam['param_phone'])
        self.com1.elm_operate(76, "")
        self.com1.elm_operate(79, "")
        self.com1.elm_operate(77, "")
        time.sleep(3)
        #验证不过，执行sql改数据库
        sql = "update credit_bankcard_four set check_result=2000 where mobile=%s"
        db_info = {"host": '10.10.11.94',
              "port": 3306,
              "user": 'root',
              "passwd": 'root$2016',
              "db": 'credit',
              "charset": 'utf8'}
        db = MysqlUtiltwo(db_info)
        db.mysql_Update(sql, phone)
        db.mysql_close()
        time.sleep(1)
        self.com1.elm_operate(77, "")

    def activate_3_get_Vcode(self):
        self.com1.elm_operate(80, "123456")
        self.com1.elm_operate(82, "")
        #蛋疼的绑定跳转需要很长时间，所以+10s
        time.sleep(10)

    def check_bidingResult(self, el, expec_values):
        """
        通过页面中的文字判断是否成功
        :param el: 元素在yaml文件中的位置，为数字
        :param expec_values: 期望值
        :return:
        """
        text = self.com1.elm_on(el).get_attribute("text").strip()
        if text == expec_values:
            return True
        else:
            return False

    def set_pay_password(self):
        self.com1.elm_operate(84, "")
        #密码输入两次
        for i in range(0, 2):
            self.com1.elm_operate(85, lgetparam['param_ppwd'])
            time.sleep(0.3)
    """
    #####################################################################################
    ## End 激活20190119 mirrorchen
    #####################################################################################
    """

    """
    #####################################################################################
    ## start 下单逻辑20190109 mirrorchen
    #####################################################################################
    """
    def homepage_search(self, sContents):
        """
        首页查询功能
        :param sContents: 查找内容（目前只根据商品名称来查询）
        :return:
        """
        self.com1.elm_operate(0, "")
        self.com2.elm_operate(0, "")
        self.com2.elm_operate(1, sContents)
        self.com2.elm_operate(2, "")
        time.sleep(2)
        #els = self.com2.elm_operate(6, "")
        #判断是否查找到目标商品

        if self.com2.get_text(0, sContents) == False:
            Log().info("没有查找到目标商品：%s" % sContents)
            return False
        else:
            els = self.com2.elm_operate(6, "")
            Log().info("共查找到 %s 条数据" % str(len(els)))
            return True

    def buy_process_1(self, sContents):
        """
        详情页中点击购买
        :return:
        """
        if self.homepage_search(sContents) == True:
            self.com2.get_dbtext(0, "手机")
        #判断是否可点击购买（定位的地区是否有货）
        if self.com2.elm_operate(11, "").get_attribute("clickable") == True:
            self.com2.elm_operate(11, "").click()
        else:
            msg1 = self.com2.elm_operate(11, "").get_attribute("text")
            msg2 = self.com2.elm_operate(12, "").get_attribute("text")
            Log().info(msg2 + "：" + msg1)
            return

    def buy_process_2(self):
        """
        更换地址
        :return:
        """
        province = "广东"
        city = "深圳"
        county = "福田区"

        self.com2.elm_operate(13, "").click()
        #判断省份是否存在
        try:
            while self.com2.elm_operate(14, "").is_displayed() == True:
                self.com2.elm_operate(14, "").click()
            else:
                self.com2.swipeup()
        except NoSuchElementException as e:
            Log().info(e)
            return
        self.com2.elm_operate(15, "").click()
        self.com2.elm_operate(16, "").click()

    def buy_process_amountPlus(self):
        """
        增加购买数量
        :return:
        """
        global amount
        amount = 2
        i = 0
        while i < amount:
            self.com2.elm_operate(20, "")
            i = +1

    def buy_process_amountReduce(self):
        """
        减少购买数量
        :return:
        """
        self.com2.elm_operate(21, "")

    def buy_process_2_submit(self):
        """
        提交
        :return:
        """
        self.com2.elm_operate(22, "")

    def buy_process_downpayment(self, dpayment):
        """
        选择首付
        :return:
        """
        self.com2.get_dbtext(1, dpayment)

    def buy_process_stages(self, stages):
        """
        选择分期
        :return:
        """
        self.com2.get_dbtext(1, stages)

    def buy_process_checkMoneyInfo(self):
        """
        检查首付金额，商品合计，月供是否正确
        :return:
        """
        t0 = self.com2.elm_operate(28, "").get_attribute("text")
        t1 = self.com2.elm_operate(25, "").get_attribute("text")
        t2 = self.com2.elm_operate(26, "").get_attribute("text")
        t3 = self.com2.elm_operate(27, "").get_attribute("text")
        total = self.com2.getdigit(t0) * amount
        dp = 0
        if self.com2.case_values(cpath3, 23)[4] == "零首付":
            if t1 == "¥0.00":
                Log().info("首付金额正确")
            else:
                Log().info("首付金额不正确")

            # if self.com2.getdigit(t2)[0] == total:  找数据库来写
            #     Log().info("月供合计金额正确")
            # else:
            #     Log().info("月供金额不正确")

        else:
            dp = self.com2.getdigit(self.com2.case_values(cpath3, 23)[4])[0]/100
            if t1 == total * dp:
                Log().info("首付金额正确")
            else:
                Log().info("首付金额不正确")

            # if self.com2.getdigit(t2)[0] == total:  找数据库来写
            #     Log().info("月供合计金额正确")
            # else:
            #     Log().info("月供金额不正确")

        if self.com2.getdigit(t2)[0] == total:
            Log().info("商品合计金额正确")
        else:
            Log().info("商品合计金额不正确")

        global payMoney
        payMoney = total -total * dp

    def buy_process_checkPayMoney(self):
        """
        检查支付金额
        :return:
        """
        lmoney = self.com2.getdigit(self.com2.elm_operate(29, "").get_atrribute("text"))
        if lmoney == payMoney:
            Log().info("支付金额正确")

    def buy_process_2_confirm(self):
        """
        确认订单
        :return:
        """
        self.com2.elm_operate(30, "")

    def buy_process_3_submitOrder(self):
        self.com2.elm_operate(31, "")

    def buy_process_inputPayPassword(self, Ppassword):
        """
        输入支付密码，函数未验证是否可行
        :param password:
        :return:
        """
        self.com2.elm_operate(32, "").click()
        for i in Ppassword:
            self.com2.elm_operate(32, "").send_keys(i)

    def buy_process_inputSMS(self, sms):
        """
        输入短信验证码，函数未验证是否可行
        :param password:
        :return:
        """
        self.com2.elm_operate(32, "").click()
        for i in sms:
            self.com2.elm_operate(32, "").send_keys(i)

    def buy_process_4_changeOrderStatus(self, phone, dpayment):
        """
        通过修改数据库来更改订单状态
        :return:
        """
        db_info = {"host": '10.12.11.86',
                   "port": 3306,
                   "user": 'store_rw',
                   "passwd": 'Spts$201708',
                   "db": 'GiveU_Store',
                   "charset": 'utf8'}
        mysql_db = MysqlUtiltwo(db_info)
        sql1 = "select * from t_shop_orders where mobile= '" + phone + "' ORDER BY create_time desc limit 3"
        result = mysql_db.mysql_getrows(sql1)
        orderNo = result[0][1]
        idPerson= result[0][2]

        time.sleep(1)
        if dpayment != "零首付":
            sql2 = "update t_shop_orders set status='4' where order_no='"+orderNo+"'"
            mysql_db.mysql_execute(sql2)
            mysql_db.mysql_close()

        #获取合同号，更改合同状态为y，执行存储过程prc_auto_daily_test,再验证状态是否已改
        oracl_db = OracleUtil()
        sql3 = "select * from cs_credit where id_person='"+str(idPerson)+"' order by create_time desc"
        tResult = oracl_db.oracle_getrows(sql3)
        creditNo = tResult[0][1]
        sql4 = "update cs_credit set status='y' where contract_no='"+str(creditNo)+"'"
        oracl_db.oracle_sql(sql4)
        #现行
        oracl_db.oracle_callproc("PRC_AUTO_DAILY_TEST", creditNo)

        #获取订单状态是否已改变
        tResult2 = oracl_db.oracle_getrows(sql3)
        cStatus = tResult2[0][4]
        if cStatus == "a":
            return True
        else:
            return False

    """
    #####################################################################################
    ## End 下单逻辑20190109 mirrorchen
    #####################################################################################
    """

if __name__ == "__main__":
    tc = C_JYSH_BusinessCode()
    tt=tc.buy_process_4_changeOrderStatus("13410342891","零首付")
    print(tt)
