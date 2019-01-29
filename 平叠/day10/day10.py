




# a = 1
# b = 2
# c = 3
# def fn(c,d):
#     e = 300
    

#     print('locals()返回',locals())
#     print('lgobals()返回',globals())
#     print(c)
#     print(globals()['c'])
# fn(100,200)

# 练习
# 写一个计算公式的解释执行器  已知有如下一些函数
# def myadd(x,y):
#     return x + y
# def musub(x,y):
#     return x - y
# def mumul(x,y):
#     return x * y
# ...
# 另有一个函数表达式get_func  有一个参数op  代表用给定的字符串
# def get_func(op):
#     ..
# 此函数在传入字符串中“加”或“+”  时 返回myadd 函数
# 此函数在传入字符串中“减”或“-”  时 返回mysub 函数
# 在主函数中


# def myadd(x,y):

#     return x + y

# def musub(x,y):
#     return x - y

# def mumul(x,y):
#     return x * y

# def muchu(x,y):
#     return x / y

# def get_func(op):
#     if op == '加' or op == '+':
#         return myadd
#     if op == '-' or op == '减':
#         return musub
#     if op == '*' or op == '乘':
#         return mumul
#     if op == '/' or op == '除':
#         return muchu

# def main():
#     while True:
#         s = input("请输入计算公式：")  # 10 加 20
#         L =s.split(' ')  # L =['10','加','20']
#         a = int(L[0])
#         b = int(L[2])
        
#         fn = get_func(L[1])
#         print("结果是：",fn(a,b))
    
# main()



# 练习
# 用全局变量记录一个函数hello  被调用的次数 部分代码如下：
# count = 0
# def hello(name):
#     print（‘你好啊 ’，name）

# hello('小张')
# while True：
#     s = input('输入人名：')
#     if not s :
#         break
#     hello(s)
# print("hello函数调用的次数是：",count)



# count = 0
# def hello(name):
#     print("你好啊",name)
#     global count
#     count += 1
# hello('小张')
# while True:
#     s = input('输入人名：')
#     if not s :
#         break
#     hello(s)
# print("hello函数调用的次数是：",count)



# 练习 写一个 lambda表达式  此表达式创建一个函数  判断n这个数的2次方+1能否被 5整除 如果能
# 返回 True  不能  返回false
# 如：
# print（fx（3）） True
# print（fx（4）） False

# fx = lambda n: (n ** 2 + 1 ) % 5 == 0
# print(fx(3))
# print(fx(4))      ##  return biaodahsi  直接返回真


# 写一个lambda 表达式 来创建函数 看谁大小
# def mymax(x,y):
#     ..
# mymax = lambda..
# print(mymax(100,200))
# print(mymax("ABC",'123'))



# mymax = lambda x,y: x if x >y else y
# print(mymax(100,200))
# print(mymax("ABC",'123'))



# 练习
# 1.看懂下面的程序在做什么
# def fx(f,x,y):
#     print(f(x,y))
# fx((lambda a,b:a+b),100,200) #300
# fx((lambda a,b: a ** b),3,4)   #81


# 2.写一个函数  musum（x） 来计算
# 1 + 2 + +...x


# def musum(x):
#     a = 1
#     sum= 0
#     while a <= x:
#         sum += a

#         a +=1
#     print(sum)
# s = int(input("请输入一个数："))
# musum(s)








# 3.写一个函数 myfac（n）  求n！
# n！ = 1*2*3*n
# 如：
# print（myfac（5）) 120

# def myfac(n):
#     a = 1
#     cheng = 1
#     while a <= n:
#         cheng = cheng * a
#         a +=1
#     return cheng

# print(myfac(5))      

# 4.写一个函数计算 1 + 2 ** 2+ n ** n + n **n
# 注： n给个小点的数

# def leijia(n):
#     a = 1
#     sum = 0
#     while a <= n:
#         sum += a ** a
#         a += 1
#     return sum
# s = int(input("请输入一个数："))
# print(leijia(s))
#######################################sum(map(lambda x : x ** x,range(1,n+1)))




# 5. 实现一个带有学生管理界面的学生信息管理程序
#  界面选择菜单如下
#  +---------------------------------------+
#  | 1) 添加学生信息                        |
#  | 2)显示学生信息                         |
#  | 3)删除学生信息                         |
#  | 4)修改学生成绩                         |              
#  | q)退出                                |
#  +---------------------------------------|
# 学生信息和存储方法与源程序相同  用列表里包含来存储信息
# 每个功能写一个函数相对应




#添加信息
def myadd():
    if s == 1:
        while True:
            d = {}
            a = input("请输入名字")
            if a == "":
                break
            b = input("请输入年龄")
            c = input("请输入成绩")
            d["name"] = a
            d["age"] = b
            d["score"] = c
            L.append(d)
    return L


#显示信息
def show():
    if s == 2:
        while True:
            print("+----------+----------+----------+")
            print("| 姓名     |   年龄   |   成绩   |")
            print("+----------+----------+----------+")
            for d in myadd():
                sn = d["name"]
                sa = str(d["age"])  # 转为字符串，易于居中
                ss = str(d["score"])
                print("|%s|%s|%s|" % (sn.center(10),
                                        sa.center(10),
                                        ss.center(10)))
            print("+----------+------------+--------+")
            break

#删除信息
def dalate():
    if s == 3:
        while True:
            a = input("请输入要删除的信息")
            if a == "":
                break
            for x in range(len(L)):
                if a == L[x]["name"]:
                    del L [x]
                    break

#修改信息
def mod():
    if s == 4:
        while True:
            a = input("请输入要修改的姓名")
            if a == "":
                break
            for x in range(len(L)):
                if a == L[x]["name"]:
                    L[x]["name"] = input("请输入名字")
                    break


L=[]
while True:
    print(1,"添加学生信息")
    print(2,"显示学生信息")
    print(3,"删除学生信息")
    print(4,"修改学生信息")
    print("q","退出")
    s = int(input("请按照输入"))
    if s == 1:
        myadd()
    if s == 2:
        show()
    if s == 3:
        dalate()
    if s == 4:
        mod()
    if s == "q":
        break

























































