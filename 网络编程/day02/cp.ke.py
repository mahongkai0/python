

from socket import * 
#创建套接字

s = socket()

#发起连接
addr =('172.88.6.210',7654)
s.connect(addr)
#消息的收发
fr = open("c:/Users/Administrator/Desktop/test/网络编程/day02/day.kehu.txt",'rb')

while True:
    data = fr.read(1024)
    if not data:
        break
    s.send(data)
    print("收发成功")
    


fr.close()
s.close()















































