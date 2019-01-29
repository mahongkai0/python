# import random
# import math
 






# __mathclass__ = type
# class map2048();
#     def reset(self):
#         self._row = 4
#         self._row = 4
#         self.data = [
#             [0 for x in rang(self)]
#         ]




# # a = 1
# b =input("请输入账号： ")
# # c = len(b)                 #总字符串长度
# # d = b[0]                  # 首字母
# # e = ord(d)               #首字母的unicode值

# # if e < 65 or 90 <e <97 or e > 122:
# #     print("首字母必须是字母,您输入的不是字母")
#     # for x in rangr(c):
#     #     if x 
# L = list(b)           #把字符xxxx# c =input("请输入密码： ")


# s = int(input("请输入一个数: "))
# a = s
# k = 1
# for x in range(1,s + 1):
#     for y in range(x,a + 1):
#         print(y,end = ' ')
        
#         k += 1
#     a += 1
#     print()  


# 黑洞数真解 
# 2、黑洞数
# 黑洞数又称陷阱数，是类具有奇特转换特性的整数。
# 任何一个数字不全相同的整数，经限“重排求差”操作，
# 总会得到某一个或一些数，这些数即为黑洞数。
# “重排求差”操作即把组成该数的数字重排后得到的最大数减去重排后得到的最小数。
# 举个例子，3位数的黑洞数为495.
# 简易推导过程：随便找个数，如297,3个位上的数从小到大和从大到小各排一次，
# 为972和279，相减得693。按上面做法再做一次，得到594，再做一次，得到495，
# 之后反复都得到495。考虑1000的情况
# A.验证4位数的黑洞数为6174。



# n = input("请输入一个数： ")
# def dl(n):
#     l =list(n)
#     l.sort()
#     minl = ''.join(l)
#     l.sort(reverse=True)
#     maxl= ''.join(l)
#     cl=int(maxl) - int(minl)
#     return cl
# f = dl(n)
# while True:
#     f =dl(str(f))
#     if f == dl(str(f)):
    
#         print(len(n), "位数的黑洞数为：", f)
#         break













# 3、思考题
# 一个Kaprekar数（雷劈数，或卡普利加数）是个非负整数，将它的平方分成两部分，这两部分之和正好是原来的数字。
# 例如，297是一个Kaprekar 数：
# 297² = 88209, 
# 88 + 209 = 297. 
# 在这里，平方分成的第二部分可以从0开始，但不能是负数。
# 例如, 999是一个Kaprekar 数：999² = 998001, 998 + 001 = 999；但100不是：100² = 10000，100 + 00 = 100, 其中第二部分









n = int(input("请输入一个数："))
l = list(str(n**2))
for i in range(len(l)-1):
    ll = l[:i + 1]
    l2 = l[i + 1:]
    m1 = int('',join(l1))
    m2 = int('',join(l2))
    if m2 ==0:
        continue
    else:
        if m1 +m2 ==n:
            print(n, '是一个Kaprekar数')
else:
    print(n,'不是一个Kaprekar数')








 


# zhanghao = input("请输入用户名:")
# flag =[0,0,0,0,0,0,0,0,'false']#账号密码一共8个条件，默认全是0即false
# if 'A' <= zhanghao[0] <= 'Z':#将输入的字符串的第一个字符进行判断
#     for a in zhanghao:#控制账号四个条件的值 条件成立为1 循环对比字符串中的每一个字符（flag[0]必为1因为上个判断） 例如A123字符中的第二的字符1 为第二次循环 即得出flag[2] = 1
#         if 'A' <= a <= 'Z':
#             flag[0] = 1
#         if 'a' <= a <= 'z':
#             flag[1] = 1
#         if '0' <= a <= '9':
#             flag[2] = 1
#         if a == '-':
#             flag[3] = 1
# if flag[0] == 1 and flag[1] == 1 and flag[2] == 1 and flag[3] == 1:#控制账号的判断条件 必须四个都成立
#     print('用户名正确')
#     for i in range(0,3):#当账号正确时 进行3次判断密码循环
#          mima = input("请输入密码:")
#          if flag[8] == 'true':#当一切条件都成立时是flag[8]为true 这时即可停止所有操作
#              break
#          for b in mima:#控制密码四个条件的值 原理同上
#             if 'A' <= b <= 'Z':
#                 flag[4] = 1
#             if 'a' <= b <= 'z':
#                 flag[5] = 1
#             if '0' <= b <= '9':
#                 flag[6] = 1
#             if b == '-':
#                 flag[7] = 1
#          if flag[4] == 1 and flag[5] == 1 and flag[6] == 1 and flag[7] == 1:#同上
#              flag[8]=='true'#当它为true时就是全部条件成立
#              print("密码正确")
#              break
#          else:
#              print("密码错误")
#     else:#讲次循环的内循环进行3次判断 内循环不成立那么flag就不可能为true
#          print("密码错误超过3次请重新登录")
# else:#此为3 13 行的否定形式
#     print('用户名不正确')




#乘法口诀表
# n = 9
# a = 0


# for x in range(1,n+1):
#     for y in range(1 , x + 1):
#         print(y , "x",x,"=",x * y,end = " ")
#     y += 1
#     print()

#判断2 到100之内的素数

# a = 2

# while a < 101:
#    for x in range(2,a)
   
  
#     # for y in range(2 , a):
#     #     if a % y != 0:
#     #         break
#         print(a,end = ' ')
#     a += 1






































