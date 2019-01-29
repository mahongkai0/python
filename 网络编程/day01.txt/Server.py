# import socket
# host = socket.gethostname()
# port = 12345
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((host,port))
# s.listen(1)
# sock,addr = s.accept()
# print('Connection built')
# info = sock.recv(1024).decode()
# while info != 'exit':
#     print('MOOD:'+info)
#     send_mes = input()
#     sock.send(send_mes.encode())
#     if send_mes =='exit':
#         break
#     info = sock.recv(1024).decode()
# sock.close()
# s.close()
# #创建套接字













# TCP套接字编程 tcp_server.py
import socket


#创建TCP套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto=0)

#绑定地址
sockfd.bind(('172.88.6.210',7776))

#设置监听
sockfd.listen(8)

#等待处理客户端连接
print("稍等")
connfd,addr = sockfd.accept()
print("Connect from",addr)  #打印客户端地址

#消息收发
while True:
    data = connfd.recv(1024)
    print("对方：",data.decode())
    if not data:
        break


    # sockfd.send(date.encode())
    # date = sockfd.recv(1024)
    date = input(">>")
    if date == "":
        break

    n = connfd.send(date.encode())
    # print("Send %d bytes" % n)

connfd.close()
sockfd.close()


























# import socket


# sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ##绑定地址
# sockfd.bind(('172.88.6.210',7777))


# ##设置监听
# sockfd.listen(100)

# ##等待处理客户端连接
# print("how much is it")
# connfd,addr = sockfd.accept()
# print("Connect from",addr) ##打印客户端地址

# #消息收发
# data = connfd.recv(1024)
# print("Receive Msg：",data.decode())

# n = connfd.send(b"I see")
# print("Send %d bytes" % n)
# #关闭套接字
# sockfd.close()

# connfd.close()




