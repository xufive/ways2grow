# -*- coding: utf-8 -*-

"""
3.8.3 线程同步——队列Queue
"""

import os, time, random
import queue
import threading

def sub_thread_A(q):
    """A线程函数：生成数据"""
    
    while True:
        time.sleep(5*random.random()) # 在0-5秒之间随机延时
        q.put(random.randint(10,100)) # 随机生成[10,100]之间的整数

def sub_thread_B(q):
    """B线程函数：使用数据"""
    
    words = ['哈哈，', '天哪！', 'My God！', '咦，天上掉馅饼了？']
    while True:
        print('%s捡到了%d块钱！'%(words[random.randint(0,3)], q.get()))

if __name__ == '__main__':
    print('线程（%s）开始，按回车键结束本程序'%os.getpid())
    
    q = queue.Queue(10)
    
    A = threading.Thread(target=sub_thread_A, args=(q,))
    A.setDaemon(True)
    A.start()
    
    B = threading.Thread(target=sub_thread_B, args=(q,))
    B.setDaemon(True)
    B.start()
        
    input()
