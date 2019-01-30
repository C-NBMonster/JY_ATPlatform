# -*- coding:utf-8 -*-
#------------------------------------
#作者：吴俊威  日期：2018年9月
#-----------------------------------

from django.db import models

class Mobiletest(models.Model):
    conname = models.CharField('合同名称',max_length=6)  # 合同名称
    connum = models.IntegerField('生成数量')#生成数量
    pctype= (('android真机：小米6.0.1MX', 'android真机：小米6.0.1MX'),('android模拟器', 'android模拟器'),('android真机：华为P10', 'android真机：华为P10'),('android真机：Honor Note10', 'android真机：Honor Note10'),
             ('android真机：MEIZU PRO6', 'android真机：MEIZU PRO6'),('android真机：小米8.0.0', 'android真机：小米8.0.0'),('android真机：小米8.0.0MI6', 'android真机：小米8.0.0MI6'),('android真机：魅族not6', 'android真机：魅族not6'))
    pcname = models.CharField(verbose_name='类型',choices = pctype,default='android真机：小米6.0.1MX',max_length=40,null=True)  # 机器类型
    pcnum= (('127.0.0.1', '127.0.0.1'),('10.14.21.20', '10.14.21.20'),('10.14.21.118', '10.14.21.118'),('10.14.21.33', '10.14.21.33'),('10.14.21.98', '10.14.21.98'),('10.14.21.125', '10.14.21.125'),('10.14.21.118', '10.14.21.118'))
    pcip = models.GenericIPAddressField(verbose_name='服务',choices = pcnum,default='127.0.0.1') # IP
    create_time = models.DateTimeField('创建时间',auto_now=True)  # 创建时间-自动获取当前时间
    runstatus = models.CharField('运行状态',max_length=100,default='未运行')  # 即有宝运行
    lstatus = models.CharField('运行状态',max_length=100,default='未运行')  # 生活运行
    cstatus = models.CharField('运行状态',max_length=100,default='未运行')  # 现金贷运行
    runnum = models.IntegerField('运行次数',default=1,editable=False)#jyb
    livenum = models.IntegerField('运行次数',default=1,editable=False)#jylive
    cashnum = models.IntegerField('运行次数',default=1,editable=False)#cashloan
    class Meta:
        verbose_name = '即有宝订单'
        verbose_name_plural = '即有宝订单'
    def __str__(self):
        return self.conname


class Mobiledata(models.Model):
    contract_no = models.CharField('合同号',max_length=30)
    con_name = models.CharField('合同名称',max_length=20)  # 合同名称
    con_ident = models.CharField('身份证',max_length=30)
    con_phone = models.CharField('手机号',max_length=30)
    capital_source = models.CharField('资金方',max_length=30,default='')
    con_status = models.CharField('合同状态',max_length=30,default='')
    create_time = models.DateTimeField('生成时间',auto_now=True)
    username = models.CharField('运行人',null=True,max_length=300)
    runnum = models.CharField('标记值',null=True,max_length=300)
    case_no = models.CharField('用例编号',null=True,max_length=300)
    class Meta:
        verbose_name = '合同查询'
        verbose_name_plural = '合同查询'
    def __str__(self):
        return self.contract_no


class Evnccdata(models.Model):
    sys_tpye= (('即有宝', '即有宝'),('即有钱包', '即有钱包'),('现金贷', '现金贷'),('后台对内', '后台对内'),('产品管理平台', '产品管理平台'),('中移金服', '中移金服'),('数据库', '数据库'),('其他', '其他'))
    systpye = models.CharField(verbose_name='系统类别',choices = sys_tpye,default='即有宝',max_length=300,null=True)  # 类型
    evn_tpye= (('测试环境', '测试环境'),('准生产', '准生产'),('正式环境', '正式环境'),('其他', '其他'))
    evntpye = models.CharField(verbose_name='环境类别',choices = evn_tpye,default='测试环境',max_length=300,null=True)  # 类别
    evn_name = models.CharField('系统名称',max_length=300)
    evn_address = models.CharField('系统地址',max_length=300)  #
    evn_account = models.CharField('账号密码',max_length=300)
    class Meta:
        verbose_name = '环境信息'
        verbose_name_plural = '环境信息'
    def __str__(self):
        return self.evn_name


