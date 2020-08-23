# -*- encoding: utf-8 -*-

"""
3.4.3 使用MongoDB数据库
"""

import pymongo

conn = pymongo.MongoClient('localhost', 27017) # 连接MongDB
conn.list_database_names() # 列出所有的库：['admin', 'config', 'local']
db = conn['demo'] # 选中demo库，若不存在，则新建

db.create_collection('roster') # 创建集合
db.roster. insert_one({'name':'Irene', 'math':95}) # 插入文档
db.roster. insert_one({'name':'Jack', 'age':18}) # 插入文档

for doc in db.roster.find(): # 查询全部文档
    print(doc)
    
for doc in db.roster.find({'name':'Irene'}, {'math':1}): # 条件查询
    print(doc)
	
db.roster.update_one({'name':'Irene'}, {'$set':{'math':99}}) # 修改文档
db.roster.delete_one({'name':'Irene'}) # 删除文档
db.list_collection_names() # 列出当前库的所有集合：['roster']

db.drop_collection('roster') # 删除集合
conn.drop_database('demo') # 删除库
conn.close() # 关闭连接
