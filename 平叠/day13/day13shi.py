
# import sys
# def myfunc():
#     print("函数开始")
#     sys.exit() #### 不给就为（0）
#     print("...")
    
# myfunc()
# print("结束")


# def myfac(n):
#     print("正在计算",n,'的阶乘')
# def musum(n):
#     print("正在计算1+2+3+...%d的和"% n)
# name1 = 'audi'
# name2 = 'tesla'

# print("day13shi 模块被加载")


####### 要在一个文件下才能被导入
# import day13shi.py
# import.myfac（5）


##-------------------------------------------

#此函数示意模块的隐藏属性
##隐藏属性不会被 from import * 语句导入
##只对from mymod2 import *有效
# def f1():
#     pass
# def _f2():
#     pass
# def _f3():
#     pass

# name1 = 'aaa'
# _name2 = 'bbb'

#### 导入的话只会导进去 f1  和 name1           


# 绝对导入  先找到包的位置 然后再往里找
# 其中  mypack是上一级
# from mypack.menu import show_menu
# show_menu()


# from ..menu import show_menu
# 错误导入
# from ...  超出顶级包







