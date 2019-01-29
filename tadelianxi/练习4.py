# s = input("请输入一个字符串:")
# if s:
#     print("第一个字符:", s[0])
#     print("最后一个字符:", s[-1])
# if len(s) % 2 == 1:
#     center = int(len(s) // 2)
#     print("中间这个字符是", s[center])
# else:
#     print("您输入的字符串是空")



# s = input("请输入一个字符串")
# a = len(s)
# if a <= 2:
#     print("您输出错误")
# b = a - 1
# print(s[1:b])

#看思维：　
# s = input("请输入字符串")
# if s:
#     s2 = s[1:-1]   #或者s[1:len(s)-1]
#     print("处理后打字符串为：", s2)





# # s = input("请输入一个字符串")
# # #a = len(s)
# #                              # l = -a
# # b = s[::-1]
# # if s == b:
# #     print("这个字符串是回文")
# # else:
# #     print(s, "它不是回文")



# # s = input("请输入一段字符串")
# # s1 = s[:1]
# # if len(s) != 0:       # if x != ''  c =x[0]
# #                          # 等同于　if x:
# #     print(ord(s1))
# # else:
# #     print("您输入的是空值")



# s = int(input("请输入一个整数0～65535    "))
# print(chr(s))


# a = input("请输入第一行")
# b = input("请输入第二行")
# c = input("请输入第三行")

# zuida = len(a)
# if len(b) > zuida:
#    zuida = len(b)
# if len(c) > zuida:
#     zuida = len(c)
# print("最长的字符个数是", zuida)
# l = '+' +'-' * (zuida + 2) + '+'
# print(l)

# l2 = '|' + a.center(zuida + 2) + '|'
# print(l2)
# print ("|" + b.center(zuida + 2) + '|')
# print ("|" + c.center(zuida + 2) + '|')

# print(l)








# # # # i = 1
# # # # while i < 21:
# # # #     print(i)    # print(i,end='\n')
# # # #     i = i + 1

# # # # i = 1
# # # # while i < 21:
# # # #     print(i, end = '  ')
# # # #     i = i + 1   
# # # # print()    # print(end='\n')










# # # #用while循环打印　1～　20　的整数，打印在一行显示每个数字
# # # #之间用一个空格分离



# # # i = 1
# # # while i < 6:
# # #     print(i, end = ' ')
# # #     i = i + 1      # if i == 5:
# # # print()                # print()     
# # # while i < 11:                        # if i == 10:
# # #     print(i, end = ' ')                  # print()
#
             # #     i = i + 1                    #  以此类推
# # # print()
# # # while i < 16: 　　　　　　　　　　#if i == 5 or i ==10
# # #     print(i, end = ' ')           # or i == 10 or i == 15
# # #     i = i + 1                   # or i == 20
# # # print()                                   #亦或
# # # while i < 21: 　　　　　　　　　　　　# if i % 5 == 0:
# # #     print(i, end = ' ')
# # #     i = i + 1



# # #输入一个整数ｎ，　打印一个宽度和高度都为n个字符的长方形



# # n = int(input("请输入一个整数"))

# # l = n * '＃'
# if n ==1:
#     print("＃")
# else:
#     print(l)
#     s = '＃' + (n - 2) *  '  ' + '＃'
#     i = 1
#     while i <= (n - 2):
    
#         print(s)   #控制一个＃号时　　可以不加ｉｆ　　ｅｌｓｅ
#         i = i + 1　　　　改换条件　ｉｆ　ｎ＞＝2　打印最后一行
#     print(l)



# 输入一个整数ｎ代表结束的数值　求下列表达式的和
# 1＋2＋3+4+...+(n-1)+n的和
# 如　输入　100　　　打印5050


# n = int(input("请输入一个整数  "))
# s = 0
# i = 1
# while i <= n:
#     s = s + i
#     i = i + 1
# print(s)



# money = int(input("请输入商品总额"))
# pay = money - 20 if money >= 100 else money
# print("您需要支付:", pay, "元")




``

大纲

