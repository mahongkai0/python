

#查看如下字符串中有几个字符

# len('abcd1234') 11111111     8
# len('s\'4"') 1111            4
# len('\"\x34\056')            3
# len('\a\b\c\d') 2211         6
# len('\n\t\r\\')  1111        4



# s = int(input("请输入一个整数"))

# print('#' * s)
# a = 1
# l = s - 2
# for a in range(l):
#     print('#' + (s - 2) * ' ' + '#')
#     a += 1
# print('#' * s)


# x = 'dsnshksjknjjdslm'
# 'l' in x
# True



# 任意输入以段字符串　判断你的名字是否在字符串中　如果存在则打印
# ＇您的名字出现了＇　　　否则不予理采

# s = input("请输入一段字符串：　　")

# x = '马登亮'
# if x in s:
#     print("您的名字出现了")
# else:
#     print("没有您的名字")


# 写程序　输出一行字符串　　输出第一个　最后一个　　如果是奇数　打印中间哪一个

# s = input("请输入一行字符串：　")
# a = len(s)
# print(s[0])
# print(s[a - 1])
# if a % 2 == 1:
#     print(a // 2)　　　　center = int(len(s)//2)
# else:
#     print("这个字符串长度是偶数")




# s = input("请输入一个字符串：　")

# a = len(s)
# print(s[1:a - 1])



# s = input("请输入一个字符串：　")

# print(s[1:a - 1])






# l = input("请输入一个字符串：　")

# if l == l[::-1]:
#     print("它是回文")
# else:
#     print("不是回文")




# s = input("请输入一个字符串")
# if len(s) > 0:   if s:   如果s不为空　则bool(s) 为 True
#     l = s[0]
#     print(ord(l))

# f = int(input("输入：　"))
# if 0 <= f and f <= 65535:
#     a = chr(f)
#     print(a)


# code = int(input("ll"))

# ch = chr(code)
# print(code,'对应的字符是:', ch)

# 输入一个字符串　把输入的字符串中的空格全部去掉
# 打印出处理之后的字符串内容
# 输入三行文字　　让这三行文字在同一个方框内剧中显示　如（请不要输入中文）
# 请输入第一行：　hello！
# 请输入第二行：　I'm studing python!
# 请输入第三行：　I like python!



# s = input("请输入一个字符串")

# a = s.replace(' ','')
# print(a)


# s = input("请输入第一行：　")
# y = input("请输入第二行：　")
# z = input("请输入第三行：　")
# zuida = len(s)
# if zuida < len(y):
#     zuida = len(y)
# else:
#     zuida =zuida
# if zuida < len(z):
#     zuida = len(z) 

# print('+' + (zuida + 2) * '-' + '+')
# print('|' + s.center(zuida + 2) + '|')
# print('|' + y.center(zuida + 2) + '|')
# print('|' + z.center(zuida + 2) + '|')
# print('+' + (zuida + 2) * '-' + '+')


# s = int(input("请输入一个数"))
# l = s
# a = 1
# b = 1
# while a <= s:
#     print(l * ' ' + b * '*')
#     b += 2
#     a += 1
#     l -= 1































