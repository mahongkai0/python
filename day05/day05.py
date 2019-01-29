

# s = 'ABCD'
# for x in s:
#     print(x)
# else:
#     print("结束了")


# s = input("ffffff： ")
# # blank_count = 0
# # for x in s:
# #     if x == ' ':
# #         c += 1
# # print(c)   

# english_count = 0
# for ch in s:
#     if 0 <= ord(ch) <= 127:
#         english_count += 1
# print(english_count)


 


# blank_count = 0
# index = 0
# while index < len(s)
#     ch = s[index]
#     if ch == ' ':
#         blank_count +=1
#     index += 1


# english_count = 0
# index = 0
# while index < len(s)
#     ch = s[index]
#     if 0 <=ord(ch) <= 127:



# 输入一个字符串，从尾想头输出这个字符串的字符
# 用while
# s = input("ddd:  ")

# for x in  s[::-1]:
#     print(x)

# #
# index = len(s) - 1
# while index >= 0:
#     ch = s[index]
#     print(ch)
#     index -= -1



# for x in range(1,21):
#     print(x, end = ' ')

# print()
# for y in range(1,101):
#     if y * (y + 1) % 11 == 8:
#         print(y, end = ' ') 

# sum = 0
# for x in range(1,100,2):
#     sum += x

# print(sum)

# LIANXI 
# 输入一个整数 代表正方形的宽度  打印如下的正方形
# （注“用for语句嵌套实现）
# 请输入  5
# 打印
# 1 2 3 4 5
# 1 2 3 4 5            
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# 2.打印5
#  12345
#  23456
#  34567
#  45678
#  56789


# s = int(input("请输入一个整数： "))
# c = 0
# if s == 1:
#     print("1")
# else:    
#     while c <= s:
#         for x in range(1, s +1):
#             print(x, end = ' ')
        
#         print()
#         c += 1
#  双for循环





# 12345
# 23456
# 34567
# 45678
# 56789
# w = int(input("请输入一个整数： "))
# for x in range(1, w + 1):
#     ###print(x)
#     for y in range(x , x + w ):
#         print(y, end = ' ')
#     print()
 ######################共创建了6个range对象   1  +  5  





# for x in range(5):
    
#     if x == 3:
#         continue
#     print(x,end = ' ')
# x = 0
# while x < 10:
#     if x % 2 == 0:
#         print(x)  
#     x += 1




#   ##不能被 2. 5.7.3整除的数的和

# s = 0
# for x in range(101):
#     if x % 2 == 0:
#         continue
#     if x % 3 == 0:
#         continue
#     if x % 5 == 0:
#         continue
#     if x % 7 == 0:
#         continue
#     s = s + x
# print(s)

# s = 0

# z = 0
# while s <101:
#     if s % 2 == 0 or s % 3 == 0 or s % 5 == 0 or s % 7 == 0:
        
#         s += 1
#         continue
#     z += s
#     s += 1

# print(z)


# 输入三行文字  将这三行文字保存在一个列表L中 并带打印这个列表
# 如“
# 请输入： abc
# 请输入： 123
# 请输入： 你好
# 生成如下列表 L =['abc','123','你好']

# print（L）#########['abc','123','你好']


# s = input("..yi:  ")
# a = input("..er:  ")
# c = input("..san:  ")
# # L = [s,a,c]
# # print(L)

# L = []
# q = L + [s]
# q = q + [a]
# q = q + [c]
# print(q)


# print(L)






# 写一个程序 让用户输入很多个正整数  当输入负数时  结束输入 讲用户输入的数字存于列表中

# 1.然后打印这个列表
# 2.计算出这些数字的和 然后打这些和
# 如

# ;1
# :2
# 3
# 4
# -1
# 打印【1,2,3,4】


# k= 0

# while True:
#     s = int(input("请输入一个正整数： "))
#   

#     if s <= 0:
#         break
#     k = K + s   

 
# 创建一个空列表 
# L = []

# while True:
#     x = int(input("dddddd: "))
#     if x < 0:
#         break
#     L += [x]
# print(L)


# s =0
# for x in L:
#     s += x
# print(s)



