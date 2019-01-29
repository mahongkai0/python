


from student import Student

def input_student():
    L = []   # 创建一个列表,准备放字典
    while True:
        try:
            n = input("请输入姓名: ")
            if n == '':  # if not n:
                break
            a = int(input("请输入年龄: "))
            s = int(input("请输入成绩: "))
        except (ValueError,TypeError):
            print("您输错了")
            import time
            time.sleep(2)
            continue  
        # d = {}  # 每次创建一个
        # d['name'] = n
        # d['age'] = a
        # d['score'] = s
        d =Student(n,a,s)
        L.append(d)
    return L

def output_student(L):
    print("+---------------+----------+----------+")
    print("|    姓名       |   年龄   |   成绩   |")
    print("+---------------+----------+----------+")
    for d in L:
        # sn = d['name']
        # sa = str(d['age'])  # 转为字符串,容易居中
        # ss = str(d['score'])
        sn,sa,ss = d.get_infos()
        
        print("|%s|%s|%s|" % (sn.center(15),
                            sa.center(10),
                            ss.center(10)))
    print("+---------------+----------+----------+")

def remove_student(L):
    name = input("请输入要删除学生的姓名: ")
    # 方法1
    # for d in L:
    #     if d['name'] == name:
    #         L.remove(d)
    #         print("删除成功")
    #         return
    for i in range(len(L)):  # i代表列表的索引
        d = L[i]
        if d.get_name() == name:
            del L[i]
            print("删除成功")
            return
    print("删除失败")

def modify_student(L):
    name = input("请输入要修改成绩的学生姓名: ")
    for d in L:
        if d.get_name() == name:
            try:
                score = int(input("请输入学生成绩:"))
                d.set_score(score)
                print("修改成功!")
                return
            except ValueError:
                print("修改失败！")
                return
    print("修改失败")

def read_from_file(filename='si.txt'):
    '''读取filenamem 内容,形成字典的列表返回 
    返回: [
          {'name': '张三', 'age': 20, 'score': 100},
          {'name': '李四', 'age': 21, 'score': 96},
          {'name': '小王', 'age': 22, 'score': 98},
          ]
    '''
   
    L=[]
    fr = open(filename,encoding = "utf-8")
    text=fr.readlines()
    for x in text:
        x=x.rstrip()
        l=x.split(' ')
        L.append(dict(name=l[0],age=l[1],score=l[2]))
    print("读取数据成功")
    return L
# def save_to_file(L):
#     try:
#         fw = open("si.txt", 'w')
#         for d in L:
#             print(d['name'], d['age'], d['score'],
#                   file=fw)
#         fw.close()
#         print("保存成功")
#     except OSError:
#         print("保存失败!")


def save_to_file(L):
    try:
        fw = open('sit.txt','w')
        for x in L:
            print(x["name"],x['age'],x['score'],file = fw)
        fw.close()
        print("保存成功")
    except EOFError:
        print("保存失败")
    



