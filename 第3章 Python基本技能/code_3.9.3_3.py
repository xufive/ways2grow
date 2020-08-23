# -*- coding: utf-8 -*-

"""
3.9.3 进程间通信——共享内存
"""

import os, time
import multiprocessing as mp

def sub_process_A(flag, data):
    """A进程函数"""
    
    while True:
        if flag.value == 0: # 若标志为0
            time.sleep(1)
            for i in range(len(data)): # 共享数组各元素加2
                data[i] += 2
            flag.value = 1 # 置标志为1
            print([item for item in data])

def sub_process_B(flag, data):
    """B进程函数"""
    
    while True:
        if flag.value == 1: # 若标志为0
            time.sleep(1)
            for i in range(len(data)):
                data[i] -= 1 # 共享数组各元素减1
            flag.value = 0 # 置标志为0
            print([item for item in data])

if __name__ == '__main__':
    print('主进程（%s）开始，按回车键结束本程序'%os.getpid())
    
    flag = mp.Value('i', 0) # flag类型是ctypes.c_long，不是普通的int
    data = mp.Array('d', range(5))
    
    p_a = mp.Process(target=sub_process_A, args=(flag, data))
    p_a.daemon = True
    p_a.start()
    
    p_b = mp.Process(target=sub_process_B, args=(flag, data))
    p_b.daemon = True
    p_b.start()
        
    input()