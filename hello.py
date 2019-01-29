# #! /usr/bin/python3
# print("hello world")
# print("你好")
# print("你好啊勇士")

# python3  解释执行器　　 被解释的文件
# import random
# print random.randint(1,100)

# weimz@tedu.cn
# aid1811  zhengzhou weimingze



# 5. 实现一个带有学生管理界面的学生信息管理程序
#  界面选择菜单如下
#  +---------------------------------------+
#  | 1) 添加学生信息                        |
#  | 2)显示学生信息                         |
#  | 3)删除学生信息                         |
#  | 4)修改学生成绩                         |              
#  | q)退出                                |
#  +---------------------------------------|
# 学生信息和存储方法与源程序相同  用列表里包含来存储信息
# 每个功能写一个函数相对应






print("你好")
print("你好啊勇士")
L =[]
def tianjia():

   
    while True:
        d ={}
        name = input("请输入学生姓名：")
        if name =='':
            break
        age = str(input("请输入学生年龄: "))
        score = str(input ("请输入学生成绩: "))
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
        # for x in range(len(L)):
        #     if name == d[x]['name']:
        #         print("您已经添加过了，请重新输入：")
        #         break   
        #     else:
        #         L.append(d)
       
    return L

def xianshi():
    print("+------+------+------+")
    print("| 姓名 | 年龄 |  成绩|")
    print("+------+------+------+")
    for x in range(len(L)):
        print("|" + L[x]['name'].center(6) +"|" + str(L[x]['age']).center(6) +"|"+ str(L[x]['score']).center(6) + '|')
    print("+------+------+------+") 

def shanchu():
    shanchu = input("请输入您所要删除的姓名名称：")
    if shanchu == '':
        return
    for x in range(len(L)):
        if shanchu == L[x]["name"]: 
            del L[x]
        else:
            print("您输错了亲")
            break

def xiugai():
    xiugai = input("请您输入要修改的姓名：")
    if xiugai == '':
        return
    else:
        xiuhou = input("请您输入修改后的名称：")
        if xiuhou == '':
            return
        for x in range(len(L)):
            if L[x]["name"] == xiugai:
                L[x]["score"] = xiuhou
                return
            
while True:

    print("+---------------------------------------+")
    print("| 1) 添加学生信息                        |")
    print("| 2)显示学生信息                         |")
    print("| 3)删除学生信息                         |")
    print("| 4)修改学生成绩                         |")             
    print("| q)退出                                |")
    print("+---------------------------------------|")           
    bianhao =str(input("请亲输入编号："))
    
    if bianhao == '1':
        tianjia()
    elif bianhao == '2':
        xianshi()

    elif bianhao == '3':
        shanchu()

    elif bianhao == '4':
        xiugai()
    elif bianhao == "q":
        break
    else:
        print("您输错了")

### for i in range(len(L)):
##    d = L[i]
#     if d['name'] = L[i]
#     d.remove(i)



























