# 写程序打印99乘法表

# 1x1 =1
# 1x2 =2  2x2=4
# 1x3 =3  2x3=6 3x3 =9
# 1x4 =4  2x4=8 3x4=12
# 1x9 =9 ................9x9=81

# b = 1
# a = 1
# s = 2

# print("1 x 1 = 1")
# for x in range(a,3):
#     print(b, "x 2 =", s,end = ' ')
#     b += 1
#     s += 2
# print()

# qq = 3
# q = 1
# for x in range(a,4):
#     print(q, "x", b, '=', qq, end = ' ')
#     q += 1
#     qq += 3
# print()

# qqq = 4
# p = 1
# for x in range(a,5):
#     print(p, 'x 4', '=', qqq, end = ' ')
#     qqq += 4
#     p += 1
# print()

# qqqqq = 5
# pp = 1
# for x in range(a,6):
#     print(pp, 'x 5', '=', qqqqq, end = ' ')
#     qqqqq += 5
#     pp += 1
# print()

# qqqqqq = 6
# ppp = 1
# for x in range(a,7):
#     print(ppp, 'x 6', '=', qqqqqq, end = ' ')
#     qqqqqq += 6
#     ppp += 1
# print()

# qqqqqqq = 7
# ppppppp = 1
# for x in range(a,8):
#     print(ppppppp, 'x 7', '=', qqqqqqq, end = ' ')
#     qqqqqqq += 7
#     ppppppp += 1
# print()

# qqqqqqqq = 8
# pppppppp = 1
# for x in range(a,9):
#     print(pppppppp, 'x 8', '=', qqqqqqqq, end = ' ')
#     qqq += 8
#     pppppppp += 1
# print()

# qqqqqqqqq= 9
# ppppppppp = 1
# for x in range(a,10):
#     print(ppppppppp, 'x 9', '=', qqqqqqqqq, end = ' ')
#     qqqqqqqqq += 9
#     ppppppppp += 1
# print()

# +

# for x in range(1,10):
#     for y in range(1, x +1):
#         print(y, '*', x, '=', x * y, end =' ')

#     print()




# 写一个程序 任意输入一个整数 判读这个数是否为素数 prime素数（也叫质数）是只能被1和自身整除的正整数
# 如：2357  用排除法

# prime = int(input("请输入一个整数： "))
# if prime < 2:
#     print("no")
# else:
    
#     a = True
#     for x in range(2,prime):    
#         if prime % x  == 0:
#             a = False
#             break
#     if a:
#         print(prime, "它是质数")
#     else:
#         print(prime, "它不是质数")


# n = int(input("请输入一个整数： "))
# for x in range(2,n):
#     if n % x == 0:
#         print("no sushu")
#         break
        
# else:
#    print("sushu")






# 3.输入一个整数，此整数代表树干的高度，打印一棵树如下形状的圣诞树
#         输入2 打印
#                     *               
#                    ***                    
#                     *
#                     *
                    
#
 #                    *               
#                    ***
#                   *****
#                     *
#                     *
#                     *


# s = int(input("请输入一个整数： "))
# a = 1
# for x in range(1, s + 1):
   
#     print(('*' * a).center(2 * s - 1))
#     a += 2
# for y in range(1, s + 1):
#     print('*'.center(2 * s - 1))










# 4.  算出100 ~ 999 范围内的水仙花数  （Narcissistic Number）
# 水仙花数是指百位的三次方  + 十位的三次方 + 各位的三次方  等于原数的整数  如153   370






# for s in range(100,1000):
#     if (s // 100) ** 3 + ((s % 100) // 10) ** 3 + (s % 100 % 10) ** 3 == s:
#         # continue
#         print("您需要的水仙花数：", s) 

####字符串方法 索引   先转化为字符串  然后用索引  加时机的转化为整数  ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
################                             ################
# for bai in range(1,10):
#     for shi in range(0,10):
#         for ge in range(0,10):
            
#             x = bai * 100 + shi * 10 + ge
#             if x == bai ** 3 + ge ** 3 +shi ** 3:
#                 print(x)

























