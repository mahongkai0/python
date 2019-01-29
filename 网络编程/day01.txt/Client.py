# import socket
# s= socket.socket()
# host = socket.gethostname()
# port = 12345
# s.connect((host,port))
# print('Linked')
# info = ''
# while info != 'exit':
#     print('SCIENCE:'+info)
#     send_mes=input()
#     s.send(send_mes.encode())
#     if send_mes =='exit':
#         break
#     info = s.recv(1024).decode()
# s.close()

















from socket import *
#创建套接字
sockfd = socket()

#发起连接请求
server_addr = ("172.88.6.210",7776)
sockfd.connect(server_addr)

#等待处理客户端连接

# connfd = sockfd.accept()



#消息收发
while True:
    # date = connfd.recv(1024)
    data = input(">>")

    if data == "":
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("对方", data.decode())



#关闭套接字
sockfd.close()














