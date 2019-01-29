



####### 要在一个文件下才能被导入
# import day13shi
# day13shi.myfac(5)
# day13shi.musum(10)
# print(day13shi.name1)

# from day13shi import *
# myfac(20)
# # from day13shi import name2
# print("name2",name2)



###注： 此__all__列表限制在from day13 import *  
# __all__ = ['f1','name1']  ### 放哪个导过去哪个
# def f1():
#     pass
# def f2():
#     pass
# def f3():
#     pass

# name1 = 'aaa'
# name2 = 'bbb'
###############dir(day13)   5个变量

###


# 练习：
# 1.猜数字游戏 
# 随机生成一个 1 100 之间的一个整数  用变量x绑定
# 让用户输入一个数用变量y绑定 然后输出猜数字的结果
# 如果 y 等于 生成的x  提示猜对  反之猜大或者猜小继续猜 最后打印次数
# import random
# count = 0
# x = random.randrange(1,101)
# #print("系统生成数：",x)
# while True: 
#     count += 1
#     y = int(input("请输入一个1到100之间的整数："))   
    
#     if y == x:
#         print("您猜对了")      
#         print("您猜了",count,'次')
#         break
#     elif y > x:
#         print("您猜的数字大了，请继续")     
#     elif y<x:
#         print("您猜小了，请继续")
        

# lianxi 
# 1.写一个程序  模拟斗地主发牌 牌共54张
# 种类有 黑桃 '\u2660'   梅花  '\u2663'      9824  9827   9829  9830 
#         红桃 '\u2665'  方块  '\u2666'

# 数字有 A2 -10JQK
# 大王和小王
# 输入回车  打印第一个人的17张牌
# 输入回车  打印第二个人的17张牌
# 输入回车  打印第三个人的17张牌
# 输入回车  打印 3张底牌


import random
L = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']  ##生成 2~10 s = [str(x) for x in range(2,11)]
L1 = ['\u2660','\u2663','\u2666','\u2665']
L3 = []                                                 #  s += list("JQK")

def sha(x):
    for y in x:
        L3.remove(y)

# random.shuffle(L3)
#assert len(s) == 54, '出错，断言'
for x in L:
    for y in L1:
        s = y + x 
        L3.append(s)

L3 += ['大王','小王']
# 洗牌

random.shuffle(L3)
one =random.sample(L3,17)
sha(one)
two =random.sample(L3,17)
sha(two)
three= random.sample(L3,17)
sha(three)
##————————————————————————————————-——————————————
##|one = L[:17] two = [17:34] three = [34:51]  |
##-——————————————————————————————————————————————

input()
print("一",one)
input()
print("二",two)
input()
print("三",three)
input()
print('底牌',L3)














   
# 2将学生信息管理系统拆分为模块
# 要求
# 1. 主时间循环的main函数放在 main.py中
# 2. 显示菜单的函数show_menu 放在menu.py中
# 3.与学生信息操作相关的函数放在student_info.py中













