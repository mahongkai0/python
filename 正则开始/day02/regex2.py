
import re

pattern = r"(ab)cd(?P<dog>ef)"
regex = re.compile(pattern)

#获取match对象

obj = regex.search('abcdefghijkhh',pos = 0,endpos = 8)

#obj属性遍历
print(obj.pos)  # 目标字符串的开始位置
print(obj.endpos)       #目标字符串的结束位置
print(obj.re)           #正则表达式
print(obj.string)   #目标字符串
print(obj.lastgroup)    #最后一组的名称 如果没有  就是None
print(obj.lastindex)    #最后一组的第几组

print("#" * 100)
print(obj.span())  #得到匹配内容的起止位置
print(obj.start())#得到匹配内容的开始位置
print(obj.end())    #得到匹配内容的结束位置



print(obj.group())    #整体匹配内容
print(obj.group(1))     #第一组
print(obj.group(2))     #第二组
print(obj.group('dog')) #dog组内容
print(obj.groupdict()) #获取捕获组子典
print(obj.groups()) #获取所有子组对应内容














