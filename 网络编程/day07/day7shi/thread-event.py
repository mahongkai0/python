from threading import Thread,Event
from time import sleep
e = Event()
s = None # 设置为

def bar():
    print('Bar 拜山头')
    sleep(2)
    global s
    s = '天王盖地虎'
    e.set()

b = Thread(target=bar)
b.start()

print("说对口令就是自己人")
e.wait() #阻塞等待 分支线程set


if s == '天王盖地虎':
    print('确认过眼神 你是对的人')
else:
    print('打死他')


b.join()
