from threading import Thread
from test import *
import time


def io():
    wite()
    read()


job = []
t = time.time()
for i in range(10):
    th = Thread(target=io)
    job.append(th)
    th.start()
for i in job:
    i.join()
print('Thread ',time.time() - t )


