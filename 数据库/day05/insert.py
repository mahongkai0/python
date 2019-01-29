


import pymysql
from db_cunf import *  #导入配置


try:
    #连接数据库
    conn = pymysql.connect(host, user, password, dbname)  

    #获取游标
    cursor = conn.cursor()
    ##执行sql语句
    sql = '''insert into acct(acct_no,acct_name,cust_no, acct_type, reg_date, status, balance) \
    values('622345000009','Robert', 'C0010', 1, now(), 1, 33.00)'''
    cursor.execute(sql) #执行
    conn.commit() #提交事务
    print("insert OK")

except Exception as e:
    print("数据库插入异常")
    print(e)

finally:
    cursor.close()
    conn.close() #关闭连接 







