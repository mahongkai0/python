

from socket import * 
import os 

if os.path.exists("./sock"):

    os.remove('/sock')



#chuangjianbendi /套接字

sockfd = socket(AF_UNIX,SOCK_DGRAM)


#绑定套接字文件

sockfd.bind("./sock")

#监听
sockfd.listen(2)

while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.close()
    sockfd.close()








