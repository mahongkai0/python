import gevent
from gevent import monkey

monkey.patch_all() #执行脚本插件 修改阻塞行为
from socket import * 

#创建套接字

def Server():
    s = socket()
    s.bind(('0.0.0.0',5641))
    s.listen(4)
    while True:
        c,addr = s.accept()
        print('Connect from',addr)
        handle(c)
        gevent.spawn(handle,c)#协程方案

def handle(c):
    while True:
        data = c.recv(1024)
        
        if not data:
            break
        print(data.decode())
        
        c.send(b'ok')
    c.close()
Server()




