

from socket import * 
from select import select

#准备要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',4646))
s.listen(5)

# 添加关注列表
     
rlist = [s]
wlist = []
xlist = []

while True:

#监控IO的发生
    rs,ws,xs = select(rlist,wlist,xlist)
    #遍历三个列表 确定哪个IO发生
    for r in rs:
        if r is s:
            #如果遍历到s说明s就绪 则有客户端向我发起连接
            c,addr = r.accept()
            print("Connect from", addr)
            rlist.append(c)
        #客户端连接套接字就绪 则接收消息
        else:
            data= r.recv(1024)
            
            if not data:
                rlist.remove(r)
                r.close()

                continue
                
            print("Receive from %s:%s"% (r.getpeername(),data.decode()))
            #r.send(b'Receive')
            wlist.append(r)####################  立即返回 让你主动处理

    for w in ws:
        w.send(b'Receive your message')
        wlist.remove(w)
    
    for x in xs:
        x.close()
        raise


