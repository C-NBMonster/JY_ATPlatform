# coding:utf-8
import pymysql.cursors
import datetime
# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

mysql_info = {"host": '10.14.21.20',
              "port": 3306,
              "user": 'root',
              "passwd": 'root2018',
              "db": 'jyautotest',
              "charset": 'utf8'}

class MysqlUtil():
    '''
    mysql数据库相关操作
    连接数据库信息：mysql_info
    创建游标：mysql_execute
    查询某个字段对应的字符串：mysql_getstring
    查询一组数据：mysql_getrows
    关闭mysql连接：mysql_close
    '''
    def __init__(self,mysql_info=mysql_info):
        self.db_info = mysql_info
        u'''连接池方式'''
        self.conn = MysqlUtil.__getConnect(self.db_info)

    @staticmethod
    def __getConnect(db_info):
        '''静态方法，从连接池中取出连接'''
        try:
            conn = pymysql.connect(host=db_info['host'],
                                   port=db_info['port'],
                                   user=db_info['user'],
                                   passwd=db_info['passwd'],
                                   db=db_info['db'],
                                   charset=db_info['charset'])
            return conn
        except Exception as a:
            print("数据库连接异常：%s"%a)

    def mysql_execute(self, sql):
        '''执行sql语句'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            self.conn.rollback()         # sql执行异常后回滚
            print("执行SQL语句出现异常：%s"%a)
        else:
            cur.close()
            self.conn.commit()          # sql无异常时提交

    def mysql_getrows(self, sql):
        ''' 返回查询结果'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            print("执行SQL语句出现异常：%s"%a)
            rows = ''
            return rows
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    def mysql_getstring(self, sql):
        '''查询某个字段的对应值'''
        rows = self.mysql_getrows(sql)
        if rows != None:
            for row in rows:
                for i in row:
                    return i

    def mysql_close(self):
        ''' 关闭 close mysql'''
        try:
            self.conn.close()
        except Exception as a:
            print("数据库关闭时异常：%s"%a)





# MySQLdb.connect()     建立数据库连接
# cur = conn.cursor()    #通过获取到的数据库连接conn下的cursor()方法来创建游标。
# cur.execute()    #过游标cur 操作execute()方法可以写入纯sql语句。通过execute()方法中写如sql语句来对数据进行操作。
# cur.close()     # cur.close() 关闭游标
# conn.commit()   # conn.commit()方法在提交事物，在向数据库插入(或update)一条数据时必须要有这个方法，否则数据不会被真正的插入。
# conn.rollback() # 发生错误时候回滚
# conn.close()     # Conn.close()关闭数据库连接

if __name__ == "__main__":
    A = MysqlUtil()
    # sql = "SELECT  *FROM notify_request t where TEMPLATE_ID LIKE '16091%' ORDER BY t.REQUEST_TIME DESC  limit 0,1"
    # sql = "select runstatus from mobiletest_mobiletest where id=2"
    gtid=2
    t="(已运行)"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    # sql = "UPDATE  mobiletest_mobiletest SET runstatus='%s' where id= '%s'"%(t,gtid)
    # A.mysql_execute("UPDATE  mobiletest_mobiletest SET runstatus='%s' where id= '%s'"%(t,gtid))
    # b=A.mysql_getrows(sql)
    # print (b)
    # c=A.mysql_getrows("select * from mobiletest_mobiletest")
    # print (c)
    # param_list = A.mysql_getrows("SELECT param_one,param_two,param_three,param_four,param_five,param_six,param_seven,param_eight FROM mobiletest_paramdata")
    # print(param_list)
    con_name="test"
    # sql = "select * from mobiletest_mobiletest where conname  like '%s%%'"%con_name
    sql = "SELECT t.con_name FROM (SELECT * FROM mobiletest_mobiledata WHERE con_name LIKE '自动化%' ORDER BY create_time DESC) t LIMIT 1"
    x=A.mysql_getrows(sql)
    y=A.mysql_getstring(sql)
    print(x,y)
    # print (A.mysql_getstring(sql))
    # A.mysql_close()
    capval = MysqlUtil().mysql_getrows("SELECT t.capital_source,t.l_amount FROM mobiletest_capitallx t WHERE t.capital_source<>'资金cookie'")
    print(capval[1][0],capval[1][1])
    cookie_val = MysqlUtil().mysql_getrows("SELECT l_amount FROM `mobiletest_capitallx` WHERE capital_source='FAXC'")
    cookie_val = cookie_val[0][0].strip()
    print(cookie_val)
    con_name='自动化箺愃'
    conval = MysqlUtil().mysql_getstring("SELECT t.con_status FROM (SELECT * FROM mobiletest_mobiledata WHERE con_name LIKE '%s%%' ORDER BY create_time DESC) t LIMIT 1"%con_name)
    if conval is not None: #contract_no
        print(conval)
    else:
        print('不存在')
    if conval is None:
        print('None')
    elif conval: #流程测试a合同
        print(conval)#流程测试a合同
        print('ok')
        # OracleUtil(dbname).oracle_callproc('PRC_AUTO_DAILY_TEST',conval)  #流程测试a合同
    else:#流程测试a合同
        print('kkk')

