

# s = sum(range(1,101))

# print(s)



# 练习 
# 求 1  **2   + 2 ** 2+ 3** 2 + ...9** 2 的和
# # 求 1**3 + 2**3+3 *3 + ..9**3
# # 1 ** 9  2** 8 ..... 9**1
# sum = 0
# for x  in map(pow,range(1,10),[2]*9):
#     sum += x
# print(sum)


# s = 0
# for x  in map(pow,range(1,10),[3]*9):
#     s += x
# print(s)

# ss = 0
# for x  in map(pow,range(1,10),range(9,0,-1)):
#     ss += x
# print(ss)


# # def pow2(x):
# #     return x**2
# # s = 0
# # for x in map(pow2,range(1,10)):
# #     s += x
# print(x)


# s = 0
# for x in map(lambda x : x ** 2 ,range(1,10))
#     s += x
# print(x)              


# s = sum(map(lambda x : x**2 ,range(1,10))) ####################    核心算法！！！！！！
# print(s)


# 练习
# 用 filter 函数将1 ~100之间所有的素数prime存放于列表中

# def isprime(x):
#     if x < 2:
#         return False
    

#     for i in range(2,x):
#         if x % i == 0:
#             return False
           
#     return True


# L =list(filter(isprime,range(1,100)))
# print(L)


# L=[x for x in filter(isprime,range(100))]
# print(L)




# 练习  
# 将下列列表中的数据进行排序
# L=[{1,5},(3,9),(4,1),(3,6),(5,3)]
# 1.将列表内的元组按第二个数据的从小到大的顺序排序
# 结果如下
# 自己拼

# L=[(1,5),(3,9),(4,1),(3,6),(5,3)]

# L1=sorted(L,key = lambda x :x[1])
# print(L1)
# # 2.将列表内的五个元组按第二个数的从小到大顺序进行排列 打印排序之后的结果

# LK=[(1,5),(3,9),(4,1),(3,6),(5,3)]

# L2=sorted(L,key = lambda x :x[1],reverse = True)           #####  lambda x ： x[1]  是指列表在进到函数里面
# print(L2)
# 3.假设元组中的数据是数学直角坐标系的坐标  则按他们距离原点的距离进行排序
# （提示：  距离等同于  distance = sqrt（x**2 + y**2））
# K=[(1,5),(3,9),(4,1),(3,6),(5,3)]
# Ls = sorted(K,key = lambda t :((t[0] ** 2 + t[1] ** 2)) ** 0.5      )
# print(Ls)







# L=[(1,8),(3,4)]
# def xx(t):
#     print(t)
#     return t[1]
# # print(xx(L) )

# L2 =sorted(L,key = xx)
# print(L2)

####################################0      递归函数

# def fx(n):
#     print("递归进如第",n,'层')
#     if n == 3:
#         return
#     fx(n+1)
#     print("递归退出",n,"层")
# fx(1)               #先创建个数据对象
# print('程序结束')

##############################################阶乘大法
# def myfac(n):
#     if n ==0:
#         return 1
#     s = n * myfac(n - 1)   # 求n的阶乘
#     return s
# print(myfac(5))




# 试写一个递归函数  mysun（n）， 此函数用递归方式求   1+2+3+4+5+...n的和


#####################
# s = 0
# def mysun(n):
#     global s
#     if n == 0:
#         return 
#     s += n
#     mysun(n - 1)
#     return s
# print(mysun(100))
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# def mysun(n):
#     if n == 1:
#         return 1
    
#     return n + mysun(n -1)
    

# print(mysun(100))



# 已知有五位朋友在一起
# 第五个人说他比第四个人大2岁
# 第四个人说他比第san个人大2岁
# 第三个人说他比第er个人大2岁
# 第二个人说他比第1个人大2岁
# 第一个人说他10岁

# 写函数 get_age(n) 求 第三个人几岁  第五个人几岁


# def get_age(n):
    
#     if  n == 20:
#         return 
    
   
#     print("第",int(n / 2 - 4),'个人',n,'岁')
#     get_age(n + 2)
    
    
# get_age(10)



# def get_age(n):
#     if n == 1:
#         return 10
#     else:
#         return get_age(n-1) + 2
# print("3",get_age(3)) 
# print("5",get_age(5))

###闭包  把money变量放在外部嵌套函数作用域内       特点 能延长外部函数变量的使用时间
#                                                 #一个函数关联另一个函数的执行环境
# def give_yasui_money(m):
#     money = m   
  
#     def child_buy(obj,m):
    
  
   
#         nonlocal money

#         if money > m:
#             money -= m
#             print('买',obj,'花',m,'元')
            
#             print("剩余",money,"元")
#         else:
#             print("您的钱不够，购买失败了勇士")   
#     return child_buy
# cb = give_yasui_money(1000)
# cb('变形金刚',200)
# cb('水果',100)
# cb('手机',1300)


#创建一系列的函数

# def xx(y):
#     def fn(x)；
#         return x ** y
#     return fn



# 1.已知有列表
# L=[[3,5,8],10,[[13,14],15,18],20]  递归  type
# 写一个函数  print_list(lst) 打印出所有的数字
# 如：
# #     print_list(L)  #打印 3 5 8 10 13 14 


