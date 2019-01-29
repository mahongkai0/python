# width = 6
# height = 4
# l = (width + height) * 2
# print("周长为",l)
# s = width * height
# print("面积为",ｓ)


from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db=conn.hha

#创建集合对象
myset = db.class0

# #c操作数据
# print(dir(myset))
# myset.insert_one({'name':'居里','king':'伟人'})
# myset.insert_many([{'name':'罗大佑','king':'歌手'},{"name":'苏有朋','king':'张无忌'}])
# myset.insert({'name':'成龙','king':'演员'})
####    myset.save({'_id':1,'name':'郑少秋','king':'乾隆'})
####   myset.save({'_id':1,'name':'吴奇隆','king':'乾隆'})替换掉

#查找操作
# cursor = myset.find({},{'_id':0})

# #获取游标对象
cursor = myset.find({'name':{'$exists':True}},{'_id':0})


# print(cursor)
# for x in cursor:
#     print(x)



# print(cursor.next())#获取下一个文档　　　根for冲突　因为游标不是完整的　　它已经向后移动了
# for i in cursor.skip(1).limit(3):
#     print(i)



#注意　排序写法同mongo shell　不同　用元祖表达式
# for i in cursor.sort([('age',1)]):
#     print(i)





# dic = {'$or':[{'king':'乾隆'},{'name':'林丹'}]}
# d = myset.find_one(dic)
# print(d)







#修改操作
# myset.update_one({'king':'演员'},{'$set':{'king_name':'玄晔'}},upsert =True)

# myset.update_many({'king':'乾隆'},{'$set':{'king_name':"弘历"}})



#删除操作
# myset.delete_one({'king':'伟人'})
# myset.delete_many({'age':{'$exists':False}})
# print(myset.find_one_and_delete({'name':'Emma'})) #找到并删掉

#关闭连接

conn.close()


