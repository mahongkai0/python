


# # 实现链各个自定义列表相加 
# class Mylist():
#     def __init__(self,iterable = ()):
#         '''此处用给定的可迭代对象iterable创建一个新的列表 绑定此对象的data  实例变量中'''
#         #self.iterable = iterable
#         self.data = [x for x in iterable]
#     def __repr__(self):
#         return "Mylist(%s)" % self.data

#     def __add__(self,rhs):
#         # he= self.iterable + rhs.data
#         # return "Mylist(%s)" % he 
#         return Mylist(self.data + rhs.data)




#     def __mul__(self,rhs):
#         return Mylist(self.data * 2)
#     def __rmul__(self,lhs):
#         print("反向运算符已重载")
#         return Mylist(2 * self.data)
    
#     def __iadd__(self,rhs):
#         '''此方法用于重载 += 运算符'''
        
#         self.data .extend(rhs.data)   # self.data += rhs.data
#         return self

# L1 = Mylist([1,2,3])

# L2 = Mylist(range(4,7))
# print(L2)
# # L3 = L1+L2
# # print(L3)  #  Mylist([1,2,3,4,5,6])
# L1 += L2
# print(L1)

# L4 = L2 + L1
# print(L4)   #Mylist([4,5,6,1,2,3])
# L5 = L1 * 2  
# print(L5)  #Myist([1,2,3,1,2,3])
# L6 = 2 * L1  #  L6= L1.rmul_(2)
# print(L6) ## 需要重载反向运算符重载


# lianxi 
# 实现有序集合类  OrderSet()  能实现两个集合的交集  &    并集|   补集-
# 对称补集  ^,  ==,  != ,   in,   not  in 等操作
# 要求  ： 集合内部用list 存储数据
# 如：
#     s1= OrderSet([1,2,3,4])
#     s2 = OrderSet([3,4,5])
# print(s1 & s2)  #  OrderSet([3,4])
# print(s1 | s2)  #  OrderSet([1,2,3,4,5])
# print(s1 ^ s2)  #  OrderSet([1,2,5])
# if OrderSet([1,2,3]) != s1:
#     print("不相等") 
# else:
#     print("相等")
# if s2 == OrderSet([3,4,5])
#     print('s2 == OrderSet([3,4,5])')
# if 2 in s1:
#     print('2 in s1')
# 答案键 
# orderset.py
# assert  raise  fgtfgb







class A:
    v = 100
    def __init__(self):
        self.v = 200
a1 = A()
a2 = A()
del a2.v
print(a2.v)




























































































