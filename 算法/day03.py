



# def cha():
#     for x in range(len(l)):
#         if l[x]>l[x+1]:
#             l[x],l[x+1] =l[x+1],l[x]
           
# cha()
# # print(l)

# def insert(l):
#     #外部循环 对应遍历所有无序数据 依次取出元素插入有序部分\
#     #从第一个无需数据开始  下标为1
#     #到最后一个位置 len(l)
#     for i in range(1,len(l)):
#         #内部循环 对应从后向前扫描有序数据 找出取出元素的插入位置
#         #从当前无序数据（i）的前一个位置开始扫描 i-1
#         #直到遍历完下标为0时 
#         #要求从后向前扫描
#         #获取当前无序位置
#         temp = l[i]
#         #存放该数据的位置
#         pos = i
#         for j in range(i-1,-1,-1):
#             if l[j] >temp:
#                 #若有序数据大于取出数据
#                 #则该有序数据后移
#                 l[j+1] =l[j]
#                 #更新插入取出数据的位置
#                 #对应遍历完所有数据首部插入元素的位置
#                 pos = j 
#             else:
#                 #若有序数据小于等于取出数据
#                 #则在该有序数据后插入取出数据
#                 #即找到插入位置
#                 pos = j+1
#                 break

#             l[pos] = temp

# if __name__ == "__main__":
#     l = [80,35,12,50,541,100,52,611,18,50]
#     print("排序前：",l)
#     insert(l)
#     print('排序后',l)


def quick(l):
    #递归退出条件
    if len(l)<2:
        return l
    
    #sehzhi 关键数据
    mark = l[0]
    #z找出所有小于关键数据的
    #找出所有大于关键数据的
    #zhaochu 和你关键数据相等的
    small = [x for x in l if x < mark]
    equal = [x for x in l if x == mark]
    big = [x for x in l if x > mark]

    #从小到大排序
    return quick(small) + equal + quick(big)


if __name__ == "__main__":
    l = [80,35,12,50,541,100,52,611,18,50]
    print("排序前：",l)
    l = quick(l)
    print('排序后',l)


