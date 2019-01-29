

import gevent
from time import sleep

def fo(a,b):
    print("111111111111",a,b)
    gevent.sleep(2)
    print("222222222222222")

def bar():
    print('33333333333')
    gevent.sleep(3)
    print("ddddddddddddddddddddddd")

f = gevent.spawn(fo,1,2)
b = gevent.spawn(bar)


#回首协程
gevent.joinall([f,b])


