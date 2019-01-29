from socket import * 
from multiprocessing import Process
from threading import Thread
import signal
import sys

#创建套接子
s = socket()
s.bind(('0.0.0.0',8880))
s.listen(3)



#客户端处理函数
def handler(c):
    print('Connect from',c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thank you')
    c.close()


signal.signal(signal.SIGCHLD,signal.SIG_IGN)
#接受客户端请求
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('服务器推出')
    except Exception as e:
        print('服务器异常',e)
        continue
#创建线程
    t = Process(target = handler,args = (c,))
    t.daemon = True #主县城推出　所有线程推出
    t.start()

