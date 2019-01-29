

# def liner(value = [3,9,8,2,1,5,4,6,10,7,13,12,11],key = 6):
#     for i in range(len(value)):
#         if value[i] == key:
#             return i
#         # else:
#         #     return liner
#     else:

#         return -1

# if __name__ == "__main__":
#     res = liner(value = [3,9,8,2,1,5,4,6,10,7,13,12,11],key = 6)
#     if res == -1:
#         print('NO')
#     else:
#         print('OK',res)


##############################################################二分
# if 9 > (13//2):
#     for x in range((13//2),13):
#         if x == 9:
#             print('OK')
#             print('dddddddd')
# else:
#     for x in range((13//2)):
#         if x == 9:
#             print(x)

#每次查找左侧下标值 left  右侧right




# def binaary(value,key,left,right):
#     if left > right:
#         #查找失败 返回1
#         return 1
#     middle = (left+right)//2
#     if value[middle] == key:
#         return  middle
#     elif value[middle] >key:
#         return binaary(value,key,left,middle-1)

#     else:
#         return binaary(value,key,middle+1,right)

# if __name__ == "__main__":
    
  
#     value = [1,2,3,4,5,6,4,7,8,9,10,11,12,13]
#     key = 9
#     res = binaary(value,key,0,len(value)-1)
#     if res == 1:
#         print("NO")
#     else:
#         print('成功',res)


#######################################################################
value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
key = 9
c = value[0] + value[12]
while True:
    
    if key > c:
        c += 1
    if key < c:
        c -= 1
    else:
        print(c)
        break
 

