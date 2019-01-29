
import os
pid = os.fork()

if pid < 0:
    print("Create process error")
elif pid == 0:
    print("New process")
else:
    print("The old process")
print("fork test end...")

##### 4  号print 打印两边    123中选两个打引  

# 作业：把要求的问题自己描述整洁
# 网络编程程序过一遍
# 程序类
# 计算机原理 数据结构  算法讨论
# tcp图解






















































