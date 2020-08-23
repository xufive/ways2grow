# -*- coding: utf-8 -*-

"""
3.9.2 创建、启动和管理进程
"""

import os, time
import multiprocessing as mp

def sub_process(name, delay):
    """进程函数"""
    
    while True:
        time.sleep(delay)
        print('我是子进程%s，进程id为%s'%(name, os.getpid()))

if __name__ == '__main__':
    print('主进程（%s）开始，按任意键结束本程序'%os.getpid())
    
    p_a = mp.Process(target=sub_process, args=('A', 1))
    p_a.daemon = True  # 设置子进程为守护进程
    p_a.start()
    
    p_b = mp.Process(target=sub_process, args=('B', 2))
    p_b.daemon = True  # 如果子进程不是守护进程，主进程结束后子进程可能成为僵尸进程
    p_b.start()
        
    input() # 利用input函数阻塞主进程，按回车键结束。这是常用的调试手段
