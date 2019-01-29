

from socket import * 

sockfd = socket(AF_UNIX,SOCK_DGRAM)

sockfd.connect('/sock')

while True:
    msg = input(">>>")
    if not msg:
        break
    sockfd.send(msg.encode())

sockfd.close()






