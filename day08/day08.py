


# jingli = {'曹操','刘备','孙权'}
# jishuyuan = {'曹操','孙权','张飞','关羽'}
# print(jingli & jishuyuan)
# print(jishuyuan - jingli)
# print(jingli  - jishuyuan)
# if "张飞" in jingli:

#     print("yes")
# else:
#     print('no')
# print(jingli ^ jishuyuan)
# print(jingli | jishuyuan)

########## 用于def创建一个函数

# g = 10  ###################全局变量
# def say_hello(): 
#     ##########################value = 100  如果在say_hello（）运行  会出错  外部无法调用内部变量              
#     print("hello word")
#     print("hello china")
#     print("hello tarena")
#     print(g)
#     ############################ g  =20  出错 修改全局变量不合法
#     ########################调用say_helloo这个函数 三次
# say_hello()
# say_hello()
# say_hello()

# print(g)



# ##############此示例定义用以带有形参的函数       此函数名叫mymax   此函数能接收两个实际调用函数 在函数内部 
# ################# 找出最大的一个打印到终端上
# def mymax(a,b):
#     if a > b:
#         print("a最大")
#     else:
#         print("b最大")


# ################### 调用有参数的函数
# mymax(100,200)

  #写一个函数   myadd 此函数中的参数列表里有两个参数   x，y 打印 x+y
# def myadd(x,y):
#     print(x + y)

# myadd(100,200)
# print()
# myadd("ABC","123")


################### 先有再调

# def print_even(n):
#     s =[x for x in range(n) if x % 2 == 0 ]
#     for x in s:
#         print(x,end = ' ')
# print_even(10)


######################此示例用return给函数的调用者返回信息
# def say_hello_2():
#     print("a")
#     print("d")
#     return[1,2,3,4] ####加了返回  V= 【1,2,3,4】  不加返回none      ########没了 返回调用他的地方                        
#     print("s") 
#    ## return  加不加都行   后面加法 return 1 + 1 
                      
# v = say_hello_2()
# print("v=",v)
#                                     ###两个V  id不同  不是同一个
# v2 = say_hello_2()
# print("v=",v)



######return 练习

# def mymax(x,y):
#     zuida = x
#     if y > zuida:
#         zuida = y
#         return zuida   
# print(mymax(100,200))
# print(mymax("ABC","ABCD"))



# def mymax(a,b):
#     return a if a >b else b
      
# print(mymax(100,200))
# print(mymax("ABC","ABCD"))



# def mymax(a,b):
#     return max(a,b)
      
# print(mymax(100,200))
# print(mymax("ABC","ABCD"))




# 写一个函数  myadd  实现给出两个数  返回这两个数的和
# def myadd(x,y):

# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# print(a,'+', b, '的和是', myadd(a,b))



# def myadd(a,b):
#     return a + b


# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# print(a,'+', b, '的和是', myadd(a,b))


# 此函数用来获取用户循环输入的整数 当输入负数时  结束输入
# # 将用户输入的数字形成列表的形式返回  再用内建函数max，min，sum 求用户输入的最大值 最小值及和

# def input_number():
#     list=[]
#     while True: 
#         a = int(input("请输入整数："))
        
#         if a < 0:
#             break
#         list.append(a)
#     return list
   
# L =rinput_numbe()
# # print("用户输入的最大值：",max(L))
# # print("用户输入的最小值：",min(L))
# # print("用户输入的和：",sum(L))




# def input_number():
#     list=[]
#     while True: 
#         a = int(input("请输入整数："))
       
#         if a < 0:
#             return list          #####return 执行时 粗函数的所有语句都
#         list.append(a)                     ###    list += 【x】
    
                               
# L =input_number()
# print("用户输入的最大值：",max(L))
# print("用户输入的最小值：",min(L))
# print("用户输入的和：",sum(L))



# 1.写一个函数   get_chinese_char_count  此函数实现的功能是给定一个字符串  返回这个字符串中文字数的个数
# def get_chinese_char_count(s):


# s = input("请输入中英文字混合的字符串：")
# print("您输入的中文字符的个数是",get_chinese_char_count(s))
#                    ######中引文编码个数      0x4E00 0x9FA5(包含)
      
# def get_chinese_char_count(s):
#     ge = 0
#     for x in s:
#         if int(0x4E00) <=ord(x) <= int(0X9FA5):        ###可以不加int
#         # if int('0x4E00',16) < ord(x) < int('0x9FA5',16):
#             ge += 1
#     return ge

    

# s = input("请输入中英文字混合的字符串：")
# print("您输入的中文字符的个数是",get_chinese_char_count(s))




# 定义两个函数
# sum3(a,b,c)   用于返回三个数的和
# pow3(x)                 用于返回x的三次方

# 用以函数计算
# 1.计算1的立方 +2的立方 +3的立方的和
# 2.计算1+2+3 的立方的和
# 即  1**3+2**3+3**3       (1+2+3) ** 3

# def sum3(a,b,c):
#     he = a +b + c
#     return he

# def pow3(x):
#     he2 = x ** 3
#     return he2
# print(sum(pow(1),pow(2),pow(3)))
# print(pow3(sum3(1,2,3))
# # print(pow3(he2) ** 3)



# 3.编写函数fun  其功能是计算并返回下列多项式的值
# Sn = 1 + 1/2 + 1/3 +...1/n
# def fun(n):
#     ..
# print(fun2)      1.5
# print(fun3)             1.8333333333333333
# print(fun10)             ?????????

# def fun(n):
#     s = 0
#     y = 1
#     while y <= n:
#         s += 1 / y
#         y += 1
#     return s
# print(fun(2))
# print(fun(3))
# print(fun(10))

# def print_line(char,times):
#
#     print(char*times)
# print_line("^",10)



# L=[]
# def myadd():
   
#     while True:
#         d = {}
#         a = input("请输入名字")
#         if a == "":
#             break
#         b = input("请输入年龄")
#         c = input("请输入成绩")
#         d["name"] = a
#         d["age"] = b
#         d["score"] = c
#         # d.append(d)
#     return d
# print(myadd())
for x in range(1):
    print(x)
