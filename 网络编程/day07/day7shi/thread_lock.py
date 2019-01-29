from threading import Lock,Thread
lock= Lock()
a = b = 0
def value():
    while True:
        lock.acquire() #加锁
        if a != b:
            print('a = %d,b =%d'%(a,b))
        lock.release()  #解锁
t  = Thread(target=value)
t.start()

while True:
    with lock:  ###加锁 解锁
        a +=1 
        b +=1

t.join()
