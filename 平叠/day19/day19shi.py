###enclosure.py

# class A:
#     def __init__(self):
#         self.__money = 100  ##私有属性，只能用此类的方法来调用

#     def borror(self,x):
#         if x <self.__money:
#             return x
#         return 0
# a = A()
# #访问私有属性shibai 
# # print(a.__money)
# # a.__money -= 100

# # print(a.__money)


# print("借钱:",a.borror(20))







# class A:
#     def __init__(self):
#         self.__money = 100  ##私有属性，只能用此类的方法来调用

#     def __m(self):
#         print("私有方法，__m 被调用")
#     def show__info(self):
#         self.__m()
#         print(self.__money)#可以访问

# a = A()
# #a.__m()  # 失败  不允许访问
# a.show__info()
# # a 就是 self
##————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


### poly.py


# class shape:
#     def draw(self):
#         print("shape .draw()被调用")
# class Point(shape):
#     def draw(self):
#         print("正在画一个点！！！")
# class Circle(Point):
#     def draw(self):
#         print("正在画一个圆")
# def my_draw(s):
#     s.draw() # 此处调用谁
# s1 = Circle()
# s2 = Point()
# my_draw(s1)
# my_draw(s2)

##+________________________________________________________________________________________________
# multiple_inherit.py
# class Plane:
#     def fly(self,hight):
#         print("飞机以海拔",hight,"米的高度飞行")
# class Car:
#     def run(self,speed):
#         print("汽车有",speed,'公里/小时的速度行驶')
# class PlanceCar(Plane,Car):
#     'PlaneCar 继承自Plane 和Car类'

# p1=PlanceCar()
# p1.fly(100)
# p1.run(300)

##________________________________________________________________________
#multi_inherit2.py

# class A:
#     def m(self):
#         print("A.m（）被调用！")
# class B:
#     def m(self):
#         print("B.m（）被调用！")
# #小王感觉校长和小李写的类都可以用
# # 
# class AB(A,B):
#     pass
# ab = AB()
# ab.m()  # 请问调用谁  调用A 因为顺序问题


##____________________________________________________________________________________________________________________
############                             棱形问题   
####__________________________________________________________________________________________________________________
##_______________________________________________________________________________________________________________________

# class A:
#     def go(self):
#         print("A")

# class B(A):
#     def go(self):
#         print("B")
#         super().go()

# class C(A):
#     def go(self):

#         print("C")
#         super().go()
# class D(B,C):
#     def go(self):
#         print("D")
#         super().go()
# d = D()

# d.go()######?????????  d b c a
# ## for classmethod in D._mro_:  错误
# ##     print(cls)
# ##__________________________________________________________________________________________________________________________________________________________
# s = "I'm a Teacher"
# sr = repr(s)
# ss = str(s)
# print(sr)
# print(ss)






# # mynumber.py
# class MyNumber:
#     '''自定义一个数字类，这个类用来表示自己定义的数字信息'''
#     def __init__(self,value):
#         self.data = value

    
#     def __str__(self):
#         return "数字:" + str(self.data)
#     def __repr__(self):
#         return "MyNumbre %d" % self.data
#     def __int__(self):
#         n = int(self.data)
#         return n



# n1 = MyNumber(100)
# print(str(n1))      # s数字 100    str(n1)相关于 n1.__str__()
# print(repr(n1))

# i = int(n1)
# print(i)

##############————————————————————————————————————————————————————————————————————————

####   __len__

# class MyList:
#         def __init__(self,iterable=()):
#             self.data = [x for x in iterable]

#         def __repr__(self):
#             return "MyList(%s)" % self.data
        
#         def __len__(self):
#             '''此方法必须返回整数'''
#             #return len(self.data)
#             return self.data.__len__()
#         def __abs__(self):
#             # L=[]

#             # for x in self.data:
#             #     if x <  0:
#             #         x = -x
                
#             #     L.append(x)
#             # return L
#          #—————————————————————————
#             L=[abs(x) for x in self.data]
#             lst = MyList(L)  #创建mylist新型列表
#             return lst
#         def __int__(self):
#             n = int(self.data)
#             return n




# myl = MyList([1,-2,3,-4])
# print(myl)
# print(len(myl))

# print(abs(myl))
# #_________-__

#————————————————————————————————————————————————————————————————————————————————————————————————————
##                ————————终极迭代器示例————————————————————————————————————


class MyNumber:
    '''自定义一个数字类，这个类用来表示自己定义的数字信息'''
    def __init__(self,value = ()):
        self.data = value

    
    # def __str__(self):
    #     return "数字:" + str(self.data)
    # def __repr__(self):
    #     return "MyNumbre %d" % self.data
    # def __int__(self):
    #     n = int(self.data)
    #     return n
    
    def __iter__(self):
        return MyListIterator(self.data)

class MyListIterator():
    '''此类用来创建一个迭代器，此迭代器可以用来访问MyList类型的对象'''
    def __init__(self,lst):
        self.data2 = lst
        self.index = 0  #用来记录此迭代器当前访问的地点
    def __next__(self):
        if self.index >= len(self.data2):
            raise StopIteration
        r = self.data2[self.index]
        self.index += 1
        
        return r

myl = MyNumber([1,-2,3,-4,5])
it = iter(myl)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break