

########序列传参示例：
# def ss(a,b,c):
#     print("a=",a)

#     print("b=",b)
#     print("c=",c)

# L= [1,2,3]
# ###ss(L[0],L[1],L[2])
# ss(*L)
# T = (100,200,300)
# s = "ABC"

################关键字传参
# def sss(a,b,c):
#     print("a=",a)

#     print("b=",b)
#     print("c=",c)

# sss(c = 3,b = 2,a = 1)  可以不按位置  不能多给
# L= [1,2,3]
# ###ss(L[0],L[1],L[2])
# ss(*L)
# T = (100,200,300)
# s = "ABC"




# def sss(a,b,c):
#     print("a=",a)

#     print("b=",b)
#     print("c=",c)


# d= {'c':33,'b':22,'a':11}
# # sss(c= d['c'],b=d['b'],a=d['a'])
# sss(**d)  等同于  ss（c=33，b=22，a=11）

# 错误示例
# d2 ={'c':33,'b':22,'f':11}and 'a' = 11,'w' =2}
# sss(**d2)


 
# a = [1,2,3]
# b = 200
# def ss(x,y):
#     print(id(x))       
#     x = x + [y]       #####此处改变的是变量 不是对象
#     print(id(x)) 
#     print(x)       
# ss(a,b)
# print(a)   #[1,2,3]
# print(b)   #200  


#————————————————————————————————————函数形参——————————————————————————————————————————————



###3示意函数的缺省参数
def info(name,age = 1,address="不详"):
    print(name,"今年",age,"岁，家庭住址:", address)

info("魏明泽",35,"北京市朝阳区")
info("Tarena",15)
info("小张")


# 练习 
# 写一个函数  myadd，  此函数可以计算两个数  三个数和四个数的和
# 如

# def myadd(a,b,c=0,d=0 ):
#     sum = a + b + c + d
#     return sum

# print(myadd(10,20))
# print(myadd(100,200,300))
# print(myadd(1,2,3,4))


# name_Tupele = ("zhangsan",12,12.5)
# for x in name_Tupele:
#     print(x)

# def func(*args):        ###绑定元组
#     print("实参个数是：",len(args))
#     print('args=',args)
# func()
# func(1,2,3,4)
# func(1,2,3,4,'AAA','BBB')
# func(*"ABCDE")

#写一个函数 mysum 可以传入任意个数字实参 返回所有实参的和
# def mysum(*a):
#     s = 0
#     for x in a:
#         s += x
#     return s
# # 
# 
#  def mysum(*args):
#     s = sum(args)  ###############s =sum([*args])
# #     return s
# print(mysum(1,2))
# print(mysum(1,2,3,4))
# print(mysum(1,2,3,4,5,6,7,8))

# 此函数示例字典关键字形参
# def func(**kwargs):
#     print("关键字参数的个数是：",len(kwargs))
#     print("kwargs=",kwargs)
# func(name='魏明泽',age = 35,address='朝阳区')
# func(a=1,b=2,c=3,d='ABC',e = [1,2,3])
# ###########func(1=2)   出错 并不是标示符

# 已知内建函数max的帮助文档
# help（max）
# max（iterable）
# max（arg1,arg2,*args）
# 仿造max写一个mymax函数  功能与max函数完全相同 （不允许调用max）

# print（max（【6,8,5,3】）


# def mymax(*args):
# ###判断实参是一个可迭代对象还是多个数据
#     if len(args) == 1:  #说明args里是可迭代对像
#       #如[6，8,5]
#         # iterable = args[0]        #把可迭代对象取出
#         zuida = args[0][0]#iterable[0]
#         for x in args[0]:
#             if x >zuida:
#                 zuida = x
#         return zuida
      
#     elif len(args) > 1:  #说明args里是有两个或两个以上的数据
#     #如 args(1,2,3,4)
#         zuida = args[0]
#         for x in args:
#             if x > zuida:
#                 zuida = x
#         return zuida

