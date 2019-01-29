


from socket import * 
from time import sleep 
#设置广播目标地址

dest = ('172.88.6.255',9999)#'172.88.6.255',8100

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("往后余生，风雪是你".encode(),dest)



s.close()














