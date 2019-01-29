


# def div_apple(n):
#     print("%d个苹果想分组几个人？"%n)
#     s = input("请输入人数")
#     count =int(s)      ##可能触发ValueError错误
#     result = n / count           ###  
#     print("每一个人分了",result,'苹果')


# try:
#     div_apple(10)
#     print("分苹果成功")

# ## except (ValueError,ZeroDivisionError):
# ##     print("N")

# except ValueError as err:        ### 绑定错误对象   
#     print("分苹果失败",err ,'=' )
# except ZeroDivisionError:  ###(count = 0)
#     print("没有人来")

# # except:
# #     print("除ZeroDivisionError，ValueError类型的错误发生了")
# #     print("错误已被捕获")

# finally:    #### 即使报错 也一定会执行
#     print("我是try里的finally语句 我一定会被执行")

# print("正常结束")


#####—————————————————————————————— ------------------------------------- 示例  try -finally

# def fry_ege():
#     try:
#         print("打开天然气点燃：")
#         try:
#             count = int(input("请输入鸡蛋个数："))
#             print("共剪了%d个鸡蛋" % count)
#         finally:
#            print("关闭天然气")  ##此事必须做
#      except ValueError:
#         print("不好了，煎鸡蛋失败了！！！,快跑啊")
# fry_ege()

#######----------------------------------raise--------------------------------------

# def make_except():
#     print("开始....")
#     #raise ValueError    #触发一个ValueError类型的异常           raise ZeroDivisionError 也可以触发错误
#     #创建一个错误对象用error 来绑定
#     error = ValueError("xxx大街xxx号着火了")
#     raise error
#     print("结束....")
# try:
#     make_except()
#     print("make_except 调用完成")
# except ValueError as err:
#     print("收到 ValueError 的类型通知")
#     print("err=",err)

# print("程序正常结束")



# def f1():
#     n = int(input("请输入整数："))   ###   此处可能触发  ValueError


# def f2():
#     try:
#         f1()
#     except ValueError as err:
#         print("f1函数内出错")
#         print("f2里的err =",err)
#         #raise err
#         raise #ValueError("aaaaaaaaaaa")
# try:
#     f2()

# except ValueError as err:
#     print("f2内发生ValueError类型错误")
#     print("err=",err)



##——————————————————————————————————————————————————————————————————————————————————————————————


#####assert.py

# def get_score():
#     s = int(input("请输入学生成绩:"))
#     #此语句assert让s不再范围内主动报错
#     assert 0 <= s <=100 , '成绩超出范围'
#     return s
# try:
#     score = get_score()
#     print("成绩是：",score)
# except AssertionError as err:
#     print("断言失败，",err)

###-————————————————————————————————————————————————————————————————————————————————————————————————————————

### except.py
# def f1():
#     '''此函数可能发生错误'''
#     s = "我是错误信息"
#     raise ValueError(s)
    
# def f2():
#     f1()
# def f3():
#     f2()
# def f4():
#     f3()
# try:
#     f4()
# except ValueError as err:
#     print("err=",err)

##___________________________________________________________________________

##迭代器
# L= [1,3,5,7]
# it = iter(L)  # 从对象  L 中获取迭代器 然后用it变量绑定

# print(next(it)) # 1
# print(next(it)) # 3
# print(next(it)) #5
# print(next(it)) # 7

# print(next(it)) #StopIteration异常

##==================================================================================

##iterator.py
#此示例示意用迭代器遍历一个列表
# L=[1,2,3,4]
# #先让L提供一个迭代器
# it = iter(L)
# #循环从迭代器中获取数据 直到接收到 StopIteration 异常为止
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration :
#         break
# ## 以上多条语句可以用如下的for循环实现  for 语句实质就是上面的情况

# for x in L:
#     print(x)

#3---_____________________________________________________________________________________








































































