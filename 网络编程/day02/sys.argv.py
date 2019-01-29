
# import sys
# print(sys.argv)


from socket import *
s = socket()#AF_INET,SOCK_DGRAM
#设置端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

print(s.type) #套接字类型
print(s.family) #套接字地址类型

s.bind(('172.88.6.210',1000))
print(s.getsockname()) #获取绑定地址


print(s.fileno()) #文件描述符


s.listen(3)
c,addr = s.accept()

print("Clicent address", c.getpeername())

data= c.recv(1024)
c.close()
s.close()