# L=[[3,5,8],10,[[13,14],15,18],20]
# def print_list(lst):
#     for x in lst:
#         if type(x) is int:
            
#             print(x,end = ' ')
#         else:
#             print_list(x)
            
# print_list(L)
                           ### 想换行可以再最后调用的函数里面加个  ture （第一次运算） 在第一函数参数里面加个 li = False
                           # ### 下面加代码  如果  if li：   print（） 
# d = []
# def print_l(lst):
#     for x in lst:
#         if type(x) is int:
            
#             d.append(x)
#         else:
#             print_l(x)
            
# print_l(L)
# print()
# print("和是：",sum(d))


# 写一个函数  sum_list(lst)  返回这个列表中所有数字的和
# 如 
# print(sum_list(L)) # 106





# # 2.写程序求出 1~20  阶乘的和
# # 1！+ 2! + 3!+...20!
###### 1111111111111111111111111111111
# def jiecheng(n):
    
#     if n == 1:
#         return 1
#     s = n * jiecheng(n-1)
#     return s 
# sum = 0
# def he():
#     global sum
#     for x in range(1,21):
#         jiecheng(x)
#         sum += jiecheng(x)
#     return sum
# print(he())

######################  2222222222222222222


# def factorial(x):
#     if x ==0:
#         return
#     return x * factorial(x - 1)
# s = sum(map(factorial,range(1,21)))
# print(s)














# 3.改写之前的学生信息管理系统 添加如下四个工能
# | 5) 按学生成绩高~低显示学生信息 |
# | 6) 按学生成绩低~高显示学生信息 |
# | 7) 按学生年龄高~低显示学生信息 |
# | 8) 按学生年龄低~高显示学生信息 |




L=[]


def tianjia():
    while True:
        d = {}
        name = input("请输入学生姓名：")
        if name == '':
            break
        age = str(input("请输入学生年龄: "))
        score = str(input("请输入学生成绩: "))
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
        # for x in range(len(L)):
        #     if name == d[x]['name']:
        #         print("您已经添加过了，请重新输入：")
        #         break
        #     else:
        #         L.append(d)

    return L


def xianshi(L):
    print("+------+------+------+")
    print("| 姓名 | 年龄 |  成绩|")
    print("+------+------+------+")
    for x in range(len(L)):
        print(
            "|" + L[x]['name'].center(6) + "|" + str(L[x]['age']).center(6) + "|" + str(L[x]['score']).center(6) + '|')
    print("+------+------+------+")

def shanchu(L):
    shanchu = input("请输入您所要删除的姓名名称：")
    if shanchu == '':
        return
    for x in range(len(L)):
        
        if shanchu == L[x]["name"]:
            del L[x]
            print("删除成功")
            return
        
        
    print("您输错了")

# def shanchu(L):
#     shanchu = input("请输入要删除学生的姓名: ")
#     # 方法1
#     # for d in L:
#     #     if d['name'] == name:
#     #         L.remove(d)
#     #         print("删除成功")
#     #         return
#     for i in range(len(L)):  # i代表列表的索引
#         d = L[i]
#         if d['name'] == shanchu:
#             del L[i]
#             print("删除成功")
#             return
#     print("删除失败")



def xiugai():
    xiugai = input("请您输入要修改的姓名：")
    if xiugai == '':
        return
    else:
        xiuhou = input("请您输入修改后的成绩：")
        if xiuhou == '':
            return
        for x in range(len(L)):
            if L[x]["name"] == xiugai:
                L[x]["score"] = xiuhou
                return


def sore_di(x):
    return int(x['score'])


def show_info(L):
    li = sorted(L, key=sore_di)
    xianshi(li)


def sortgao(L):
    da = sorted(L, key=sore_di, reverse=True)
    xianshi(da)

def age_zheng(x):
    return int(x['age'])


def age_di(L):
    sss = sorted(L, key=age_zheng)
    xianshi(sss)

def age_gao(L):
    ssss = sorted(L, key=age_zheng, reverse=True)
    xianshi(ssss)

while True:

    print("+---------------------------------------+")
    print("| 1) 添加学生信息                        |")
    print("| 2)显示学生信息                         |")
    print("| 3)删除学生信息                         |")
    print("| 4)修改学生成绩                         |")
    print("| 5) 按学生成绩高~低显示学生信息         |")
    print("| 6) 按学生成绩低~高显示学生信息         |")
    print("| 7) 按学生年龄高~低显示学生信息         |")
    print("| 8) 按学生年龄低~高显示学生信息         |")
    print("| q)退出                                 |")
    print("+--------------------------------------- |")
    bianhao = str(input("请亲输入编号："))

    if bianhao == '1':
        L = tianjia()
    elif bianhao == '2':
        xianshi(L)

    elif bianhao == '3':
        shanchu(L)

    elif bianhao == '4':
        xiugai()
    elif bianhao == "q":
        break
    elif bianhao == "6":
        show_info(L)
    elif bianhao == "5":
        sortgao(L)
    elif bianhao == "8":
        age_di(L)
    elif bianhao == "7":
        age_gao(L)
    else:
        print("您输错了，请重新输入")





























































