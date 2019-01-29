# import os,sys
# from time import sleep 

# def copy_1():
#     global n
   
#     while True:
        
#         if n <1024:
#             data= fr.read(n)
#             print(data)
#             fw.write(data.decode())
#             print("复制一半成功")  
#             break
#         data = fr.read(1024)
#         fw.write(data.decode())
#         n -= 1024
#     fw.flush()
    


# def copy_2():
#     global n
#     fr.seek(n,0)
#     while True:
#         data = fr.read(1024)
#         print(data)
#         if not data:
#             print("复制一半成功")
#             break
#         fw.write(data.decode())
#     fw.flush()


# size = os.path.getsize('liao/x1')
# fr = open('liao/x1','rb')
# fw = open('liao/x2','a')
# n = size // 2

# pid = os.fork()

# if pid <0 :
#     print("拉到吧")
# elif pid == 0:
   
#     copy_2()
# else:
#     copy_1()




import os
filename= './text'
#获取文件大小
size = os.path.getsize(filename)
pid = os.fork()
if pid < 0:
    print("shibai")
if pid == 0:
    #复制上半部分
    f = open(filename,'rb')
    fw = open('随便写','wb')
    n = size // 2
    while True:
        if n< 1024:

            data = f.read(1024)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
        f.close()
        fw.close()
    
else:
    #复制下半部分
    f = open(filename,'rb')
    fw = open('随便写','wb')
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
       
        if not data:
            
            break
        fw.write(data.decode())
    f.close()
    fw.close()





