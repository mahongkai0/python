






##myyield.py

####此示例示意生成器函数的创建和调用

# def myyideld():
#     print("即将生成2")
#     yield 2
#     print("生成器结束")
# gen = myyideld() # 调用生成器函数生成一个生成器
# print(gen)  # generator

# it= iter(gen)        ##生成器中获取一个迭代器

# print(next(it))      #向迭代器要数据 此时生成器函数才会执行一步
# print(next(it))      #触发 StopIteration 异常

###——————————————————————————————————————————————————————————————————————————————————————————————————————————————
#此示例示意生成器函数的创建  和用for语句来调用生成器函数

# def myyield():
#     yield 2 
#     yield 3 
#     return
#     yield 5 
#     yield 7 
#     print("生成器生成结束")


# it = iter(myyield())  #调用生成器函数生成一个生成器

# print(next(it))
# print(next(it))    #一旦调用return 就触发异常

# print(next(it)).

# print(next(it))

# for x in myyield():
#     print(x)


##______________________________________________________________________________________________________
# myinteger.py

# def myinteger(n):
#     i = 0
#     while i <n:
#         yield i
#         i+=1
# for x in myinteger(10):
#     print(x)

# it = iter(myinteger(20))
# print("------------------------------")
# print(next(it))  # 0
# print(next(it))   # 1

# L= [x for x in myinteger(20) if x % 2 == 1]
# print(L)

#########################################################
####++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
## zip函数的实现

# def myzip(iterable1,iterable2):
#     it1 = iter(iterable1)
#     it2 = iter(iterable2)
#     while True:
#         try:
#             x1 = next(it1)
#             x2 = next(it2)
            
#             yield (x1,x2)
#         except StopIteration:
#             return

# number = [1,2,3,4]
# names = ['z','g','h']
# for x in myzip(names,number):
#     print(x)


#########################################################################################

# names = ['中国','移动']
# def myenumerate(iterable,start = 0):
#     ###return enumerate(iterable,start)
#     int = iter(iterable) # 先拿到迭代器再访问
#     while True:
#         try:
#             x = next(int)
#             yield (start,x)
#         except StopIteration:
#             break
        

# for x in myenumerate(names,101):
#     print(x)   ###(101,'中国')















































