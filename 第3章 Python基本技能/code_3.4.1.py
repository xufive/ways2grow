# -*- encoding: utf-8 -*-

"""
3.4.1 使用SQLite数据库
"""

import sqlite3

class Sqlite3Client:
    """读取sqllite数据库的客户端类"""
    
    def __init__(self, db_file):
        """构造函数"""

        self._conn = sqlite3.connect(db_file)

    def create_table(self, sql):
        """创建数据表"""
        
        self.execute(sql)
        self._conn.commit()

    def execute(self, sql, args=()):
        """运行SQ语句"""
        
        cursor = self._conn.cursor()
        if isinstance(args, list): # 批量执行SQL语句
            cursor.executemany(sql, args)
        else: # 单次执行SQL语句，此时parameter是tuple或者None
            cursor.execute(sql, args)
        
        if sql.split()[0].upper() != 'SELECT':  # 非select语句
            self._conn.commit()
        
        result = cursor.fetchall()
        cursor.close()
        
        return result

    def close(self):
        """关闭数据库连接"""

        self._conn.close()

if __name__ == '__main__':
    sql_table = '''CREATE TABLE spring(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        btq REAL,
        hhq REAL
    )'''
    
    db = Sqlite3Client(r'..\res\water.db') 
    db.create_table(sql_table)
    
    sql = 'insert into spring (date, btq, hhq) values(?,?,?)'
    db.execute(sql, ('2019-05-31', 27.58, 27.56))
    
    sql = 'select * from spring where date = ?'
    result = db.execute(sql, ('2019-05-31',))
    print(result)
