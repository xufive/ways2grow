# -*- coding: utf-8 -*-

"""
3.9.5 MapReduce模型
"""

import time
from functools import reduce
import multiprocessing as mp

def power(x, a=2):
    """进程函数：幂函数"""
    
    time.sleep(0.5) # 适量延时，模拟耗时的复杂计算
    return pow(x, a)

if __name__ == '__main__':
    mp.freeze_support()
    print('开始计算。。。')
    t0 = time.time()
    with mp.Pool(processes=4) as mpp:
        result_map = mpp.map(power, range(100))
        result = reduce(lambda result,x:result+x, result_map, 0)
        
    print('结果为%d，耗时%0.3f秒'%(result, time.time()-t0))