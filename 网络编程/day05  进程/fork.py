
import os
from time import sleep
print('22222222222222222222222222222222222')   #打印一次
a = 1
pid = os.fork()

if pid < 0:
    print("Creeate porcess failed")
elif pid == 0:
    print("child procee")
    print("a  = %d" % a)
    a = 10000
    print('clild:',os.getpid())
    print('parena',os.getppid()) #在子进程中获取父进程的id
else:
    sleep(0.5)
    print("Parent Process")
    print("parent a:" ,a)
    print('parena:',os.getpid())
    print('clild:',pid)

pid.close()



