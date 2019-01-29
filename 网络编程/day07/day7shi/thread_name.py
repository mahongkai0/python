from threading import Thread,currentThread
from time import sleep

def fun():
    print("当前线程：",currentThread().getName())
    sleep(3)
    print("线程属性示例")

#创建线程名称
t = Thread(target=fun,name = 'Tedu')
#设置daemon
t.setDaemon(True)
print('Daemon:',t.isDaemon)


t.start()
###修改线程名称
t.setName('大风雷')                                   
print(t.getName())##t.name

###线程状态
print('获取线程状态Is alive：',t.is_alive())
t.join()

