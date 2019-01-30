#coding=utf-8
#-------------------------------------------------------------------------------------------
#作者：吴俊威  日期：2018年10月
#内容：脚本生成与运行
#--------------------------------------------------------------------------------------------
# import time
from run_main import *
from jy_case.jyb_temp import *
from appium import webdriver
# import time
from mobiletest.appcomm import *
from common.fun_t import *
from common.mysql_pub import *
from common.mysql_pubtwo import *
from common.oracle_pub import *
from common.logger import Log
cpath = PATH("..\config\yaml\jyb\jybcase1.yaml")

def app_run_test(getid):
    Log().info("即有宝提单开始执行")
    OracleUtil(dbname).oracle_sql("update dafy_sales.registers set status='n' where reg_number=1647 and reg_val_code=1805")  #关闭协议支付
    OracleUtil(dbname).oracle_sql("update dafy_sales.sys_parameters set para_value=0 where para_id='LIVE_BODY_CHECK_SWITCH'") #关闭活体检测
    try:
        con_name,con_num,pc_type,pc_ip = getrun_db(getid)
        delpath=PATH("../case")
        filename = 'test_'+str(getid)
        del_files(delpath,filename)
        time.sleep(2)
        for j in range(con_num):
            try:
                getparam,paramcount = param_db()
                print("统计行:%s"%paramcount)
                for i in range(paramcount):
                    try:
                        filep = PATH("../case/test_")+str(getid)+"_"+str(i)+".py"
                        remove_lines(PATH("../jy_case/jyb_temp.py"),filep,"#默认误删")
                        with open(filep,'r',encoding='UTF-8') as ui:
                            data = ui.readlines()
                        for inx,line in enumerate(data):
                            if inx == 14:
                                val = str("cpath=")+"PATH(\"..\config\yaml\jyb\jybcase1.yaml\")"+"\n"+str("con_name=")+"\""+str(con_name)+"\""+"\n"+str("pc_type=")+"\""+str(pc_type)+"\""+"\n"\
                                      +str("pc_ip=")+"\""+str(pc_ip)+"\""+"\n"+str("getparam=")+str(getparam[i])+"\n"+str("class jyb_order_")+str(getid)+"_"+str(i+1)+str("(unittest.TestCase):")+"\n"
                                data[inx] = val
                            else:
                                data[inx] = line
                        with open(filep,'w',encoding='UTF-8') as oi:
                            oi.writelines(data)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
            time.sleep(2)
            ruleval="test_"+str(getid)+"_*.py"
            all_case = add_case(caseName="case", rule=ruleval)
            run_case(all_case)
            report_path = os.path.join(cur_path, "report")
            print(report_path)
            report_file = get_report_file(report_path)
            shutil.copyfile(report_file,os.path.join(cur_path, "mobiletest/templates/result_wei.html"))
        # A.mysql_close()
    except Exception as e:
        print(e)

