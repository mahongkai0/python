



import socket


##创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##################sockfd = socket(AF_INET,SOCK_STREAM)
##绑定地址
sockfd.bind(('0.0.0.0',5641))


##设置监听
sockfd.listen(100)

##等待处理客户端连接
while True:
    print("how much is it")
    connfd,addr = sockfd.accept()
    print("Connect from",addr) ##打印客户端地址

    #消息收发
    while True:
        data = connfd.recv(1024)
        #客户端退出 立即返回空字串
        if not data:
            break
        print("Receive Msg：",data.decode())

        n = connfd.send(b"I see")
        print("Send %d bytes" % n)
    connfd.close()
    #关闭套接字
sockfd.close()

connfd.close()







