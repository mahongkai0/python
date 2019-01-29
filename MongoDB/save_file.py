





from pymongo import MongoClient

import bson.binary

conn = MongoClient('localhost',27017)
db = conn.image
myset = db.boy

#读取图片
# with open ('tadelianxi/大鲨鱼.jpg','rb') as f:
#     data = f.read()

# #转换mongo格式
# content = bson.binary.Binary(data)
# #将内容插入集合
# doc = {'filename':'大鲨鱼.jpg','data':content}

# myset.insert_one(doc)


# 获取图片
img = myset.find_one({'filename':'大鲨鱼.jpg'})  #用find_one　返回字典

with open('boy.jpg','wb') as f:
    f.write(img['data'])





conn.close()
























