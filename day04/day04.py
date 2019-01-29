





# 输入三行文字 让着三行文字依次以20个字符的宽度右对齐输出
# 如：
# 输入第一行  hello word
# 输入第二行 abcd
# 输入第三行  a
# 输出结果为
#  hello word
#        abcd
#           a
# 做完思考  
# 能否以最长的字符串长度进行右对齐显示 左侧填充空格




# s = input("请输入第一行文字： ")
# l = input("请输入第二行文字： ")
# k = input("请输入第三行文字： ")

# max_length = max(len(s), len(l), len(k))
# a = '%' + str(max_length) + 's'

# print(a % s)
# print(a % l)
# print(a % k)





# j = max(len(s), len(l), len(k))
# print(' ' * (j - len(s)) + s)         ##1
# print(' ' * (j - len(l)) + l)
# print(' ' * (j - len(k)) + k)



# print("%20s" % s)
# print("%20s" % l)                      ###2
# print("%20s" % k)





# s = int(input("ssss: "))
# i = 1
# while i <= s:
#     print("这是第",i, "行") 
#     i += 1

# # i = 1


# while i <= 20:
#     print(
# "hello")
#     i += 1

# a = 1

# while a <= 10:
#     i = 1
#     while i <= 20:
#         print(i, end = ' ')
#         i += 1
#     print()
#     a += 1

# a = 1
# while a <= 5:
#     print(a, end = ' ')
#     a += 1
# print()
# while a <= 10:
    
#     print(a, end = ' ')
#     a += 1
# print()
# while a <= 15:
#     print(a, end = ' ')
#     a += 1
# print()

# while a <= 20:
#     print(a, end = ' ')

#     a += 1
# print()


# i = 1
# while i <= 20:

#     print(i, end = ' ')

#     if i % 5 == 0:
       
#         print()
#     i += 1


# #  
# i = 20
# while i >= 1:
#     print(i, end = ' ')
#     i -= 1





# begin = int(input("请输入一个开始的整数： "))
# end = int(input("请输入一个结束的数： "))
# x = begin
# print_count = 0
# while x < end:
#     print(x, end = ' ')
#                                              # print_count += 1
#                                              # if print_count % 5 == 0:
#                                              #     print()
#                 #             # if  x % 5 == (begin + 4) % 5:
#                 #     print()
#     x += 1




# s = int(input("请输入一个整数： "))
# if s == 1: 
#     print('#')
# else:    

#     print('#' * s)

#     i = 1
#     while i <= s - 2:
#         print('#' + (s - 2) * ' ' + '#')
#         i += 1
#     print('#' * s)            ## 输入为一  可以在最后一行设置 if 变量>=2 来防止打1出2的结果




#1.练习 写一个程序在计算 1 + 2 +.....99+100

# 2.


# s = 0
# x = 1
# while x <= 100: 
#     s += x
#     x += 1
# print(s)



# i = int(input("请输入一个整数： "))
# s = i
# b = 1
# c = 0
# a = 1
# while b <= s:
 
#     for x in range(a, i + 1):
#         print(x, end = ' ')
#         a += 1
#         i += 1
    
#     b += 1


#打印正方形

# s = int(input("ddddddddd:  "))

# c = 1
# while c <= s:
#     a = 1
#     while a <= s:
#         print(a, end = ' ')
#         a += 1
#     print()
#     c += 1


#让用户输入一些整数  当输入负数时结束输入  当输入完成后 打印用户输入的所有整数的值
# 如：
# 输入：1
# 输入：2
# 输入：3
# 输入：4
# 输入：-1
# 打印如下： 您输入的这些数的和是10


  ##死循环例子      输出数求和
# s = 0
# while True:
#     a =int(input("请输入： "))
#     if a < 0:
#         print(s)
#         break
#     k = a
#     s = s + k
  


# #   练习  
# #   1.写程序求下列算式的值
# #   1/1 -1/3 +1/5-1/7+1/9....-（2 * n- 1）
# 1.当n等于10000时  此算式的值
# 2.当n等于10000时   算式的和乘以4  打印结果  （3.14）
# 2.用while 语句打印三角形 输入一个三角形的宽度和高度 打印相应的三角形
# 见 练习5
# 3.用程序while 语句生成如下字符串 并打印结果
# 1.  'ABCD....XYZ'         ord  chr
# 2.  'AaBaCa....XxYyZz '


# a = 1
# s = 65
# while a <= 26:
#     print(chr(s), end = '') 
#     s += 1
#     a += 1
# print()

# #A  65   a = 97

# z = 97
# d = 65
# g = 1
# 
# while g <= 26:
#     print(chr(d), end = '')
#     print(chr(z), end = '')
#     g += 1
#     z += 1
#     d += 1






## 
# z = 1
# s = 3
# c = 1
# while z <= 19999:
  
#     n = 1 / s
#     c = c - n 
#     z += 2
    
#     s += 2 
# d = 1
# g = 0
# n = 1
# while d <= 4999:
#     q = 2 / ((n * 4) + 1)
#     g = g + q
#     n += 1
#     d += 1
# a12 = c + g

# print(a12)
# print(a12 * 4)



#1 - 1/3 + 1/5 ....-1 /(2 * n )-1

# n = 1
# c = 1
# d = 0
# e = 0
# while n <= 10000:

#     if n % 2 == 0:
#         d += c
#     else:
#         e += c
#     n += 1
#     a = 2 * n - 1
#     c = 1 / a
    
# print(e - d)

# print((e - d) * 4)



#1 - 1/3 + 1/5 ....-1 /(2 * n )-1

# j = 1
# n = 1
# s = 0

# while n <= 10000:
#     s += 1 / (2 * n - 1) - 1 / (2 * n + 1)
#     n += 2
# print(s)
# print(4 * s)





















