############
#query.py
# pymysql 查询示例
import pymysql

    # 第一步： 导入pymysql模块
host = 'localhost' #服务器地址
user = 'root'               #登陆用户名
password = '123456'     #登陆密码
dbname = 'bank'         #要操作的库

    


    ## 第二步： 建立到数据库服务器的连接 创建连接对象

conn = pymysql.connect(host, user, password, dbname)  


    # 第三步： 创建游标对象（cursor） 通过调用数据库连接对象获得游标
   
cursor = conn.cursor()  #前cursor是名称 后面的是方法
   
   
    ## 第四步： 利用cursao对象 执行sql语句 
sql = "select * from acct"
cursor.execute(sql) #执行SQL语句

    
                    # #第五步： 提交事务（如果需要）只是需要修改数据库时才会用到 暂不用
    ##取出查询结果 并打印
result = cursor.fetchall() #取出结果集  result是一个元祖

# #result = cursor.fetchmany()20

## print(result)

#result = cursor.fetchmany(2)
#print(result)

for r in result:
    acct_no = r[0]
    acct_name = r[1]
    if r[6]: #判断是否为控制
        balance = float(r[6])
    else:
        balance = 0.00 #余额为空转为0
    print('账号：%s, 户名:%s, 余额:%.2f' % (acct_no, acct_name, balance))
   ##第六步：关闭游标对象

cursor.close()
    ## 第七步：关闭数据库连接对象
conn.close()















