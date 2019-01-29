



def bubble(l):
    for i in range(len(l) - 1):
        #内部循环：对应每次走访数据时 相邻数据对比次数
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    print('遍历次数',i+1)
if __name__ == '__main__':
    l = [165,155,153,166,142,148,162,158,160,800]
    print("排序前",l)
    bubble(l)
    print("排序后",l)





















