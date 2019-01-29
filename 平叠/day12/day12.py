

############################   此示例示意函数的缺省参数lst =[]  列表会在def语句执行时创建 
# 并一直绑定  不会被释放  因此可能会引起函数不可重入问题

# L=[1,2,3]
# def f(n = 0,lst=[]):
#     lst.append(n)
#     print(lst)

# f(4,L)    ####[1,2,3,4]
# f(5,L)    ####[1,2,3,4,5]
# f(100)    ##[100]
# f(200)     ### [100,200]
#改进方法 最后重入f（200）得其【200】L=[1,2,3]
# L=[1,2,3]
# def f(n = 0,lst=None):
#     if lst is None:
#         lst =[] # 创建一个新列表并绑定
#     lst.append(n)
#     print(lst)

# f(4,L)    ####[1,2,3,4]
# f(5,L)    ####[1,2,3,4,5]
# f(100)    ##[100]
# f(200)     ### [200]



# 练习：
# 1.写一个程序 输入园的半径 打印出这个圆的面积

# r = float(input("请您输入圆的半径："))
# import math
# s = r ** 2 * (math.pi)
# print("这个圆的面积是：",s)

# 2.写一个程序 输入园的面积 打印出这个圆的半径

# s = float(input("请输入一个圆的面积："))
# import math
# q = s / (math.pi) 
# r = math.sqrt(q)
# print("这个圆的半径为：",r)

######### 改个名   import math as  a(所需要改的，底下可以少打代码,如 a.pi  ) 




# 练习  
# 写一个程序 输入你的生日 （年月日）
# 1)算出你已出生多少天
# 2）算出您出生那天星期几



# year = int(input("请您输入出生年："))
# month = int(input("请您输入出生月："))
# day = int(input("请您输入出生日："))

# import time
# birthday_tuple =(year,month,day,0,0,0,0,0,0)
# #计算出生时计算的内部时间
# birthday_second = time.mktime(birthday_tuple)
# # 计算出生的时长
# life_second = time.time()
# # time.mktime(birthday)
# cha =  life_second - birthday_second

# print("您已出生了",float(cha / 3600 // 24),"天")

# week = {
#     0:'一',
#     1:'二',
#     2:'三',
#     3:'四',
#     4:'五',
#     5:'六',
#     6:'日',
# }


# #得到出生的时间元组                   #  秒数  转化为本地秒数
# birthday_tuple  = time.localtime(birthday_second)
# print("您出生的那天是星期",week[birthday_tuple[6]])


# lianxi 
# 写一个程序  以电子时钟的格式打印时间
# 格式为
# HH：MM：SS
# ru :
# 17:51:20
# 时间自动变化


# import time
# while True:
#     t = time.localtime()
#     #print("%02d:%02d:%02d" %((t[3],t[4],t[5])))#,end = '\r')
#     print("%02d:%02d:%02d" %t[3:6],end = '\r')
#     time.sleep(1)




# import time
# ti = time.time()
# ti_x = time.localtime(ti)
# ti_day = time.asctime(ti_x)

# print('\r' +ti_day[11:13],ti_day[14:16],ti_day[17:19],sep = ':',end = ' ')

# print('\r' +ti_day[11:13],ti_day[14:16],ti_day[17:19],sep = ':',end = ' ')
# # 2.编写一个闹钟程序，启动时间设置定时时间 到时间后打印一句：
# ”时间到！！！“  然后退出程序

# import time
# h= int(input("请设置定时时间小时："))
# min =int(input("请设置定时分钟："))
# # s = int(input("请设置定时秒钟："))
# while True:
#     xianzai = time.time()
#     x_yuan = time.localtime(xianzai)
#     zifuchuan = time.asctime(x_yuan)
#     shi = int(zifuchuan[11:13])
#     fen = int(zifuchuan[14:16])
#     # miao = int(zifuchuan[17:19])
#     print('\r' +zifuchuan[11:13],zifuchuan[14:16],zifuchuan[17:19],sep = ':',end = ' ')
#     if h == shi and min ==fen:
            
#         print("时间到！！！") 
#         break


# 
# def run_alarm(hour,minute):
#     ''' 此函数用来等待时间  当时间到写设定时间相等时 退出此函数'''
#     import time 
#     while True:
#         t = time.localtime()
#         print("%2d:%2d:%2d" %t[3:6],end = '\r')
#         if t[3:5] == (hour,minute):
#             return
#         time.sleep(1)
# h = int(input("请输入定时的小时："))
# m = int(input("请输入定时的分钟："))
# run_alarm(h,m)
# print("时间到！！！")
#########################################################

import time
t = time.localtime()
s = t[3:6]
print(s)
######################################################################
# 3. 编写函数 fun 基功能室计算下列多项式的和
# sn = 1 + 1! +1/2!+1/3！ + 1/n！
# （建议用数学模式factorial）
# 求当 n得20时  Sn的值
# 即
# print（fun（20） 2.718281828...
########################################### 方法1
# import math
# sn = 1
# def fun(n):
#     global sn
#     for x in range(1,n + 1):
#         sn +=1/ math.factorial(x)
#     return sn
# print(fun(20))
########################################方法2
# def fun(n):
#     sn = 0
#     for fenmu in map(math.factorial, range(n + 1)):
#         sn += 1 / fenmu

#     return sn

# print(fun(20))

# def fun(n):
#     sn = sum([1 / math.factorial(x) for x in range(n+1)])
#     return sn

# print(fun(20))




















