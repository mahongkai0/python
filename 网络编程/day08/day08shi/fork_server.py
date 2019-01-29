

from socket import * 
import os,sys
#创建套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

s = socket() # 创建TCP套接字
s.bind(ADDR)
s.listen(5)


#客户端处理函数
def clent_handler(c):
    print('客户端：',c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thank you')
    c.close()


#循环等待客户端连接请求
print('Listen to the port 8888...')
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('您已退出服务器')
    except Exception as e:
        print('Error:',e)
        continue

    #创建新的进程处理客户端请求
    pid =os.fork()

    if pid == 0:
        p = os.fork()
        if p == 0: #二级子进程
            s.close()
            clent_handler(c) #chuli具体请求
            #执行完这一步 它将会循环 向上继续走while true  但是c已经被占了 不需要子进程等待客户端所以 
            sys.exit(0) #子进程处理完将会将他tui出

        else:
            sys.exit(0)
    else:  ###父进程创建进程失败或者是父进程都继续等待下一个客户端连接
        c.close()
        os.wait()




