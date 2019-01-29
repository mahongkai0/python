
from threading import Thread
from test import *
import time







job = []
t = time.time()
for i in range(10):
    th = Thread(target=count,args=(1,1))
    job.append(th)
    th.start()
for i in job:
    i.join()
print('Thread ',time.time() - t )


