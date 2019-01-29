


from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db=conn.hha

#创建集合对象
myset = db['class0']



# index_name = myset.create_index('name')
# index_name = myset.create_index([('age',-1)],name='AGE')
# index_name = myset.create_index([('age',1)],name='GE')
# print(index_name)

#创建其他索引类型 稀疏
# myset.create_index([('name',1),('age',-1)],sparse=True)



# #查看索引
# for i in myset.list_indexes():
#     print(i)


# #删除索引
# # myset.drop_index('name_1')
# myset.drop_indexes()#删除所有

#聚合操作
l =[
    {'$group':{'_id':'$gender','num':{'$sum':1}}}
]

cursor = myset.aggregate(l)
for i in cursor:
    print(i)


conn.close()






