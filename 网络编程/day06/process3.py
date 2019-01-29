 
from multiprocessing import Process
from time import sleep

#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("Im %s" % name)
        print("Im working...")

# p = Process(target = worker,args = (2,'Levi'))
# p = Process(target = worker,kwargs={'sec':2,'name':'levi'})
p = Process(target = worker,args = (2,),kwargs={name':'levi'})
p.start()
p.join()