from multiprocessing import Process,Array
import time

#创建共享内存

# shm = Array('i',[1,2,3,4])#开辟列表空间

# shm = Array('i',5)#开辟5个 int空间

shm = Array('c',b'Hello')


def fun():
    for i in shm:
        print(i)
        shm[0] = 1000 #xiugai

p = Process(target = fun )  
p.start()
p.join()
for i in shm:
    print(i)

print(shm.value)