class Paramdata(models.Model):
    username = models.CharField('用户名',null=True,max_length=300)
    param_one = models.CharField('门店ID',null=True,max_length=300)
    param_two = models.CharField('商品类型',null=True,max_length=300)
    param_three = models.CharField('产品版本',null=True,max_length=300)
    param_four = models.CharField('商品总额',null=True,max_length=300)
    param_five = models.CharField('首付总额',null=True,max_length=300)
    param_six = models.CharField('保险一',null=True,max_length=300)
    param_seven = models.CharField('贷款期数',null=True,max_length=300)
    param_eight = models.CharField('商品小类',null=True,max_length=300)
    param_nine = models.CharField('商品品牌',null=True,max_length=300)
    param_ten = models.CharField('保险二',null=True,max_length=300)
    param_eleven = models.CharField('资金方',null=True,max_length=300)
    param_twelve = models.CharField('合同状态',null=True,max_length=300)
    case_no = models.CharField('编号',null=True,max_length=300)
    class Meta:
        verbose_name = '参数配置'
        verbose_name_plural = '参数配置'
    def __str__(self):
        return self.param_one

class capitallx(models.Model):
    capital_source = models.CharField('资金方',max_length=30,default='')
    # l_amount = models.DecimalField(max_digits=18, decimal_places=2)
    # l_amount = models.IntegerField('资金')
    l_amount = models.CharField('资金',max_length=1000,default='')
    class Meta:
        verbose_name = '资金配置'
        verbose_name_plural = '资金配置'
    def __str__(self):
        return self.capital_source

class Detaildata(models.Model):
    mtype = models.CharField('模块',max_length=30)
    caseall = models.CharField('自动化用例数',max_length=200)  # 合同名称
    caserun = models.CharField('已执行用例数',max_length=200)
    cpass = models.CharField('通过数',max_length=30)
    cfail = models.CharField('失败数',max_length=30,default='')
    runrate = models.CharField('执行覆盖率',max_length=30,default='')
    passrate =models.CharField('执行通过率',max_length=30,default='')
    runnum = models.CharField('脚本执行次数',null=True,max_length=100)
    runmark = models.CharField('执行标记',null=True,max_length=100)
    create_time = models.DateTimeField('生成时间',auto_now=True)
    class Meta:
        verbose_name = '详细数据'
        verbose_name_plural = '详细数据'
    def __str__(self):
        return self.mtype

class Data_check(models.Model):
    casename = models.CharField('用例',max_length=30)
    casecno = models.CharField('合同号',max_length=50)  # 合同名称
    dbname = models.CharField('数据库',max_length=30)
    sqlval = models.CharField('sql语句',max_length=1000)
    checkone = models.CharField('对比字段',max_length=30,default='')
    checkmath = models.CharField('公式',max_length=30,default='')
    checktwo =models.CharField('参照字段',max_length=30,default='')
    markone = models.CharField('备注',null=True,max_length=300)
    create_time = models.DateTimeField('创建时间',auto_now=True)
    username = models.CharField('用户名',null=True,max_length=30)
    class Meta:
        verbose_name = '数据对比'
        verbose_name_plural = '数据对比'
    def __str__(self):
        return self.casename

class Detail_check(models.Model):
    mtype = models.CharField('模块',max_length=30)
    runmark = models.CharField('运行源',null=True,max_length=100)
    casename = models.CharField('用例',max_length=30)
    valone = models.CharField('对比值',max_length=30,default='')
    valtwo =models.CharField('参照值',max_length=30,default='')
    status = models.CharField('结果',null=True,max_length=300)
    create_time = models.DateTimeField('创建时间',auto_now=True)
    username = models.CharField('用户名',null=True,max_length=30)
    casecno = models.CharField('合同号',max_length=50)  # 合同名称
    checkmath = models.CharField('公式',max_length=30,default='')
    class Meta:
        verbose_name = '对比结果'
        verbose_name_plural = '对比结果'
    def __str__(self):
        return self.status