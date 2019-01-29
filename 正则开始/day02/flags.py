

import re
 
# re.I
# s = 'Hello word'
# pattern = r'hello'
# regex = re.compile(pattern,flags=re.I)

# l = regex.findall(s)
# print(l)




###############################################
# re.A   美式127 不包含汉字       

# s = 'Hello 你好'
# pattern = r'\w+'
# regex = re.compile(pattern,flags=re.A)
# l = regex.findall(s)
# print(l)


###############################################

#re.S  使点作用于\n
# s = '''Hello  world
# nihao CHina
# '''
# pattern = r'.+'
# regex = re.compile(pattern,flags=re.S)
# l = regex.findall(s)
# print(l)

###############################################



# #re.M  使其前面死行的字符串也可以被识别
# s = '''Hello  world
# nihao CHina
# '''
# pattern = r'^nihao'  # nihao前面是行 不是字符串
# regex = re.compile(pattern,flags=re.M)
# l = regex.findall(s)
# print(l)


###############################################
#re.X  给正则加注释  即里面加注释不影响你正则解析
s = '''abcdefhk'''

pattern = r'''(ab)  #第一行分组
\w+                #任意字符串
(?P<dog>ef)'''  # dog组
regex = re.compile(pattern,flags=(re.X|re.I))
l = regex.findall(s)
print(l)








