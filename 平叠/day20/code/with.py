

try:
    fr = open('c:/Users/Administrator/Desktop/test/平叠/day20/code/test.txt','r',encoding = 'UTF-8')
    try:
        for line in fr:
            print(line)
    finally:
        fr.close()
except OSError:
    print("失败了")

#将由下面的with改写


try:
    with open('c:/Users/Administrator/Desktop/test/平叠/day20/code/test.txt','r',encoding = 'UTF-8') as fr:


        for line in fr:
            print(line)
    #fr.read()   #出错  因为已经关闭

except OSError:
    print("失败了")





