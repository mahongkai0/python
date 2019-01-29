from menu import *


def tianjia():
    L =[]
    while True:
        d = {}
        name = input("请输入学生姓名：")
        if name == '':
            break
        age = str(input("请输入学生年龄: "))
        score = str(input("请输入学生成绩: "))
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)

    return L


def shanchu(L):
    shanchu = input("请输入您所要删除的姓名名称：")
    if shanchu == '':
        return
    for x in range(len(L)):
        
        if shanchu == L[x]["name"]:
            del L[x]
            print("删除成功")
            return
        
        
    print("您输错了")


def xiugai(L):
    xiugai = input("请您输入要修改的姓名：")
    if xiugai == '':
        return
    else:
        xiuhou = input("请您输入修改后的成绩：")
        if xiuhou == '':
            return
        for x in range(len(L)):
            if L[x]["name"] == xiugai:
                L[x]["score"] = xiuhou
                return


def sore_di(x):
    return int(x['score'])


def show_info(L):
    li = sorted(L, key=sore_di)
    xianshi(li)


def sortgao(L):
    da = sorted(L, key=sore_di, reverse=True)
    xianshi(da)

def age_zheng(x):
    return int(x['age'])


def age_di(L):
    sss = sorted(L, key=age_zheng)
    xianshi(sss)

def age_gao(L):
    ssss = sorted(L, key=age_zheng, reverse=True)
    xianshi(ssss)




       

