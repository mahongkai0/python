

from socket import *
import pymysql
import os
import sys
import time
import signal
#定义一些全局变量
DICT_TEXT = "c:/Users/Administrator/Desktop/test/网络编程/day10/dict.txt"

HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

#网络搭建
def main():
    #创建数据库lianjie
    db = pymysql.connect('localhost','root','123456','dict_tcp')
    
    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)
    #处理僵尸
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr = s.accept()
            print('Connect from',addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器推出')
        except Exception as e:
            print('服务器异常',e)
            continue

        #创建子进程
        pid = os.fork()
        if pid ==0:
            s.close()
            do_child(c,db)  #子进程函数
        else:
            c.close()
def do_child(c,db):
    # print(c.recv(1024))      
    while True:
        data = c.recv(128).decode()
        print(c.getpeername(),':',data)
        if data[0] == 'R':
            do_register(c,db,data)
#注册
def do_register(c,db,data):
    l= data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    sql = "select * from user where dict_name = '%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b'EXISTS')
        return
    #插入用户
    sql = "indert into user (name,passwd) values\
        ('%s','%s')"%(name,passwd)

    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except Exception:
        db.rollback()
        c.send(b'FAIL')





main()




