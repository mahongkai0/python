from multiprocessing import Pool
from time import sleep,ctime

#事件函数
def worker(msg):
    sleep(2)
    print(msg)
    return time.ctime()
#创建进程池
pool = Poll()


result = []
#向进程池添加事件

for i in range(10):
    msg = 'hello %d' % i

    #异步执行 多个一同执行
    # r = pool.apply_async(fund = worker,args =(msg,))
    # result.append(r)

    #同步执行;一个一个执行
    pool.apply(func = worker,args = (msg,))



### r 只是一个对象 不是 wocrk返回值

#关闭进程池
pool.close()
#回收进程池
poll.join()
for i in result:
    print(i.get()) #可以获取进程事件函数返回值




