from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db=conn.hha

#创建集合对象
myset = db.class0

#c操作数据
            ##print(dir(myset))
# # #c操作数据
# print(dir(myset))
# myset.insert_one({'name':'居里','king':'伟人'})
# myset.insert_many([{'name':'罗大佑','king':'歌手'},{"name":'苏有朋','king':'张无忌'}])
# myset.insert({'name':'成龙','king':'演员'})
####    myset.save({'_id':1,'name':'郑少秋','king':'乾隆'})
####   myset.save({'_id':1,'name':'吴奇隆','king':'乾隆'})替换掉

#关闭连接

conn.cloe()


