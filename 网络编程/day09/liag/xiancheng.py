

# from socket import * 
# from threading import Thread
# from mutilprocess import process
# import sys
# #创建套接字
# s = socket()
# s.bind(('0.0.0.0',8888))
# s.listen(3)




# #循环收发
# def xun(c):
#     while True:
#         data = c.recv(1024)
#         if not data:
#            break
#         print(data.decode()) 
#         c.send(b"thank")
#     c.close()


# #异常处理机制
# while True:
#     try:
#         c,addr = s.accept()
#     except KeyboardInterrupt:
#         print('异常了')
#         s.close()
#         sys.exit()

#     except Exception as e:
#         print('服务器异常，原因:',e)
#         continue

# #线程

# t = Thread(target=xun,args=(c,))

# t.setDaemon(True)
# t.start()




# def fff():
#     data = c.recv(1024)
#     if not data:
#         break
#     print(data.decode())
#     c.send(b'ok')

# while True:
#     try:
#         c,addr = s.accept()
#     except KeyboardInterrupt:
#         print('chuocuo')
#         c.close()
#         sys.exit()
#     except Exception as e:
#         print('dayin',e)
#         continue



# p = process(target = fff,args = (c,))
# p.daemon = True
# p.start()


import os
filename = 'c:/Users/Adminis\
trator/Desktop/test/网络\
编程/day09/liaggggggggggg/'

size = os.path.getsize(filename + 'xt.txt')

def read(filename):
    global size
    while True:
        f = open(filename + 'xt.txt','rb')
        fw = open(filename +'xx.txt','w')
        data = f.read(size // 2)
        if (size//2) < 1024:
            fw.write(data)
            print('复制一半成功')
            break
        fw.write(f)
        f3= size // 2
        f3 -= 1024
    f.close()
    fw.close()


def read_r2(filename):
    global size
   
    while True:
         
        fr= open(filename + 'xt.txt','rb')
        fw= open(filename + 'xx.txt','a')
        fr.seek(size // 2,0)
        data = fr.read()
        if not data:
            print('fuzhi')
            break

        fw.write()
    fr.close()
    fw.close()


pid = os.fork()

if pid < 0:
    print('0000')
elif pid == 0:
    read(filename)
else:
    read_r2(filename)

