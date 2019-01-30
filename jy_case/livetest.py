#coding=utf-8
#-------------------------------------------------------------------------------------------
#作者：吴俊威  日期：2019年1月
#内容：即有生活脚本生成与运行
#--------------------------------------------------------------------------------------------
from run_main import *
from mobiletest.appcomm import *
from common.fun_t import *

def live_run_test(getid,uname,marknum):
    Log().info("即有生活开始执行")
    try:
        markval="live_"+str(uname)+"_"+str(getid)+"_"+str(marknum)
        con_name,con_num,pc_type,pc_ip = getrun_db(getid)
        delpath=PATH("../livecase")
        filename = 'test_sh_'+str(uname)+"_"+str(getid)
        del_files(delpath,filename)
        time.sleep(2)
        try:
            lgetparam,lparamcount = lparam_db(uname)
            print("统计行:%s"%lparamcount)
            count_sys = 0
            for i in range(lparamcount):
                try:
                    filep = PATH("../livecase/test_sh_")+str(uname)+"_"+str(getid)+"_"+str(i)+".py"
                    remove_lines(PATH("../jy_case/jylive_temp.py"),filep,"#默认误删")
                    with open(filep,'r',encoding='UTF-8') as ui:
                        data = ui.readlines()
                    for inx,line in enumerate(data):
                        if inx == 21:
                            val = str("pc_type=")+"\""+str(pc_type)+"\""+"\n"+str("pc_ip=")+"\""+str(pc_ip)+"\""+"\n"+str("lgetparam=")+str(lgetparam[i])+"\n"+str("class jyliveCase_")+str(uname)+"_"+str(getid)+"_"+str(i+1)+str("(unittest.TestCase):")+"\n"
                            data[inx] = val
                        else:
                            data[inx] = line
                    with open(filep,'w',encoding='UTF-8') as oi:
                        oi.writelines(data)
                except Exception as e:
                    print(e)
                count_sys = count_sys+i+1
                print(count_sys)
            time.sleep(2)
            all_case = add_case(caseName="livecase", rule="test*.py")
            run_casenew(all_case,"result_live.html")
            # report_path = os.path.join(cur_path, "report")  # 用例文件夹
            report_path1 = PATH("../report")
            print(report_path1)
            report_file = get_reportfile(report_path1,'result_live.html')
            print(report_file)
            shutil.copyfile(report_file,os.path.join(cur_path, "jylive/templates/result_live.html"))
            if count_sys > 0:
                run_sat = "ok"
            else:
                run_sat = "fail"
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
        run_sat = "fail"
    return run_sat,markval





if __name__ == "__main__":
    cur_path1 = os.path.dirname(os.path.realpath(__file__))
    cur_path = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".")
    # print(cur_path1,cur_path)
    live_run_test()