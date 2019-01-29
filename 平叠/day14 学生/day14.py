




# 练习：
#     写一个函数  get_score()  获取学生的成绩（0~100中的整数）
# 如果用户输入的成绩不是0~100中的数 则返回0  
# 如
# def get_score():
#     score = int(input("请输入成绩0~100:")）
#     ...
# score = get_score()
# print("学生的成绩是：",score)



# def get_score():
#     age = int(input("请输入成绩0~100:"))
#     if 0 <= age <= 100:
#         return age
#     return 0
    
    
# try:
#     score = get_score()
     
# except:
#     score = 0


# print("学生的成绩是：",score)


#----------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# 写一个函数 get_age（） 用来获取一个人的年龄信息 此函数规则用户只能输入1~140的整数  
# 如果用户输入其他的数  则直接触发ValueError 类型的错误
# 如：
#     def get_age():
#         ...
#     try:
#         age = get_age()
#         print("用户输入的年龄是：",age)
#     except ValueError as err:
#         print("用户输入的不是1~140的整数！！！") 


# def get_age():
#     age_e = int(input("请输入1~140之间的数："))    
#     if  1 < age_e and age_e < 140:
#         return age_e
#     else:
#         raise ValueError
    
# try:
#     age = get_age()
#     print("用户输入的年龄是：",age)
# except ValueError as err:
#     print("用户输入的不是1~140的整数！！！")



# lianxi 
# 1.有一个集合
# s = {'唐僧','悟空','八戒','沙僧'}
# 用for语句遍历所有元素如下
# for x in s:
#     print(x)
# else:
#     print("遍历结束")
# 请将上面的for语句改写成while语句的迭代器实现
# s = {'唐僧','悟空','八戒','沙僧'}
# int = iter(s)
# while True:
#     try:
#         x = next(int) 
#         print(x)
#     except StopIteration :
#         print("遍历结束")
#         break



#100 50 50  25  25  12.5  6.25
# 2.一个小球从100米高空落下  每次落地后反弹高度为原高度的一半再落下
# 1）写程序算出皮球在第10次落地后反弹多高
# 2）打印出第10次反弹小球经历的总路程
# sum = 100
# for x in range(1,11):
#     x = 100 / (2 ** x) 
    
#     sum += x * 2
    
# print("第10次落地后反弹的高度为：",x)

# print("第10次反弹小球经历的总路程为：",sum)


# def get_last_height(meter,times):
#     for _ in range(times):
#         meter /= 2
#     return meter

# print("第10次落地后反弹的高度为：",get_last_height(100,10))

# def  get_distance(meter,times):
#     s = 0
#     for _ in range(times):
#         #累加下落高度
#         s += meter
#         meter /= 2   #算出反弹高度
#         s += meter   #累加反弹高度
#     return s  
# print("第10次反弹小球经历的总路程为：",get_distance(100,10))



# 3.修改原学生信息管理系统  加入异常处理语句 让程序在任何情况下都能按逻辑正常执行  不至于崩溃
# 如：
# 输入年龄时输入非数字字符会崩溃












































































