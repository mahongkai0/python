# 练习
#     1.将没有性别域的文档删除
#     2.给所有的文档增加一个域

#     分数取值范围为 60--100

#     score:{'Chinese':xx,'math':xx,'Enhlish':xx}
#     3.聚合操作 查看所有女生的英语成绩排序 不显示_id 项
from pymongo import MongoClient
from random import randint
conn = MongoClient('localhost',27017)

db = conn.hha

myset = db.class0

myset.delete_many({'gender':{'$exists':False}})

cursor = myset.find()
for i in cursor:
    myset.update({'_id':i['_id']},{'$set':{'score':{'Chinese':randint(60,100),\
        'math':randint(60,100),'English':randint(60,100)}}})


l = [{'$match':{'gender':'w'}},
    {"$sort":{'score.english':-1}},
    {"$project":{"_id":0}}]

cursor = myset.aggregate(l)
for i in cursor:
    print(i)



