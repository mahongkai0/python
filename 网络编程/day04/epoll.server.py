from socket import *
from select import * 

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',4545))
s.listen(3)
#创建ePOLL对象

p = epoll()

#建立查找字典

fdmap = {s.fileno():s}

#注册关注IO
p.register(s,EPOLLIN|EPOLLERR)

while True:
    events = p.poll() #监控IO     ##################　　不变　　这个ｐｏｌｌ是方法
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            #添加新的关注事件  设置边缘触发
            p.register(c,EPOLLIN|EPOLLHUP|EPOLLET)
            fdmap[c.fieno()] =c
        #通过按位与判断是否某个时间就绪
        elif event & EPOLLIN:
            data = fdmap[fd.recv(1024)]
            if not data:               #客户端退出则取消关注 从字典删除
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("Receive:",data.decode())
                fdmap[fd].send(b'Receive')






















