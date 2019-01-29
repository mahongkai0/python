
#账号管理系统 实现账户增删改查
import pymysql
from db_cunf import *  #导入配置


db_conn= None #连接对象


def conn_database(): #连接数据库函数
    global db_conn
    db_conn = pymysql.connect(host, user, password, dbname)
    if not db_conn: #连接失败
        print("连接数据库失败")
        return -1
    else:           #连接成功
        return 0

def close_database(): #关闭数据库连接
    global db_conn
    if db_conn: #判断对象不为空
        db_conn.close()

def print_menu(): #打印菜单函数
    menu = '''
    -----------账户管理系统-------
        1. -查询账户信息
        2. -新建账户
        3.修改账户
        4.删除账户
        5.退出
    '''
    print(menu)
    return


##查询账户 ： 如果用户输入账号 则以账号为条件进行查询
##若果用户不输入 则查询所有账户
def query_acct(): 
    acct_no= input("请输入查询账号：")
    if acct_no and acct_no != "": #用户输入了账户
        sql= '''select * from acct
            where acct_no = '%s'
            ''' % acct_no
    else:##用户为填入账户 查询所有
        sql= 'select * from acct'

    global db_conn
    cursor = db_conn.cursor() ##获取游标
    try:
        cursor.execute(sql)  #执行sql语句
        result = cursor.fetchall() #获取所有数据
        for r in result:
            acct_no = r[0] #分别代表账号 户名 余额
            acct_name = r[1]
            
            if r[6]: #判断是否为空值
                balance = float(r[6])
            

            print("账号：%s, 户名：%s, 余额：%.2f" % (acct_no, acct_name, balance))
    except Exception as e:

        print("查询异常")
        print(e)
    return 
        

def new_acct(): ##新增账户
    try:  #准备数据过程
        acct_no = input("请输入账号：")
        acct_name = input("请输入户名：")
        acct_type =input("请选择账户类型 1 -借记卡 2 -理财卡") 
        balance = float(input("请输入开户金额："))
        assert acct_type in ["1","2"] ##判断acct_type是否合法
        assert balance >= 10.0
        
        #拼装sql 语句 执行插入
        sql = '''insert into acct(acct_no, acct_name, acct_type, balance) values
        ('%s','%s', %s, %.2f) 
        ''' % (acct_no, acct_name, acct_type, balance)
    
    ##获取游标执行
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        print("插入成功")
    except Exception as e:
        db_conn.rollback() #回滚事务
        print("插入操作失败")
        print(e)

    return


def new_update():
    try:
        acct_no = input("请输入账号：")
        new_balance= float(input("请输入修改金额："))
        assert new_balance > 0
        sql = '''update acct set balance = %.2f where acct_no = '%s' 
        ''' % (new_balance, acct_no)

   ##获取游标执行
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        print("修改成功")
    except Exception as e:
        db_conn.rollback() #回滚事务
        print("修改操作失败")
        print(e)

    
def new_delete():
    try:
        new_acct_no = input("请输入要删除的账号：")
        if new_acct_no == '':
            print("请输入正确的账号")
            return main()
        # # if new_acct_no != acct_no:
        # #     print("您输错了")
        #     return new_delete()
        sql = '''delete from acct where acct_no = '%s'
        ''' % (new_acct_no)

   ##获取游标执行
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        print("您已删除成功")
    except Exception as e:
        db_conn.rollback() #回滚事务
        print("修改操作失败")
        print(e)















#main()
def main():
    #连接数据库
    if conn_database() < 0:
        return

    #循环打印菜单，根据选择的菜单
    #调用不同的函数进行处理 
    while True:
        print_menu()
        oper = input("请选择操作：")
        if not oper:
            continue
        elif oper == '1': ##查询
            query_acct()
        elif oper == '2': ##新建
            new_acct()
        elif oper == '3': ##修改
            new_update()
        elif oper == '4':  ##删除
            new_delete()
        elif oper == '5': ##退出
            break
        else:
            print("请输入正确的值")
            continue
    #关闭数据库
    close_database()

##主函数
if __name__ == "__main__":
    main()













