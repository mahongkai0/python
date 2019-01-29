import multiprocessing as mp
from time import sleep
a = 1


#编写进程函数
def fun():
    sleep(3)
    global a
    print('a= ',a)
    print("子进程事件")
    a = 1000
#创建进程对象
p = mp.Process(target = fun)

#启动进程
p.start()
sleep(4)
print("父进程时间")


#回收进程 
p.join()

print("Parent a",a)

##全是1


















