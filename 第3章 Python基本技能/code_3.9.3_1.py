# -*- coding: utf-8 -*-

"""
3.9.3 进程间通信——队列
"""

import os, time, random
import multiprocessing as mp

def sub_process_A(q):
    """A进程函数：生成数据"""
    
    while True:
        time.sleep(5*random.random()) # 在0-5秒之间随机延时
        q.put(random.randint(10,100)) # 随机生成[10,100]之间的整数

def sub_process_B(q):
    """B进程函数：使用数据"""
    
    words = ['哈哈，', '天哪！', 'My God！', '咦，天上掉馅饼了？']
    while True:
        print('%s捡到了%d块钱！'%(words[random.randint(0,3)], q.get()))

if __name__ == '__main__':
    print('主进程（%s）开始，按回车键结束本程序'%os.getpid())
    
    q = mp.Queue(10)
    
    p_a = mp.Process(target=sub_process_A, args=(q,))
    p_a.daemon = True
    p_a.start()
    
    p_b = mp.Process(target=sub_process_B, args=(q,))
    p_b.daemon = True
    p_b.start()
        
    input()