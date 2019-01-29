

##with3.py
##此示例示意一个自定义环境管理器 让其能用于with管理

# class A:
#     def __enter__(self):
        
        
        
#         print("A.enter__被调用！！！")
#         self.file= open("c:/Users/Administrator/Desktop/test/平叠/day20/day20shi.py",encoding = 'utf-8')
#         return  self
#     def __exit__(self,e_type,e_value,e_cb):
#         self.file.close()
#         if e_type is None:
#             print("正常离开with的语句")
#         else:
#             print("在离开with语句时发生了异常：")
#             print("异常类型是：",e_value)
#             print("错误对象是：",e_cb)
#             print("追踪对象是：",e_type)
#         print("A.exitr__被调用！！！，已离开with语句")
        
        


# with A() as a :        # as a  =   a  = A（） 
#     print("这是with语句内部的语句")
#     print(a.file.readline())
#     3 /0 
# print("程序正常退出！！！")



###————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#mynumber.py
# class MyNumber:
#     def __init__(self,value):
#         self.data = value
#     def __repr__(self):
#         return 'Mynumber(%d)' % self.data
#     def __add__(self,other):
#         s = self.data + other.data
#         return MyNumber(s) # 创建一个新对象并返回
#     def __sub__(self,rhs):
#         jf = self.data - rhs.data
#         return MyNumber(jf)

    
# n1 = MyNumber(100)
# n2 = MyNumber(200)
# # #print(n1)

# # n3 = n1.__add__(n2)
# # n3 = n1 + n2  #等同于n3 = n1.__add__(n2)
# # print(n1,'+',n2,'=',n3)
# # print(n3)
# n4 = n1 - n2
# print(n4)
##————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# class MyNu:
#     def __init__(self,iterable = ()):
#         self.data = [x for x in iterable]
#     def __repr__(self):
#         return 'MyNu(%s)' % self.data
#     def __neg__(self):
#         gen = (x for x in self.data)
#         return MyNu(gen)
#     def __pos__(self):
#         gen = (abs(x) for x in self.data)
#         return MyNu(gen)
#     def __invert__(self):
#         return MyNu(reversed(self.data))
#     def __contains__(self,e):
#         return e in self.data



# L1 = MyNu([1,2,3,4,5,6])
# L2 = -L1 
# print("L2=",L2)
# L3 = +L1
# print("L3 = ",L3)
# L4 = ~L1
# print(L4)



# L8 = MyNu([1,-2,3,-4,5])
# print(2 in L8) # Fals

  ##——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————                                                                                                                                                                                                                                           
##_____________________________________________________________________________________________________________________
#　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　索引
# class MyNu:
#     def __init__(self,iterable = ()):
#         self.data = [x for x in iterable]

#     def __repr__(self):
#         return 'MyNu(%s)' % self.data
#     def __getitem__(self,i):
#         return self.data[i]
#     def __setitem__(self, i, k):          #改变列表的值
#         #return self.data[i] == k
#         self.data[i] = k
#     def __delitem__(self,i):  #  删除索引对应的值
#         #raise ValueError
#         del self.data[i]

# L1= MyNu([1,-2,3,-4,5])
# v  = L1[2]  #  L1.__getitem__(2)
# print(v) # 3

# L1[1]  =  +2 #  L1.__setitem__(1, +2)
# print(L1)

# del L1[3] # L1.__delitem__(3)
# print(L1)



##————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
                               ###            大切片示例
##——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# class MyNu:
#     def __init__(self,iterable = ()):
#         self.data = [x for x in iterable]

#     def __repr__(self):
#         return 'MyNu(%s)' % self.data
#     def __getitem__(self,i):
        
#         if type(i) is  int:
#             print("您正在索引操作")
#         elif type(i) is slice:
#             print("您正在切片操作")
#         elif type(i) is str:
#             print("别用字符串进行操作")
#         return self.data[i]
# L1=MyNu([1,-2,3,-4,5])
# # a = L1[0::2]  # ???     L[slice(0,None,2)] 等同于  L.__getitem__（slice(0,None,2)）


# a = L1[0::2]
# print("a=",a)


###）————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# property.py
class Student:
    def __init__(self,s):
        self.__score = s
    @property   
    def score(self):
        return self.__score
    @score.setter
    def score(self,s): #  设置者
        assert 0 <= s <= 100,'成绩校验失败'
        return self.__score

stu = Student(59)
print(stu.score)  # 取值  stu.getscore()
stu.score = 99  #  赋值  stu.setscore(999)
print(stu.score) #999




# stu = Student(59)
# print(stu.getscore()) # quzhi  59
# stu.setscore (99)
# print(stu.getscore())  # 59






















