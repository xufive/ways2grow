# -*- encoding: utf-8 -*-

"""
3.4.2 使用MySQL数据库
"""

import pymysql
import MySQLdb.cursors

# 需要数据库服务支持
db = pymysql.connect(host='localhost', port=3306, user='xufive', password='********', db='demo', charset='utf8')
cursor = db.cursor()
cursor.execute('select * from member where id = %s', (100,))
print(cursor.fetchall())
cursor.close()
db.close()

# 需要数据库服务支持
db = MySQLdb.connect(host='localhost', port=3306, user='xufive', password='********', db='demo', charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
cursor = db.cursor()
cursor.execute('select * from member where id = %s', (100,))
print(cursor.fetchall())
cursor.close()

# MySQL事务回滚应函数
def transaction(db):
    try:
        db.begin()
        # 此处加入出错之后需要回滚的DML(insert、update、delete)语句
        db.commit()
        return True
    except:
        db.rollback()
        return False
