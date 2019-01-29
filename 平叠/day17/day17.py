## 定义一个人的类

# class Human:
#     def set_info(self,name,age,adress = '不详'):
#         '''此方法为self对象添加姓名,年龄,家庭住址属性'''
        
#         self.name = name
#         self.age = age
#         self.adress = adress
#     def show_info(self):
#         '''此方法显示某个人（实例
#         ）的信息 '''
#         print(self.name, '今年',self.age,"岁,家庭住址:",self.adress)


# h1= Human()
# h1.set_info('校长','20','北京市朝阳区')
# h2 = Human()
# h2.set_info('小李',18)
# h1.show_info()  # 校长 今年  20 岁，家庭住址： 北京市朝阳区
# h2.show_info()  #小李  今年 18 岁， 家庭住址：不详 

##思考
#h3 = Human('小王','19','上海市')  出错 


# 练习
# 写一个学生类  Stdent类  此类用于描述学生信息  学生信息有姓名  年龄成绩 （默认为0）
# 1.为该类添加初始化方法，实现在创建对象时自己自动设置  姓名年龄成绩
# 2.添加 set_score 方法能力对象修改成绩信息
# 3.添加show_info方法打印学生对象的信息
# 如：

# class Student:
#     def __init__(self,n,a,s =0):
#         self.name = n
#         self.age = a
#         self.score = s
        
#     def set_score(self,s):
#         self.score = s
       

#     def show_info(self):
#         print(self.name,self.age,'岁','成绩',self.score)




# L = [] 
# L.append(Student('小张',20,100))
# L.append(Student('小李',18,98))
# L.append(Student('小王',19))
# L[2].set_score(80)
# for s in L:
#     s.show_info() # 显示每个对象的信息


#练习
# 年龄;age
# 姓名  name
# 钱  money
# 技能 skill
# 有两个人
# 1.姓名： 张三 年龄：35
# 2.姓名： 李四 年龄：15
# 行为：
#     1.教别人学东西   teach
#     2.工作赚钱 work
#     3.借钱 borrow（从xxx出借钱）
#     4.显示自己的信息 show_info
# 事情：
#     张三 教 李四 学 python
#     李四 教 张三 学 王者荣耀
#     张三 上班赚钱 1000 原
#     李四 向 张三 借钱 200 元
#     35 岁的 张三 有钱 800 元 他学会的技能是王者荣耀
#     15 岁的 李四 有钱 200 元，他学会的技能是：python
# 如：
# class Human:
#     def __init__(self,n,a):
#         self.name = n  # 姓名
#         self.age = a  # 年龄
#         self.money = 0 # 钱数
#         self.skill = []  #  技能
       
#     def teach(self,other,subject):
#         print(self.name,'教',other.name,'学',subject)
#         other.skill.append(subject)
#     def work(self,money):
#         self.money += money
#         print(self.name,'上班赚钱',money,'元')
#     def borrow_from(self,other,money):
#         print(self.name,'向',other.name,'借钱',money,'元')
#         self.money += money
#         other.money -= money
#     def show_info(self):
#         print(self.age,'岁的',self.name,'有钱',self.money,'他学会的技能是',self.skill)
# zhang3 = Human('张三','35')
# li4 = Human('李四','15')
# zhang3.teach(li4,'python')
# li4.teach(zhang3,'王者荣耀')      
# zhang3.work(1000)
# li4.borrow_from(zhang3,200)
# zhang3.show_info()
# li4.show_info()
    # 35 岁的 张三 有钱 800 元 他学会的技能是王者荣耀
    # 15 岁的 李四 有钱 200 元，他学会的技能是：python





# lianxi :
# 1.修改原学生信息管理程序，原学生数据用字典保存 现改为Student 对象来保存
# 要求：
#     定义一个Student 类，此类卸载
#     student.py模块中




















