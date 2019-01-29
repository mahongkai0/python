from socket import * 
from multiprocessing import Process
import sys

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

def main():    

    while True:
       
        print('-------------电子词典----------------')
        print('-------1.------登录------------------')
        print('-------2.------注册------------------')
        print('-------3.------退出------------------')
        print('-------------请输入编号---------------')
        


while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('服务器推出')
    except Exception as e:
        print('服务器异常',e)
        continue
p = Process(target = main)
p.daemon = True #主县城推出　所有线程推出
p.start()
 







