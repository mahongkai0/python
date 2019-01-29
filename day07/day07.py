

# 1 ·9 的平方元组
# t= tuple(x ** 2 for x in range(1,10))
# print(t)


# t = ()
# for x in range(1,10):
#     t += (x ** 2,)
# print(t)


# 练习
# （1）写程序  将如下信息形成一个字典 seasons
# 键       值
# # 1        春季有123月
# # 2        夏季有456月
# # 3        秋季有789月
# # 4        冬季有101112月

#      （2）.
# 让用户输入一个整数代表这个季度 打印出这个季度的信息
# 如果用户输入的信息不在字典内  则打印信息不存在




# seasons = {}
# seasons[1] = '春季有1，2，3月'
# seasons[2] = '夏季有4，5，6月'
# seasons[3] = '秋季有7，8，9月'
# seasons[4] = '冬季有10，11，12月'
# print(seasons)

# seasons = {
    
# 1:'春季有1，2，3月',
# 2:'夏季有4，5，6月',
# 3:'秋季有7，8，9月',
# 4:'冬季有10，11，12月'
# ,}



# s =int(input("ddd:"))
# if s  in seasons:
#     print(seasons[s])
# else:
#     print("bu cunzai ")


# # s = int(input("请输入一个整数代表这个季度： "))
# # if s not in range(1,4):
#     print("信息不存在")

# else:
# #     print(seasons[s]) 
    

# d = dict(input("请输入一段字符串啊亲：："))
# s = {}

# for key in d:


# print(key ,':', "次")


# s = input("请输入： ")
# d = {}
# for ch in s:
  
#     d[ch] = s.count(ch)
# for t in d.items():
#     print("%s: %d 次" % t)
# # print(d)




# s = input("请输入： ")
# d = {}
# for ch in s:
#     if ch in d:         #说明ch这个字符已经出现过
#         d[ch] += 1
#     else:             #ch这个字符是第一次出现
#         d[ch] = 1




# 写一个程序  输入一些单词和解释    将单词作为键 解释作为值存在于字典中    当输入单词为空时结束输入

# 然后进入查询单词  （死循环）
# 输入单词 如果单词在字典中 则显示内容单词不存在  则提示”没有此单词“



# words = {}
# while True:
#     q = input("请输入单词: ")
#     if q =='':
#         break

#     trans = input("请输入解释: ")
#     words[q] = trans
# print(words)

# while True:
#     w = input("请输入要查询的单词：")
#     if w in words:
#         print('解释',words[w])
#     else:
#         print("meiyou")


# # 练习
# # # 有如下字符串列表
# L= ['tarena','xiaozhang','hello']
#上变下
# # d = {x : len(x) for x L}



# d = {}
# for x in L:
#     if x not in d:
#         print({x ,len(x)})


  

# list1 = [1001,1003,1008]
# list2 = ['Tom','jerry','spike']
# 用list2 中的元素作为键  用list1中的元素作为值 生成如下
# 字典

# d = {'Tom',1001,'jerry'1003,'spike',1008]}


# d = {}
# for i in range(3):   ##################3  and  len(list1)
#     d[list2[i]] = list1[i]
# print(d)


# d = {}
# for k in list2:
#     d[k] = list1[list2.index[k]]    
# print(d)



# d = {list2[i]:list1[i] for i in range(len(list1))}




# d = {k:list1{list2.index[k]} for k in list2}
# print(d)




# 有一只小猴子 摘了很多桃子
# 第一天吃了一半  感觉不饱又吃了一个
# 第二天吃了剩下的一半   感觉不报又吃了一个
# 一次类推
# 到 第十天   只剩一个   第一天摘了多少桃子
# s = 1
# n = 4

# while s <= 8:
#     n = n * 2 + 2

#     s +=1
# print(n)




# 2.实现一个带有菜单界面的字典程序
# 菜单如下：
# 1.添加单词
# 2.删除单词
# 3.查找单词
# 4.q退出

# # 示意见：

# d = {}
# while True:
#     print()
#     print()
#     print()
#     print()
#     s = input(qingexuanz)
# if s == 1:

#     pass
#     做添加单词的操作
# elif:
#     s == 2:
#     pass
# elif s == 3:
#     pass
# elif s == q

# x = 1
# d = {}
# while True:
#     print("1.添加单词")
#     print("2.删除单词")
#     print("3.查找单词")
#     print("4.退出")

#     s = int(input("请您输入编号："))
#     if s == 1:
        
#         while True:
            
#             a =input("请您添加单词： ")
#             if a in d:
#                 print("您添加的单词已经存在，添加失败了")
            
            
#             else:
#                 d[x] = a
#                 print("您所添加单词成功，为您显示界面：",d)

#             if a == "":
#                 break
#             x += 1
            
       
#     if s == 2:
#         print(d)
#         shanchu = int(input("您需要删除的单词编号是："))
#         d.pop(shanchu)
#         print("删除过后的界面为您展开： ",d)
#     if s == 3:
#         print(d)
#         chazhao = int(input("您需要查找的单词是："))
#         print(d[chazhao]) 
#         wan=int(input("回复1为查完退出，2为继续： "))    
#         if wan == 1:
#             break 

#     if s == 4:
#         break


















# 3.项目的开始  （学生信息管理   程序）
# 输入任意一个学生的信息  ，形成字典后存入列表
# 学生信息有  姓名 年龄 成绩
# 如：
# 请输入姓名：tarena
# 请输入年龄：15
# 请输入成绩：99
# 请输入姓名：name2
# 请输入年龄：20
# 请输入成绩：80
# 请输入姓名：<回车> 结束输入
# 形成内部存储格式如下
# [{'name':'tarena','age':15,'score':99},
# {'name':'name','age':20,'score':80}]

# #以表格方式打印上述表格的内容：
# +-----------------------+
# | 姓名  |  年龄|  成绩   |          
# +-------+-----+---------+
# |tarena |  15 |  99     |            
# | name  |  20 |  80     |
# # +-----------------------+

infors = []
def biao():
    while True:
        n_name = input("请输入学生姓名：")
        if n_name == "":
            break
        a_age = int(input("请输入学生年龄："))
        s_score = int(input("请输入学生成绩："))
        d = {}
        d["name"] = n_name
        d["age"] = a_age
        d["score"] = s_score
        infors.append(d)
    return infors
print(biao())
def dayin():
    print ("+" + "-" * 10 + "+" + "-" * 10 + "+" + "-" * 10 + "+")
    print ("|" + "姓名".center(8) + "|" + "年龄".center(8) + "|" + "成绩".center(8) + "|")
    print ("+" + "-" * 10 + "+" + "-" * 10 + "+" + "-" * 10 + "+")
    for n in infors:
        sn_name = n["name"]
        sa_age = str(n["age"])      # 转为字符串，容易居中
        ss_score = str(n["score"])
        print("|%s|%s|%s|" % (sn_name.center(10),sa_age.center(10),ss_score.center(10)))
    print ("+" + "-" * 10 + "+" + "-" * 10 + "+" + "-" * 10 + "+")
dayin()




















