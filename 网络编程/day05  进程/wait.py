import os

from time import sleep

pid = os.fork()

if pid < 0:
    print("Create pracess failed")
if pid == 0:
    print("Chiled %d process exit" %os.getpid())
    os._exit(2)
else:

    pid,status = os.wait() 
    print("pid:",pid)#退出的子进程oid
    print("status：",os.WEXITSTATUS(status))#子进程退出状态
    print("Parent process...")
    while True:
        pass







