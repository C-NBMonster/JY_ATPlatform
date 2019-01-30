# coding:utf-8
import cx_Oracle
import os
# 编码声明，解决乱码问题
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

dbname = {"user": "dafy_sales",
           "pwd": "Ju$2017",
           "dsn": "10.11.11.33:1521/dbtest01"}


class OracleUtil():
    def __init__(self, dbname):
        ''' 连接池方式'''
        self.db_info = dbname
        self.conn = OracleUtil.__getConnect(self.db_info)

    @staticmethod
    def __getConnect(db_info):
        ''' 静态方法，从连接池中取出连接'''
        try:
            con = cx_Oracle.connect(db_info['user'], db_info['pwd'], db_info['dsn'])
            return con
        except Exception as a:
            print("数据库连接异常：%s"%a)

    def oracle_getrows(self, sql):
        '''查一组数据'''
        try:
            cursor = self.conn.cursor()
            try:
                cursor.execute(sql)
                rows = cursor.fetchall()
                return rows
            except Exception as a:
                print("执行sql出现异常：%s"%a)
                return False
            finally:
                cursor.close()
        except Exception as a:
            print("数据库连接异常：%s"%a)

    def oracle_getstring(self, sql):
        ''' 查询某个字段的对应值'''
        rows = self.oracle_getrows(sql)
        if rows != None:
            for row in rows:
                for i in row:
                    return i

    def oracle_sql(self, sql):
        ''' 执行sql语句'''
        try:
            cursor = self.conn.cursor()
            try:
                cursor.execute(sql)
                self.conn.commit()
            except Exception as a:
                print("执行sql出现异常：%s"%a)
            finally:
                cursor.close()
        except Exception as a:
            print("数据库连接异常：%s"%a)

    def oracle_callproc(self, proc_name,param_in):
        ''' 执行存储过程'''
        try:
            cursor = self.conn.cursor()
            try:
                param_out=cursor.var(cx_Oracle.STRING)
                cursor.callproc(proc_name,[param_in,param_out])
                self.conn.commit()
            except Exception as a:
                print("执行存储过程出现异常：%s"%a)
            finally:
                cursor.close()
        except Exception as a:
            print("数据库连接异常：%s"%a)

    def oracle_close(self):
        ''' 关闭orcle连接'''
        try:
            self.conn.close()
        except Exception as a:
            print("数据库关闭时异常：%s"%a)

if __name__ == "__main__":
        # from common.mysql_pub import *
        # A = MysqlUtil()
        # sql = "select * from cs_credit  where contract_no = '16547823001'"
        # con_name1='自动化'
        # con_name=[]
        # con_name.append(con_name1.strip())
        # ccc=con_name[0]
        # print(ccc)
        # V = OracleUtil(dbname)
        # cnoval =V.oracle_getstring("select contract_no from cs_credit where id_person=(select id from (select * from cs_person where name like '%s%%' order by create_time desc) where rownum=1))"%ccc)
        # print(cnoval)
        # bbb = OracleUtil(dbname).oracle_getstring("select contract_no from cs_credit where rownum=1")
        # OracleUtil(dbname).oracle_sql("update dafy_sales.registers set status='n' where reg_number=1647 and reg_val_code=1805 ")
        # OracleUtil(dbname).oracle_sql("update dafy_sales.sys_parameters set para_value='0'where para_id='LIVE_BODY_CHECK_SWITCH' ")
        # for i in range(1,25):
        #     OracleUtil(dbname).oracle_sql("UPDATE instalment t SET t.DATE_DUE = add_months(to_date('2018/7/1','yyyy/mm/dd'),%s) WHERE t.ID_CREDIT=(select id from cs_credit where contract_no =16552358001)  AND t.NUM_INSTALMENT=%s"%(i-1,i))
        # OracleUtil(dbname).oracle_callproc('PRC_AUTO_DAILY_TEST','21093357001')

        # conval ="  "
        # conval=conval.strip()
        # if conval is None:
        #     print('None')
        # elif conval: #流程测试a合同
        #     print(conval)#流程测试a合同
        #     print('ok')
        #     # OracleUtil(dbname).oracle_callproc('PRC_AUTO_DAILY_TEST',conval)  #流程测试a合同
        # else:#流程测试a合同
        #     print('kkk')
        orc_val = OracleUtil(dbname).oracle_getrows("select * from cs_credit where rownum=1")
        print(orc_val)




        
# 16552357001,16552360001,16552359001,16552361001,16552358001




