
###########myclass.py


##定义一个类， 此类用来描写狗的行为和属性
# class Dog:
#     '''此类用来描述动物的行为
#     和属性'''
#     def eat(self,food):
#         print("id为",id(self),"的小狗正在吃",food)
#     def sleep(self,hour):
#         print("小狗睡了",hour,'小时')
        
#     def play(self,ball):
#         print("小狗玩了",ball,'球')
# dog1 = Dog()  # 用dog类来创建一个Dog类型的对象d
# #####Dog.eat(dog1,'大海')
# dog1.sleep('1')
# dog1.play("大")



# dog2 = Dog()   # 用构造函数来创建另一个Dog类型的对象
# dog2.eat("面包")
# # print(id(dog2))




# lst1 = list()   #用；list类来创建一个列表对象
# lst1.append(10)
# lst2 = list()  ##创建另一个列表对象

##————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ##### attribute.py
# class Dog:
#     def eat(self,food):
#         print(self.color,'的',self.kinds,"正在吃",food)
#         self.last_food = food   # 让每次吃食物的狗来记住吃的是什么
#     def food_info(self):
#         print(self.color,'的',self.kinds,'上次吃的是',self.last_food)

# dog1 = Dog()
# dog1.color = '白色' #为dog1对象添加color属性 绑定白色
# dog1.kinds = '二哈' 
# dog1.eat("大树")

# dog2 = Dog()
# dog2.color = '灰色'
# dog2.kinds = '哈士奇'
# dog2.eat('狗粮')  ###       把这句放在下面函数调用语句下面会报错
# # print(dog1.color,'的',dog1.kinds)

# dog1.food_info() #显示dog1上次吃的是什么
# dog2.food_info()

##_______________________________________________________________________________________________________________
##init_method.py
# class Car:
#     '''此类定义一个小汽车的类'''
#     def __init__(self,c,b,m):
#         self.color = c
#         self.brand = b
#         self.model = m
#         print("__init__方法被调用！！！")
#     def run(self,speed):
#         print(self.color,self.brand,"小汽车",self.model,"正在以",speed,'公里/小时的速度行驶')

# a4 = Car('红色','奥迪','A4')
# a4.run(199)

# t1 = Car('蓝色','宝马','xs')
# t1.run(300)
# t1.__init__('白色','Tesla','model x')
# t1.run(300000)

# Car('红色','奥迪','A4').run(188) ###  创建 

##_________________________________________________________________________________________________
###3del_method.py


# class Car:
#     def __init__(self,info):
#         self.info =info
#         print("汽车",info,'对象被创建！')
#         #self.file = open("xxx.py")
#     def __del__(self):

#         print("汽车:",self.info,'对象将被销毁')
#         #self.file.close()
# c1 = Car("BYD E6")
# ####del c1   手动销毁  and  c1 = None
# input("请输入回车键继续")
# print("程序正常退出")


































