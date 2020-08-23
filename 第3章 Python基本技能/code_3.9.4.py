# -*- coding: utf-8 -*-

"""
3.9.4 进程池
"""

import time
import multiprocessing as mp

def power(x, a=2):
    """进程函数：幂函数"""
    
    time.sleep(1)
    print('%d的%d次方等于%d'%(x, a, pow(x, a)))

def demo():
    mpp = mp.Pool(processes=4)
    
    for item in [2,3,4,5,6,7,8,9]:
        mpp.apply_async(power, (item, )) # 非阻塞提交新任务
        #mpp.apply(power, (item, )) # 阻塞提交新任务
    
    mpp.close() # 关闭进程池，意味着不再接受新的任务
    print('主进程走到这里，正在等待子进程结束')
    mpp.join() # 等待所有子进程结束
    print('程序结束')

if __name__ == '__main__':
    demo()