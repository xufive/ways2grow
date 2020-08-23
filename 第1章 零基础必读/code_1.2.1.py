# -*- encoding: utf-8 -*-

"""
1.2.1 使用Python IDLE交互操作

本脚本文件是将IDLE交互操作的每一行语句合并在一起连续执行。
运行前，需要根据实际的数据库连接修改host/port/db/user/passwd等参数
请仔细体会交互操作和运行脚本文件的差异。
"""

import pymysql
import pymysql.cursors as cursors

db = pymysql.connect(host='localhost', port=3306, db='photo', user='xufive', passwd='123')
cursor = db.cursor()
cursor.execute('select * from album')
result = cursor.fetchall()
print(result)
db.close()
