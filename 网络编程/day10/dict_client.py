
from socket import *
import sys
import getpass
#创建网络连接
def main():
    if len(sys.argv)<3:
        print('argv is error')
    host = sys.argv[1]
    port = int(sys.argv[2])
    addr = (host,port)

    s = socket()
    try:
        s.connect(addr)
    except Exception as e:
        print(e)
        return 

##进入一级界面
    while True:
       
        print('-------------电子词典----------------')
        print('-------1.------注册------------------')
        print('-------2.------登陆------------------')
        print('-------3.------退出------------------')
        print('-------------请输入编号---------------')
        
        cmd = input('请输入选项: ')
        #s.send(cmd.encode())
        if cmd not in ['1','2','3','4']:
            print('请输入正确选项')
            sys.stdin.flush()  #清楚标准输入
            continue
        elif cmd == '1':
           
            do_register(s) #注册功能

def do_register(s):
    while True:
        name = input('User:')
        password = getpass.getpass()
        password1 = getpass.getpass()
        if (' ' in name) or (' ' in password):
            print("用户或密码不能有空格")
            continue
        if password != password1:
            print('两次密码不一致')
            continue
        msg = "R %s %s" %(name,password)
        #发送请求
        s.send(msg.encode())
        #等待回复
        data = s.recv(128).decode()
        if data == 'OK':
            print('注册成功')
            
        elif data == 'EXISTS':
            print('用户已存在') 
        else:
            print("注册成功")
        return
main()