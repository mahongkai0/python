

# #file_open.py

# # ABCD
# # 123456
# # 中文  
# try:

# ##折行符也算字节
# #打开文件
#     myfile = open("./mufile.txt")  #能正常打开
#     myfile = open("./myaaaa.py")  # 失败 myaaa没有 用一场方式来告诉出错
#     #读写/文件


#     #关闭文件
#     myfile.close()
#     print("关闭文件成功")

# except OSError:
#     print("文件打开失败")


##_______________________________________________________________________________________

 ##file_read.py
#此示例示意读取文件myfile.txt里的内容
# try:
#     myf = open("c:/Users/Administrator/Desktop/test/平叠/day16/day16.txt")
#     print("读取文件内容")
#     #读取文件内容
#     while True:
#         s = myf.readline()
#         if not s :
#             print("读取文件结束")
#             break
#         print("读取%d个字符" % len(s) ,'内容是:',s)
#     myf.close
# except OSError:
#     print("打开文件失败")


# try:
#     fw = open("c:/Users/Administrator/Desktop/test/平叠/day16/info.txt",'a') #a 追加 w  删除原来再写入
#     #创建文件并写字符串到文件中
#     fw.write("hello\n")  #写入五个字符  \n  换行
#     fw.write("word")
#     fw.writelines("[123,13,13,1,1]")  #
#     fw.close()
#     print("写入文件成功")
# except OSError:
#     print("文件打开失败")  


#----------------______________________________________________________________________________________
# #stdout.py

# import sys
# sys.stdout.write("hello，wold！！！")

# import sys
# f = open("c:/Users/Administrator/Desktop/test/平叠/day16/info.txt",'a')
# print(1,2,3,4,file = f)
# f.close()
# print("正常输出")

##_______________________________________________________________________

#sys.stdin 的用法
# import sys

# s = input("请输入：")

# s = sys.stdin.readline()
# s2 = input("dhdk")  ## 关闭sys.stdin.readline  这里会出错
# print("您刚才输入的是：",s)


# import sys
# s = sys.stdin.read()  #输入 ctrl d  为输入文件结束
# print("s=",s)
# print("程序正常结束") ############## 此示例代码正确 结果有毒



##——————————————————————————————————————————————————————————————————————————————————————————————
###file_read_binary.py
# try:

#     fr = open('c:/Users/Administrator/Desktop/test/平叠/day16/info.txt','rb')
#     #b = fr.read(10)
#     b = fr.read(100)  ###可能出错，在特定的列子中，如拆走”中“  拿走一半字符
#     print(b)
    
#     fr.close()
#     s = b.decode()
#     print("解码之后的内容是：",s)
# except OSError:
#     print("完成")



##————————————————————————————————————————————————————————————————————————————————————————————————————————————
###此示例示意向一个文件中写入256个字节
#字节值从0到255
# b = bytes(range(256))
# try:
#     fw = open('c:/Users/Administrator/Desktop/test/平叠/day16/info.txt','wb')
#      fw.write(b)  # 写入字节串
#     fw.close()
# except OSError:
#     print("写入成功")


##——————————————————————————————————————————————————————————————————————————————————————————
  #######  print 

import sys
def myprint(*args,sep = ' ',end = '\n',file = sys.stdout,flush =False):
    flag = False # 代表是否打印分隔符  sep

    for obj in args:
        s = str(obj)   #转为字符串
        if flag:
            file.write(sep)
        flag = True
        file.write(s)
    file.write(end) #输入末尾字符
myprint(1,2,3,4)
myprint(3,4,5,6,sep = '#',end = '\n***\n')



# import sys
# def myprint(*args,sep = ' ',end = '\n',file = sys.stdout,flush =False):
#     flag = False # 代表是否打印分隔符  sep

#     L =[str(obj) for obj in args]             # ['1','2','3','4']
#     file.write(sep.join(L))
#     # file.wite(end)
#     # if flush():
#     #     file.flush()

#     file.write(end) #输入末尾字符
# myprint(1,2,3,4)
# myprint(3,4,5,6,sep = '#',end = '\n***\n')



###_______________________________________________________________________________________________




###seek.py

# try:
#     fr= open("")
#     b = fr.read(2)
#     print(b)
#     print("当前位置为：",fr.tell())
#     fr.seek(5,0)  # 从文件头向后移动五个字节
#     b = fr.read(5)
#     print("移动后：b=",b)
# ###    另外的做法
#     ##fr.seek(3,1)  # 从当前位置向后移动三个字节
#     ##fr.seek(-15,2) # 从文件尾向文件头方向移动15个字节

#     fr.close()
# except OSError:
#     print("OK")

# import time
# f= open("######################",'w')
# f.write('A')
# f.flush()  # 强制清空缓冲区  如果有再写入 没有清空的话 写不进去  但后面加上 \n (控制字符) 系统默认清空
# while True:
#     pass
    



























































































