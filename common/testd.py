import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# conn = cx_Oracle.connect('dafy_sales','Ju$2017','10.11.11.33:1521/dbtest01')   #用自己的实际数据库用户名、密码、主机ip地址 替换即可
# curs=conn.cursor()
# sql="select * from cs_credit  where contract_no = '16547823001'" #sql语句
# rr=curs.execute (sql)
# row=curs.fetchone()
# print(row[0])
# curs.close()
# conn.close()