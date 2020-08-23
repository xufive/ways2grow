# -*- encoding: utf8 -*-

"""
3.8.3 线程同步——信号量Semaphore
"""

import time
import threading

S = threading.Semaphore(5) # 有5把电锤可供使用

def us_hammer(id):
    """线程函数"""
    
    S.acquire() # P操作，阻塞式请求电锤，
    time.sleep(0.2)
    print('%d号刚刚用完电锤'%id)
    S.release() # V操作，释放资源（信号量加1）

def demo():
    threads = list()
    for i in range(30): # 有30名工人要求使用电锤
        threads.append(threading.Thread(target=us_hammer, args=(i,)))
        threads[-1].start()
    
    for t in threads:
        t.join()
    
    print('所有线程工作结束')

if __name__ == '__main__':
    demo()