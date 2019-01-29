def read_info(ff):
    fr = open("info.txt",encoding="utf-8")
    while True:
        s = fr.readline()  # '张三 20 100\n'
        if not s:
            break
        s2 = s.rstrip()  # '张三 20 100' 去掉右边的空白字符?
        n, a, s = s2.split()  # ['张三', '20', '100']
        a = int(a)
        s = int(s)  # 转为整数
        L.append(dict(name=n, age=a, score=s))
    fr.close()
    return L

infos = read_info('info.txt')


# print(infos)

def print_info(infos):
    for d in infos:
        print(d['name'], '今年',
              d['age'], '岁,成绩是:',
              d['score'])


print_info(infos)