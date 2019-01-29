
from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())
    
p = Process(target = tm,name ='Tarena' )

p.daemon= True#必须在start之前使用

p.start()  




print("Process name:",p.name)
print("Process pid:",p.pid)
print("Process alive:",p.is_alive())
###记得在start后面 因为还没启动

p.join()




