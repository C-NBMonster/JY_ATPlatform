# -*- coding:utf-8 -*-
#------------------------------------
#作者：吴俊威  日期：2019年1月
#-----------------------------------

from django.db import models

class liveparam(models.Model):
    username = models.CharField('用户名',null=True,max_length=300)
    case_no = models.CharField('编号',null=True,max_length=300)
    param_phone = models.CharField('电话号码',null=True,max_length=30)
    param_pwd = models.CharField('密码',null=True,max_length=300)
    param_name = models.CharField('姓名',null=True,max_length=300)
    param_ltype = models.CharField('登录类型',null=True,max_length=300)
    param_bcard = models.CharField('银行',null=True,max_length=300)
    param_cardNo = models.CharField('银行卡',null=True,max_length=300)
    param_ppwd = models.CharField('支付密码',null=True,max_length=300)
    class Meta:
        verbose_name = '即有生活参数'
        verbose_name_plural = '即有生活参数'
    def __str__(self):
        return self.username