# print(mymax([6,8,5,3]))
# ########################## print(mymax(1,))
# print(mymax(6,80,5,3))
# # *[,key = func]





# ################bug   print（） 修正版  

# def mymax(a,*args):
# ###判断实参a是否是一个可迭代对象          元组必等于0
#     if len(args) == 0:  #\没有这样一部分
#       #如[6，8,5]
#                 
#         zuida = a[0]
#         for x in a:
#             if x >zuida:
#                 zuida = x
#         return zuida
      
#     elif len(args) > 0:  #说明args里是有两个或两个以上的数据
#     ###如 a = 1  args={2,3,5}
#         zuida = a ####假设a最大
#         for x in args:
#             if x > zuida:
#                 zuida = x
#         return zuida

# print(mymax([6,8,5,3]))

# print(mymax(6,80,5,3))
# # *[,key = func]


##############必须调用max函数


# def mymax(a,*args):
# ###判断实参a是否是一个可迭代对象          元组必等于0
#     if len(args) == 0:  #说明args里是可迭代对像
#       #如[6，8,5]
#         return max(a)       
#                 #最把可迭代对象取出
    
      
#     elif len(args) > 0:  #说明args里是有两个或两个以上的数据
#     ###如 a = 1  args={2,3,5}
#         return max(a, *args) ####拆解序列
#         ####################################return max(a,max(args))

# print(mymax([6,8,5,3]))

# print(mymax(6,80,5,3))
# # *[,key = func]



###############局部变量全局变量示意

# a = 100
# b = 200
# def fx(c):
#     d = 400
#     print(a,b,c,d)

#                              #######全局  a b  局部  c  d
# fx(300)
# print(a,b)
# print(c,d)         ######出错  c.d 不存在


# 1.写一个函数  isprime(x)   判断x 会否是素数  如果为素数 则返回True  负责返回false
# 2.写一个函数   prime_m2n（m，n）  返回从m开始 到n结束范围内的素数     返回这些素数的列表 并打印
# 如：
# L= prime_m2n（m，n）(10,20)
# print（L）【11,13,17,19】
# 3.写一个函数 primes（n），返回指定函数内n 不包含n的全部素数 的列表  并打印这些素数的列表 
# L= primes(10)
# print(L)  #[2,3,5,7]
#     1).打印100以内的全部素食
#     2）.打印100~200之间全部素数的和
# 4.改写之前的学生信息管理系统  将程序改为两个函数：
# def input_student():
#     ....#此函数用于获取学生的信息 形成包含有字典的列表
#     然后返回此列表
# def output_student(L):
#     ..#此函数以列格的形式打印学生信息的列表

# 测试（实现与之前相同的功能）
# infors = input_student（）
# output_student(infors)




# def isprime(x):
    
#     # if x == 1 or x==2:
#     if x <2:
#         return False
   
#     # elif x > 2:
#     elif x >= 2:
#         # count = 1
#         for y in range(2,x):
#             if x % y == 0:
#                 # count += 1
#                 return False
#             # if count == 1:
#             #     return True
                    
#             # else:
#             #     return False
#         else:
#             return True           

# a = int(input("请输入一个数："))
# print(isprime(a))

# ##################22222
# def prime_m2n(m,n):
#     L=[]
 
#     for x in range(m,n):
#         if isprime(x):
#             L.append(x)
#     return L

# ##return [x for x in range[m,n] if isprime(x)]
# m = int(input("请输入开始数："))
# n = int(input("请输入结束数："))        
# s = prime_m2n(m,n)
# print(s)


# #######################33333
# qq = []
# def primes(n):
#     for x in range(1,n):
#         if isprime(x):
#             qq.append(x)
#     return qq
    

# n = int(input("请输入一个整数："))

# dd = primes(n)
# print(dd)

# #print(primes(100))
# ###############4444444444444444

# print(sum(prime_m2n(100,200)))


































































































































