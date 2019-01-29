

import re

f = open("c:/Users/Administrator/Desktop/test/正则开始/day02/day2.txt",'rb')
data=f.read().decode()

# pattern = r"[A-Z]+\S*"
# pattern = r"[A-Z]+[^\)\.\s]"

pattern = r"-?\d+\.?/?\d*%?"  #匹配数字


l = re.findall(pattern,data)
print(l)







