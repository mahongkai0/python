#类属性可以通过类直接访问

# class Humean:
#     '''此示例示意类变量'''
#     count = 0 # 创建类属性（类变量）
# print(Humean.count) #获取类变量绑定的值
# Humean.count= 100 #修改类属性
# print(Humean.count) 

##————————————————————————————————————————————————————————————————————————————————————————————————————————

# class Humean:
#     '''此示例示意类属性'''
#     count = 0
# h1= Humean()
# print(h1.count) #访问类的属性           0
# h1.count = 100   ##创建实例属性（而不是修改类属性）对象访问修改不了  需要借助函数名修改
# print(h1.count) #优先访问实例属性 当实例属性不存在时才返回类属性  100
# print(Humean.count)  ##              0

##++++++++++++++++++++++++——————————————————————————————————————————————————————————————————————————————————————

# class Humean:
#     '''此实例示意类属性'''
#     count = 0
# print(Humean.count)          ###　0
# h1 = Humean()
# h1.__class__.count = 100 #可以通过__class__属性范文lei
# print(Humean.count) ##　１００
# ########################————————————————————————————————————————————————————————————————————————————————————————————————
# class Humean:
#     '''此示例示意类属性'''
#     count = 0  # 创建类属性（类变量）
#     def __init__(self,name):
#         print(name,'对象被创建')
#         self.name = name
#         self.__class__.count += 1
#     def __del__(self):
#         print(self.name,'对象被销毁' )
#         self.__class__.count -= 1
# L = [Humean('孙悟空'),Humean('猪八戒')]
# h1= Humean('沙僧')
# print("现在共有",Humean.count,'个实例对象')
# del L
# print("现在共有",Humean.count,'个实例对象')

##__________________________________________________________________________________________________________________________________________

##class_slots.py
# class Humean:
#     #此列表限定Humean类型的对象只能有一个age属性
#     __slots__ = ['age']
#     def __init__(self,age):
#         self.age = age
#     def show_info(self):
#         print("年龄是：",self.age)
# # h1 = Humean(10)

# h1.show_info()##  10  
# h1.Age = 11  ########### 大写
# h1.show_info() ### 10

##________________________________________________________________________________________________________________
##class_method.py
# 示意用类方法来访问类变量和改变类变量
# class A:
#     v = 0 # 类属性
#     @classmethod
#     def get_v(cls):
#         return cls.v
#     @classmethod
#     def set_v(cls,v):
#         cls.v = v  
# print(A.v)
# print(A.get_v())

# A.set_v(80)
# print(A.get_v())
# print(A.v)

# ###----

# class A:
#     v = 0 # 类属性
#     @classmethod
#     def get_v(cls):
#         return cls.v
#     @classmethod
#     def set_v(cls,v):
#         cls.v = v  

# print(A.get_v())
# a = A()#创建一个对象  根据对象找到这个类然后传
# print(a.get_v()) # 0
# a.set_v(100)
# print(a.get_v()) # 100
# print(A.get_v()) # 100


#####类方法不能访问此类创建的对象的实例属性

# class A:
#     v = 0 # 类属性
#     @classmethod
#     def get_v(cls):
#         return cls.v
#     @classmethod
#     def set_v(cls,v):
#         cls.v = v  

# a1 = A()  # 创建一个对象
# a1.v = 9999  #创建实例属性
# a1.set_v(8888)
# print(A.get_v()) # 8888
# print(a1.get_v()) # 8888










###__________________________________________________________________________________________________________________________________
##static_method.py

# class A:
#     @staticmethod
#     def myadd(a,b):
#         return a + b
# print(A.myadd(100,200)) # 300
# print(A.myadd("ABC",'123')) #ABC123

# a = A()
# print(a.myadd(3,5)) # 8


##——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
##inherit.py

# class Human:
#     '''定义一个学生类'''
#     def say(self,what):
#         print("对你说:",what)
#     def walk(self,distance):
#         print("走了",distance,'公里')


# h1 = Human()
# h1.say('天气变冷了')
# h1.walk('5')

# class Student(Human):
#     # def say(self,what):
#     #     print("说:",what)
#     # def walk(self,distance):
#     #     print("走了",distance,'公里')
#     def studey(self,subject):
#         print("学习",subject)

# print("=================================")
# h1 = Human()
# h1.say('真好')
# h1.walk('15')
# h2 = Student()
# h2.studey("书法")

##——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


#super.py
# class A:
#     def work(self):
#         print("A.work被调用")
# class B(A):
#     def work(self):
#         print("B.work被调用")
#     def do_somthing(self):
#         #调用自己的work
#         self.work()
#         #调用父类的work
#         super(B,self).work()
#         #简写super().work
# b = B()
# b.work()

# #A.work(b) 不推荐用
# #借助于B来调用A类的方法
# super(B,b).work() ##借助于B来调用A类的方法       把b当成B的上一级 即b当成A

# b.do_somthing()

# ##________________________________________________________________________________________________________________________________
# ##super_init.py
# class Human:
#     def __init__(self,n,a):
#         self.name = n                             ##  222
#         self.age = a
#         print("Human.__init__被调用")
#     def show_info(self):
#         print("姓名:",self.name)
#         print("年龄：",self.age)
# class Student(Human):
#     def __init__(self,n,a,s=0):
#         super().__init__(n,a) #显示调用父类的方法      1111
#         self.score = s #在此类中添加新的属性            33333
#         print("Student.__init__被调用")
#     def show_info(self):
#         super().show_info()                       #    5555
#         print("成绩：",self.score)

 
# s = Student("小张",'20')
# s.show_info()                                         ## 44444


















































