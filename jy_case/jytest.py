#coding=utf-8
#-------------------------------------------------------------------------------------------
#作者：吴俊威  日期：2018年10月
#内容：即有宝脚本生成与运行
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

def app_run_test(getid,uname,marknum):
    Log().info("即有宝提单开始执行")
    # OracleUtil(dbname).oracle_sql("update dafy_sales.registers set status='n' where reg_number=1647 and reg_val_code=1805")  #关闭协议支付
    # OracleUtil(dbname).oracle_sql("update dafy_sales.sys_parameters set para_value=0 where para_id='LIVE_BODY_CHECK_SWITCH'") #关闭活体检测
    try:
        markval=str(uname)+"_"+str(getid)+"_"+str(marknum)
        con_name,con_num,pc_type,pc_ip = getrun_db(getid)
        delpath=PATH("../case")
        filename = 'test_'+str(uname)+"_"+str(getid)
        del_files(delpath,filename)
        time.sleep(2)
        for j in range(con_num):
            try:
                getparam,paramcount = param_db(uname)
                print("统计行:%s"%paramcount)
                count_sys = 0
                for i in range(paramcount):
                    try:
                        filep = PATH("../case/test_")+str(uname)+"_"+str(getid)+"_"+str(i)+".py"
                        if getparam[i]['paraml'] == "a":
                            remove_lines(PATH("../jy_case/jyb_temp.py"),filep,"#默认误删")
                            print("生成a合同case")
                        if getparam[i]['paraml'] == "y":
                            remove_lines(PATH("../jy_case/jyb_temp.py"),filep,"#默认误删")
                            remove_lines(filep,filep,"流程测试a合同")
                            print("生成y合同case")
                        if getparam[i]['paraml'] == "s":
                            remove_lines(PATH("../jy_case/jyb_temp.py"),filep,"#默认误删")
                            remove_lines(filep,filep,"流程测试a合同")
                            remove_lines(filep,filep,"流程测试y合同")
                            print("生成s合同case")
                        if getparam[i]['paraml'] == "pr":
                            remove_lines(PATH("../jy_case/jyb_temp.py"),filep,"#默认误删")
                            remove_lines(filep,filep,"流程测试r合同")
                            remove_lines(filep,filep,"流程测试s合同")
                            remove_lines(filep,filep,"流程测试a合同")
                            remove_lines(filep,filep,"流程测试y合同")
                            print("生成pr合同case")
                        if getparam[i]['paraml'] == "r":
                            remove_lines(PATH("../jy_case/jyb_temp.py"),filep,"#默认误删")
                            remove_lines(filep,filep,"流程测试s合同")
                            remove_lines(filep,filep,"流程测试a合同")
                            remove_lines(filep,filep,"流程测试y合同")
                            print("生成r合同case")
                        with open(filep,'r',encoding='UTF-8') as ui:
                            data = ui.readlines()
                        for inx,line in enumerate(data):
                            if inx == 14:
                                val = str("newcon_name=")+"\""+str("默认空箺")+"\""+"\n"+str("con_name=")+"\""+str(con_name)+"\""+"\n"+str("cpath=")+"PATH(\"..\config\yaml\jyb\jybcase1.yaml\")"+"\n"+str("pc_type=")+"\""+str(pc_type)+"\""+"\n"\
                                      +str("pc_ip=")+"\""+str(pc_ip)+"\""+"\n"+str("getparam=")+str(getparam[i])+"\n"+str("uname=")+"\""+str(uname)+"\""+"\n"+str("markval=")+"\""+str(markval)+"\""+"\n"+str("class jyb_order_")+str(uname)+"_"+str(getid)+"_"+str(i+1)+str("(unittest.TestCase):")+"\n"
                                data[inx] = val
                            else:
                                data[inx] = line
                        with open(filep,'w',encoding='UTF-8') as oi:
                            oi.writelines(data)
                    except Exception as e:
                        print(e)
                    count_sys = count_sys+i+1
                    print(count_sys)
            except Exception as e:
                print(e)
            time.sleep(2)
            ruleval="test_"+str(uname)+"_"+str(getid)+"_*.py"
            all_case = add_case(caseName="case", rule=ruleval)
            run_casenew(all_case,"result_wei.html")
            report_path = os.path.join(cur_path, "report")
            print(report_path)
            report_file = get_reportfile(report_path,'result_wei.html')
            shutil.copyfile(report_file,os.path.join(cur_path, "mobiletest/templates/result_wei.html"))
            if count_sys > 0:
                run_sat = "ok"
            else:
                run_sat = "fail"
    except Exception as e:
        print(e)
        run_sat = "fail"
    return run_sat,markval
