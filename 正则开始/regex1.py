import re


pattern = r"\d+"
s = "2018年你过年了吗6.6月，2017年基本持平，2019面许多难题"


it = re.finditer(pattern,s)

#match对象属性
# print(dir(next(it)))


for x in it:
    print(x.group())

try:
    obj = re.fullmatch(r"\w+","hello1973")
    print(obj.group())
except AttributeError as e:
    print(e)


obj = re.match(r"[A-Z]\w","Hello world")
print(obj.group())

sear = re.search(r"\d+",s)

print(sear.group())






