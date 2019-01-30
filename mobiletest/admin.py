#coding=utf-8
#------------------------------------
#作者：吴俊威  日期：2018年8月
#-----------------------------------
from django.contrib import admin

from mobiletest.models import Mobiletest,Evnccdata

class MobiletestAdmin(admin.ModelAdmin):
    list_display = ['conname ', 'connum ', 'pctype','pcname','pcnum','pcip','create_time','runstatus']

class EvnccdataAdmin(admin.ModelAdmin):
    list_display = ['systpye', 'evntpye', 'evn_name ', 'evn_address ', 'evn_account']

admin.site.register(Mobiletest)
admin.site.register(Evnccdata)


#分别注册