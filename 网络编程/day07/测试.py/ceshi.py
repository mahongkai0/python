




#计算密集型程序
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

#io密集型程序
def write():
    f = open('test','w')
    for i in range(120000):
        f.write('hello word\n')
    f.close()
def read():
    f = open('test','r')
    lines = f.readlines()
    f.close()

















