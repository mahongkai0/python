
# 首先示例while的嵌套
# 　打印1　到20　　十行

# s = 1

# while s <= 10:
   
#     #print("此行语句会执行10次")
#     i = 1
#     while i <= 20:
#         print(i, end = ' ')
#                              #if i == 10:
#                                 #   break 打断
#         i += 1
        
#     print() 
#     s = s + 1


# 输入一个整数ｎ　打印指定宽度的正方形
# 如：
# 　　　请输入　5　　　　　　　　　　　　　　　　请输入3
# 　　打印：　　　1　2　3　4　5　　　　　　　　　1　2　3
# 　　　　　　　　1　2　3　4　5　　　　　　　　　1　2　3
# 　　　　　　　　1　2　3　4　5　　　　　　　　　1　2　3
# 　　　　　　　　1　2　3　4　5
# 　　　　　　　　1　2　3　4　5

# n = int(input("请输入一个整数　　"))

# s = 1
# while s <= n:
#     i = 1
#     while i <= n:
#         print(i, end = ' ')
#         i = i + 1
#     print()
   
#     s += 1
    







# 示例　break的使用


# i = 1
# while i < 6:
#     print("循环开始时的ｉ=", i)
#     if i == 3:
#         break
#     print("循环结束时的ｉ=", i)
#     i += 1
    
# else:
#         print("while里的else子句被执行")
# print("程序结束")


 
       # 让用户输入一些整数，当输入负数时结束输入　　当输入完成
         #　后，打印您输入这些数的总和
 


# s = 0
# while True:
#     n = int(input("请输入："))
#     if n < 0:
#         break
#     s = s + n

# print("您输入的总和是：", s)   

# s = "ABCDE"
# for ch in s:
  
#     print("ch---->", ch)
#     if ch == 'C':
#         break
# else:
#      print("for语句的else子句被执行")



# 练习：
# 　　任意输入一段字符串
# 　　计算出这串中空格的个数
# 　　　计算出字符串中中文字符的个数
# 　　　　　　（注：中文　字符的编码值一定要大于128，可用ord判断）

   #单纯计算空格          # x = input('请输入一段字符串')
                        # print("空格的个数是：　", x.count(' '))



# x = input("请输入一段文字:")

# #print("空格的个数是：　", x.count(' '))
# blank_count = 0
# for c in x:
#     if c == ' ':
#         blank_count += 1
# print("空格的个数是：", blank_count)
# chinse_count = 0
# for c in x:
#   if ord(c) > 128:
#       chinse_count += 1
# print("中文的字符个数是：", chinse_count)

# 用while                                 
# i = 0
# while i < len(x)
#     c = x[i]



#示意生成range 函数
# for x in range(4):
#     print(x)   


# 打印1~20的整数　打印在一行　用for实现
# 计算1＋2＋...＋100　的和　　用for 和range实现
# 计算　1＋3+5+...97+99  的和　　用for 实现
# 　　




# for x in range(1,21):
   
#    print(x, end = ' ')
     
# print() 



# s = 0       
# for c in range(1,101):
#     s += c
# print(s)
    



# s = 0
# for x in range(1,100,2):
#     s += x
# print(s)




# continue的用法
# for x in range(0,10):
#     if x % 2 == 0:
#         continue
#     print(x)

# i = 0
# while i < 10:
#     if i % 2 == 0:
#         i += 1           切记：　这行代码如果没有将会出现无xian空值
#         　　　　　　　　　　　　　　因为ｉ＝　0
#         continue
#     print(i)
#     i += 1
  
  #  求1到100之间所有不能被2.3.5.7整除的数的和



# s = 0

# for x in range(1,101):
#     if x % 2 == 0:
#         continue
#     if x % 3 == 0:
#         continue
#     if x % 5 == 0:    
#         continue
#     if x % 7 == 0:
#         continue
#     s += x   
# print(s)


# 　　输入一个整数　此整数代表三角形直角边长
# 　　根据整数n打印如下四种三角形
#       请输入：　3
#       　　打印如下：
# 1.      　　　   *
#       　　　　　　**
#                 ***

# 2.              *
#                **
#               ***
# 3.            
#               ***
#               **
#               *
# 4.
#                ***
#                 **
#                  *
# 
# 2.写一个程序，任意输入一个整数，判断这个整数是否是素数
# （prime）　　素数也叫质数，只能被自己和1整除
# 　提示：
# 　　　用排除法　当判断ｘ是否为素数时　　只要让x分别
# 　　　　　　　　除以　2，3，4，x -1,只要又一个能整除
# 　　　　　　　　则ｘ不是素数　，否则ｘ是素数


# 3.输入一个正整数代表正方形的宽和高　打印如下正方形
# 如：　　请输入：　5
# 　　　打印：
# 　　　　　　1　2　3　4　5
# 　　　　　　2　3　4　5　6
# 　　　　　　3　4　5　6　7
# 　　　　　　4　5　6　7　8　
# 　　　　　　5　6　7　8　9
# 　如：　请输入：　3
# 　打印：　　　
# 　　　　　1　2　3
# 　　　　　2　3　4
# 　　　　　3　4　5



# s = int(input("请输入一个整数:"))
# c = s
# m = 1

# while m <= s:
#     print('*' * m)
#     m += 1
# print()
# l = 1
# while l <= s:
#     print(' ' * (s - l) + '*' * l)
#     l += 1
# print()
# j = 1
# while j <= s:
#     print('*' * s)
#     s = s - 1
# print()


# #  s 递减　想办法改变ｓ变量
# y = 1
# e = 0
# while y <= c:
#     print(e * ' ' + c * '*')
#     c = c - 1
#     e += 1 


#   　
# s = int(input("请输入一个整数：")) 

# b = True   标记一下
# for x in range(2, s):　　　　遍历
#     if s % x == 0:　　　　　　　
#         b = False　　　　　　　　如果有一个数还可以除尽的话　　直接打断改变标记　
#         break　　　　　　　　　　　　　　　　　　　　
# if b:　　　　　　　　
#     print ("YES")　　　　　　　　　　　　　　　　没被改变　证明不能被整除　　为质数
# else:　
#     print ("NO")　　　　　　　　　　　　　　　　　　　　　能被整除      证明不是质数

      
      

# s = int(input("请输入一个整数"))

# k = 1
# a = range(1,s + 1)
# for x in a:
#     print(x, end = ' ')

#     k += 1        
# print() 
# for y in range(k, 2 * s -1):
    
#     if k <= 2 * s - 1:
#        print(y)   



 

# 实心正方形
# s = int(input("请输入一个整数"))


# for x in range(1,s + 1):
#     if x <= s:
#         print(s * '* ' + s * ' ')
#         x += 1
    

# 空心正方形
# s = int(input("请输入一个整数"))
# i = 1
# for x in range(1,s + 1):
#      if x == 1:
#          print(s * '* ')
#      if x <= s - 1:
#          print('*' + (s - 2)* '  ' + ' *')   #为了美观　可按规则算
#      if x == s and s != 1:
#          print(s * '* ')






# 实心正方形

#  rows = 6

# for i in range(6):
#     for j in range(6):
#         print(' *', end='')
#     print()


# rows = 6

# for i in range(rows):
#     if (i == 0) | (i == rows-1):
#         for j in range(rows):
#             print(' *', end='')
#     else:
#         for j in range(1):
#             print(' *', end='')
#         for j in range(rows-2):
#             print('  ', end='')
#         for j in range(1):
#             print(' *', end='')
#     print()






for x in range(100,1000):
    s = str(x)
    if s * [0] ** 3 +s * [1] ** 3+s[2] ** 3 == s:
        print(s)






















