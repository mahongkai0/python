



# 已知列表
# L=【3,5】
# 用索引和切片操作 讲元列表改为
# L=【1,2,3,4,5,6】



# # 将列表反转  删除最后一个元素再打印此列表
# # print（L）  #【6,5,4,3,2】
# # （尽可能让L绑定的对象的Id不变）

# L = [3,5]


# L = L[::-1]  #反转
# L[-1:] = []   #删除最后一个
#    id 改变   
# L [:] = L [::-1]
# id bubian

# print(L)



# 练习 输入一些正整数  存入列表中 当输入-1 ，的时候结束输入
# 1.打印出列表中的所有的数字
# 2.打印出您输入的数字的最大数
# 3.打印出您输入的这些数的平均值




# L = []
# while True:
#     s = int(input("请输入正整数： "))
    
#     if s < 0:
#         break
       
#     L += [s]

# for x in L:
#     print(x)
# print(L)
# print("zuida",max(L))

   





# 写一个程序 让用户输入两个以上的正整数  当输入负数时 结束输入  
# （要求 限制用户 不允许输入重复的数）
# 1.打印这些数字的和
# 2.打印这些数中最大的一个数
# 3.打印这些数中第二大的一个数
# 4.删除最小的一个数 
# 2.思考
# 如何保证原数据 的结构不变 最后按原来的顺序打印出剩余的数 copy


L = []
while True:
    a = int(input("请输入正整数："))

    
    if a < 0:  #此处再次进行判断  查看已经获取的数据
        if len(L) > 2:
            break
        else:
            print("您输入的数字太少，请继续输入")
            continue
        #判断x是否为输入过的数字
    for a in L:                                #  if L.count(a) != 0
        print("您已经输入过这个数了，请输入其他的数")
        break
    else:
        L.append(a)    #第一次出现  加入到列表中

print(L)

print("这些数的和是： ", sum(L))

L2=L.copy()
L2.sort()  #从小到大排序
print("最大一个数：",L2[L-1])
print("第二大的数是：",L2[-2])
#删除最小的一个数
zuixiao = L2[0]
L2.remove(zuixiao)


# print("最大数的数为：", max(L))
# zuida = max(L)
# L.remove(max(L))
# print("最二大数的数为：", max(L))
# L.append(zuida)
# L.remove(min(L))
# print("最终的结果是",L)




# 上题  join 函数       副本   copy. deepcopy



# 练习：
#   有字符串”hello“  生成字符串”h e l l o“
#  和 ”h-e-l-l-l-o“



# s = "hello"
# L=s.split('')
# print(L)



# L = list("hello")
# s1 = ' '.join(L)
# print(s1)
# s2 = '-'.join(L)  
# print(s2)



# s1 = ' '.join("hello")
# s2 = '-'.join("hello")



# 求100以内的奇数
# L = [x for x in range(1,100,2)] 
# print(L)

# 1.10 奇数平方的和
# L1 = [x ** 2 for x in range(1,10) if x % 2 != 0 ]
# print(L1)


# ######################## 嵌套
# L = [x + y for x in [10,20,30] for y in[1,2,3]]

# print(L) 


# 用字符串'ABC” 和字符串 ”123“  生成如下列表
# 【‘A1’，‘A2’,‘A3’,‘B1’,'B2','B3',‘C1’,‘C2’,‘C3’】

# L = [x + y for x in ["A","B","C"] for y in ["1","2","3"]]
# print(L)





# lianxi
# 1.输入一个开始的整数  用begin绑定
# 输入一个结束的整数   用end邦定
# 将从begin开始   到end结束   （不包含end）的偶数存于列表中 并打印此列表
# # （列表推导式）
# begin = int(input("请输入开始数："))
# end = int(input("请输入结束数："))
# L =[x for x in range(begin,end) if x % 2 == 0]
# print(L)









# 2.已知有字符串 
# s = "100,200,300,500,800"
# 将其转化为列表 列表的内部都为数字
# # L= 【100,200,300,500,800】
# s = "100,200,300,500,800"
# L = [int(x) for x in s.split(',')]

# print(L)


# s = "100,200,300,500,800"
# l = s.split(',')
# y = []
# for x in l:
#     a = int(x)
#     y.append(a)
# print(y)






# 3.已知有一个列表中存在很多数还有重复的 如：
# L=【1,3,2,1,6,4,2.....98,82】
# 1.将列表中出现数字存入一个列表L2中
# 要求：重复出现很多次的数字只能在L2中出现一次   （去重）

# 2.将L列表中出现两次的数字存于另一个列表L3中 在L3中值只保留一份
# L= [1,3,4,446,41,5,1,1,1,2,2,4,6,86,48,21,6,6]
# L2=[]
# # # #L2 =list(set(L))

# # #print(L2)
# L3 = []
# for x in L:
#     if x not in L2:
#         L2.append(x)
# print(L2)
# for x in L2:   ##################### ################################# L
#     count = L.count(x)         ### 如果出现两次 和  没出现过
#     if count ==2: ###################################################and x not in L3:
#         L3.append(x)
# print(L3)


# # L2 =[]
# for x in L:
#     if x in L2:
#         continue
# else:
#     L2.append(x)

# print(L2)







# 4.写程序  生成前40个.....ob数

# 1 1 2 3 5 8 13 .............
# 要求将这些数存于一个列表中  并打印



# a = 0
# b = 1
# c = 1
# L=[]
# while len(L) < 40:
#     L.append(c)
#     c = a + b
#     a = b               三行如一：          a , b = b, a +b
#     b = c
# print(L)
    


# L= [1,1]

# for x in range(38):
#     sum = int(L[x]) + int(L[x + 1])
#     L.append(sum)
# print(L)



# L= [1,1]
# while  len(L) < 40:
#     L = [L[-1] +L[-2]]
# print(L)


# s = "100,200,300"
# for x in s.split(','):
#     a =int(x)
#     x.append(a)
# print(a)















































