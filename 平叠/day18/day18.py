

# 用类来描述一个学生的信息（可以修改之前写的Student类)
# 如：

# class Student:
#     ....
# 将这些学生对象存于列表中 写函数或方法实现添加学生和删除xue生信息等操作
# 1.打印学生个数
# 2.打印学生平均成绩

class Student:
    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.score = s
l=[]
def tianjia(n,a,s):

    
    
    sn = Student(n,a,s)
    
    l.append(sn)
def shanchu():
    n = input("请输入要删除的名字：")
    for index, sn in  enumerate(l) :
        if sn.name == n:
            del l[index]
            print("删除成功")
            return 
    print("删除失败")

tianjia("校长",100,50)
tianjia("大长",10,5)
shanchu()
print(len(l))
count = 0
for sn in l:
    count += sn.score
print(count/len(l))























# 能否在不改变原列表类list的基础上，为列表创建一个新的类，mylist类，新类继承原类全部功能，并添加一个insert_head(n)的方法
# 如：
    
# class mylist(list):
#     def insert_head(self,n):
#         #self[0:0] =[n]
#         #self.insert(0,n)
#         q = [n]
#         q += self

# myl = mylist(range(3,6))
# print(myl)  # [3,4,5]
# myl.insert_head(2)
# print(myl) #[2,3,4,5]

# myl.append(6)
# print(myl) #[2,3,4,5,6]



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





# lianxi  


# 1.看懂我写的示例代码














