

from socket import * 
import struct


ADDR =  ('127.0.0.1',4562)

s = socket(AF_INET,SOCK_DGRAM)

#与接收方有同样的数据结构
# st = struct.Struct('i5sf')
while True:
    id = int(input("id:"))
    name = input("name:") 
    height = float(input("height:"))
    data = struct.pack('i5sf',id,name.encode(),height)
    s.sendto(data,ADDR)



























































