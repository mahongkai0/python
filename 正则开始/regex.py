import re
pattern= r"(\w+:\d+)"
s = '张:2019,李:1995'

#直接用re 调用
# l = re.findall(pattern,s)
# print(l)
# ##只能获取子组内容




#compile对象来调用
regex = re.compile(pattern)
l = regex.findall(s,pos = 0,endpos = 10)
print(l)

l = re.split(r'\s+',"hello    word    hh")
print(l)

s = re.sub(r'\s+','##',"hello nihao kitt y",2)
print(s)


s = re.subn(r'\s+','##',"hello nihao kitt y",2)
print(s)









