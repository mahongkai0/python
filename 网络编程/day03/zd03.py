#   4.编写一个select服务端，要求监听客户端的连接，客户端发送的内容，以及从终端输入的内容，将客户端发送
#         过来的内容那个和终端输入的内容全部备份到一个文件里
#              sys.stdin   标准输入流
                

from socket import * 
from select import select
import sys
from time import ctime
s = socket()

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',5641))
s.listen(5)


rlist = [s,sys.stdin]
wlist = []
xlist = []

fw = open("c:/Users/Administrator/Desktop/test/网络编程/day03/bei.txt",'a',encoding = 'utf-8') 


while True:
    rs, ws, xs = select(rlist,wlist,xlist)
    for x in rs:
        if x is s:
            connfd,addr = s.accept()  # addr  地址
            rlist.append(connfd)
        elif x is sys.stdin:
            #获取从终端上输入
            data = sys.stdin.readline() 
            data = ctime()+' '+data+'\n'
            fw.flush()
            fw.write(data)
        
        
        
        else:
            data = x.recv(1024).decode()
            
            
           
            data = ctime()+' '+data+'\n'
            fw.write(data)
            fw.flush()
            if not data:
                x.close()
                rlist.remove(x)
                continue
            
         
                
            # print("Receive from %s:%s"% (x.getpeername(),data.decode()))
            
           
            x.send(b'xx')
            wlist.append(x)


    # for w in ws:
    #     w.send(b'Receive your message')
    #     wlist.remove(w)
    
    
    
    
 
  





















