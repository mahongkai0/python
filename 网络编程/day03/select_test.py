


from socket import * 
from select import select

s = socket()
s.bind(('0.0.0.0',6548))
s.listen(6)

print("监控IO")

rs, ws, xs = select([s],[],[])
print("就绪IO",rs)
print("就绪IO",ws)
print("就绪IO",xs)















