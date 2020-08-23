# -*- coding: utf-8 -*-

"""
3.9.3 进程间通信——信号量
"""

import time
import multiprocessing as mp

S = mp.Semaphore(5) # 有5把电锤可供使用

def us_hammer(id, S):
    """进程函数"""
    
    S.acquire() # P操作，阻塞式请求电锤，
    time.sleep(0.2)
    print('%d号刚刚用完电锤'%id)
    S.release() # V操作，释放资源（信号量加1）

def demo():
    p_list = list()
    for i in range(30): # 有30名工人要求使用电锤
        p_list.append(mp.Process(target=us_hammer, args=(i, S)))
        p_list[-1].start()
    
    for t in p_list:
        t.join()
    
    print('所有进程工作结束')

if __name__ == '__main__':
    demo()