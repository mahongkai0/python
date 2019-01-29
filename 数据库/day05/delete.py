import pymysql
from db_cunf import *  #导入配置



try:
    #连接数据库
    conn = pymysql.connect(host, user, password, dbname)  

    #获取游标
    cursor = conn.cursor()
    ##执行sql语句
    sql = '''delete from acct where acct_no= '622345000009'
    '''
   
    cursor.execute(sql) #执行
    conn.commit() #提交事务
    print("修改笔数： %d" % cursor.rowcount)

except Exception as e:
    print("数据库删除异常")
    print(e)

finally:
    cursor.close()
    conn.close() #关闭连接 


