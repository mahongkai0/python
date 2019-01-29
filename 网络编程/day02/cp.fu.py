from socket import * 

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定地址
sockfd.bind(('172.88.6.210',7654))
#设置监听套接字
sockfd.listen(10)

#等待客户端连接
connfd,addr = sockfd.accept()

#消息收发


fr = open("c:/Users/Administrator/Desktop/test/网络编程/day02/day.wan.txt",'wb')
while True:

    data = connfd.recv(1024)
    if not data:
        break
    fr. write(data)




#关闭套接字
connfd.close()
fr.close()
sockfd.close()











































































