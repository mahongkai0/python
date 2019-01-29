
# 练习
# 自己写一个文件 info.txt 内部西融入如下一些文字信息


# 张三 20 100
# 李四 21 96
# 小王 22 98
# 写程序将这些数据读取出来  并以如下格式打印

# 张三 今年 20岁,成绩是: 100
# 李四 今年 21岁,成绩是: 96
# 小王 今年 22岁,成绩是: 98

    

# def read_info(filename):
#     '''读取filename 内容 ，形成字典的列表返回
#     返回：[
#         {'name':'张三','age':20,'score':'100'}
#     ]
#     ''' 
#     L=[]   
#     try:
#         fr = open(filename)
#         while True:
#             s = fr.readline()
#             if not s :
#                 break
#             print(s)
#             s2 = s.rstrip()
#             l=s2.split() 
#             print(L)
            
#                #去掉右边的空白字符
#             n,a,s =   # ['张三','20','100']
#             a = int(a)
#             s = int(s)
#             L.append(dict(name = l[0],age = int(l[1]),score = int(l[2])))
#         fr.close()

    
#     except OSError:
#         print("打开文件失败")
#     return L
# infos = read_info("c:/Users/Administrator/Desktop/test/平叠/day16/info.txt")
# def print_info(infos):
#     for d in infos:
#         print(d['name'],'今年',d['age'],'岁,成绩是',d['score'])

# print_info(infos)





# def read(filename):
#     L=[]
#     fr = open(filename,encoding = "utf-8")
#     text=fr.readlines()
#     for x in text:
#         x=x.rstrip()
#         l=x.split(' ')
#         L.append(dict(name=l[0],age=l[1],score=l[2]))
#     return L
# L=read('c:/Users/Administrator/Desktop/test/平叠/day16/info.txt')
# for x in L:
#     print(x['name'],'今年',x['age'],'岁,成绩是',x['score'])
# #
# 写一个程序 让用户输入很多个正整数
# 最后将这些整数存在于文件  mynumbers.txt中
# 如
# 请输入：1
# 请输入：2
# 请输入：3
# 请输入：4
# 请输入：-1   # 结束
# 格式自己定义
# 2.写一个程序 将上一个程序输入的内容从mynumbers文件中读取出来 打印和


# try:
#     fw = open("c:/Users/Administrator/Desktop/test/平叠/day16/mynumbers.txt",'w')
#     try:    
#         while True:
#             n = int(input("请输入数字："))
            
#             if n < 0:
#                 break
        
            
#             fw.write(str(n))  # 转为字符串
#             #fw.write('\r')
#             fw.write('\n')
#     finally:
#         fw.close()
                
# except OSError:
#         print("输入失败")
# except ValueError:
#     print("文件内容错误")






# try:
#     fr = open("c:/Users/Administrator/Desktop/test/平叠/day16/mynumbers.txt",'r')
#     L=[]
#     while True:
#         s = fr.readline()
#         if not s:
#             break
#         L.append(int(s.rstrip()))
#     fr.close()
# except OSError:
#     print("打开文件失败")
# print("和是",sum(L))




# 练习
# 1.写程序，实现文件的复制（注：只复制文件，不复制文件夹）      （同时两个打开文件  一个读  一个写）
# 要求：
#     要考虑文件管闭的问题
#     要考虑超大文件无法一下加载到内存的问题
# #     要能赋值二进制文件（非文本文件）


def copy(src_file,dst_file):
    '''源文件   目标文件  
    返回值True 成功 反之失败
    '''
    try:
        fr = open(src_file,'rb')  ##  条件三成立
        try:  
            fw= open(dst_file,'wb')
            try:
                while True:
                    b = fr.read(4096)          # 条件二成立  4096为缓冲区最大值
        
                    if  not b:
                        break
                    fw.write(b)
            finally:
                fw.close()
        finally:        
            fr.close()
    except OSError:
        return False
    return True


src = input("请输入源文件名:")
dst = input("请输入目标文件名:")
if copy(src,dst):
    print("chenggong ")
else:  
    print("文件失败")





























# try:
#     myf = open("c:/Users/Administrator/Desktop/test/平叠/day16/day16.txt",'wr')
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




# 2.为原学生信息管理系统添加两个功能：
#     9）从文件中读取数据（si.txt）
#     10）保存信息到文件（si.txt）
# 说明：
#     9）相当于文件功能
#     10）相当于保存功能
# 3





















