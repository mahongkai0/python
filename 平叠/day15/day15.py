


# lianxi 
# 写一个生成器函数  myeven（star，stop）  # 不包含stop
# 如：

# def myeven(start,stop):
#     ...#自己实现
# evens = list(myeven(10,20))
# print(evens)   # [10,12,14,16,18]
# for x in myeven(21,30):
#     print(x)  # 22 24 26 28



# def myeven(start,stop):
#     i = start
#     while i < stop:
#         if i % 2==1:
#             yield i
#         i += 1
#     return i 
#     #return [x for x in range(start,stop) start % 2 == 1]
# evens = list(myeven(10,20))
# print(evens)   # [11,13,15,17,19]
# for x in myeven(21,30):
#     print(x)  # 21 23 25 27 29


# 已知有列表
# L=[2,3,5,7]
# 2.写一个生成器函数 让此函数能够动态的提供数据  数据为原列表中数字的平方和加1  

# 2.写一个生成器表达式  让次列表表达式能够动态提供数据  数据同样为表中数字加1
# 3.生成一个列表 此列表内的数据为原列表数字平方加1
# 最终生成的数为  5  10  26  50 




# L=[2,3,5,7]
# def my():
#     # for x in L:
#     #     yield x ** 2 + 1
#     return (x ** 2 +1 for x in L) 

# for x in my():
#     print(x)

# print("------------------------------------------")
# gen = my()
# for x in gen:
#     print(x) 


# print("------------------------------------------")

# L2=[x ** 2 + 1 for x in L ]
# print(L2)



## 试写一个生成器函数  myfilter(func,iterable)
## 要求此函数与PYthonne内建的函数功能完全相同
## 如：
# #####方法1
# def myfilter(func,iterable):
#     it = iter(iterable)  ## 拿到可迭代对象的迭代器
#     while True:
#         try:
#             x = next(it)
#             if func(x):
#                 yield x 
#         except StopIteration:
#             return

# for i in myfilter(lambda x:x % 2== 1,range(10)):
#     print(i)

##方法2
# def myfilter(func,iterable):
#     for x in iterable:
#         if func(x):
#             yield x

# for i in myfilter(lambda x:x % 2== 1,range(10)):
#     print(i)

##方法三   不是生成器函数 但内部生成了一个生成器
# def myfilter(func,iterable):
#    return(x for x in iterable if func(x))


# 3.看下面两个程序的执行结果是什么 为什么
# 程序1
# L=[2,3,5,7]
# A=[x *10 for x in L]
# it = iter(A)
# print(next(it))###???   20
# L[1] =333
# print(L)
# print(next(it)) ##？？   30    


# # 程序2
# L=[2,3,5,7]
# A=(x *10 for x in L)
# it = iter(A)
# print(next(it))###???   20
# L[1] =333
# print(L)
# print(next(it)) ##？？   3330    现用现生成




# 练习
#     实现一个python2下的xrange(start,stop,[step])生成器函数 此生成器函数按range的规则来生成
#     一系列整数    
#         要求：
#         myxrange功能与range功能完全相同 
#         不允许调用range函数和列表
#         用自己写的myxrange结果生成器表达式求 1~10内所有奇数的平方和



# def myxrange(start = 0,stop = 1,step = 1):
#     if stop is None == 0:
#         stop =start
#         start = 0
#     if step is None:
#         step = 1

#     if step >0:
#         while start < stop:
#             yield start
#             start += step
#     elif step <0:
#         while start > stop:
#             yield stop
#             stop += step




# it = iter(x ** 2 for x in myxrange(1,10) if x % 2 == 1 )
# print("结果为：",sum(it))





# 求 1 ** 2 + 3 ** 2 + 5** 2.....+

# 2
# .写一个程序  从键盘输入一段字符串  用变量s绑定
#     1.将此字母串转为字节串用变量b绑定  并打印出此字节串b
#     2.打印字符串s的长度和字节串b的长度
#     3.将字节串b再转化为字符串用变量s2绑定  然后判断s2和s是否相同






# s = input("请输入一串字符串：")
# #b = bytes(s,encoding='utf-8')
# b =s.encode(encoding = 'utf- 8')
# print(b)
# print("字节串b的长度是：",len(b))
# print("字符串s的长度是：",len(s))
# s2 = b.decode(encoding = 'utf - 8')
# print(s2)

# if s2 is s:
#     print("是")
# else:
#     print("不是")

# #s = input("请输入一串字符串：")
# #b = s.encode()
# #print(b)











# 3.分解质因数 输入一个正整数  分解质因数
# 如输入  90   
# 打印  
# 90 = 2*3*3*5
# 注：
#  质因数是指最小能被原数整除的素数（不包括1）

# 思路一 ： 写一个质数函数 然后把区间所有的质数填入列表   除完列表递归继续除  核心：str【i】 + ‘*’ +str（函数（输入数/i））
# 思路二：  写一个质数函数  然后把区间所有能满足条件的填入列表  



# L = []
# s = int(input("请输入一个数："))
# n = s
# def zhi(s):
#     if s == 2:
#         print('2 = 2') 
#         return
#     else: 
        
#         for x in range(2,s+1):
#             if s % x == 0:
#                 s = s // x 
#                 L.append(x)
#                 return zhi(s)
#         # return L


   
#     print(n,' = ', '*'.join([str(x) for x in L]))

# zhi(s)

### print(ma,'=','*'.join([str(x)for x in L])




# 4.预习文件操作 面向对象  
#______________________________________    111                                 
# def zhi(x):
#     if x < 2:
#         return False
#     for n in range(2,x):
#         if x % n == 0:
#             return False
#     return True
# ma = int(input("请输入一个整数："))
# ma_k = ma
# L=[]
# def fen_j(ma):     
#     if zhi(ma_k):
#         return ma_k  
#     for y in range(2,int(ma_k // 2 + 1)):
        
#         if ma % y == 0:
#             fu = int(ma /y)
#             L.append(y)
#             if fu == 1:
#                 return L           
#             return fen_j(fu)       
# fen_j(ma)
# if len(L) ==1:
#     print(ma,'=',ma)                        
# elif len(L) >= 2:
#     print(ma,'=',end = '')
#     for x in range(len(L)):
        
#         if x == len(L) - 1:
#             print(L[x],end = '')
#         else:
#             print(L[x],'*',end ='')


### print(ma,'=','*'.join([str(x)for x in L])




##___________________________________________________________________________________

# def  get_all_yinshu(x):
#     '''此方法用来获取一个数x的所有因数'''
#     L=[]
#     while x > 1:
#         #每次找一个质因数,然后加入到列表后，变量x的值
#         for i in range(2,x +1):
#             if x % i == 0: #找到质因数
#                 L.append(i)
#                 x = int(x // i)
#                 break

#     return L
# n = int(input("请输入："))
# L =get_all_yinshu(n)
# print(n,'=', '*'.join(str(x) for x in L))












































