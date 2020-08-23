# -*- coding: utf-8 -*-

"""
3.9.3 进程间通信——互斥锁
"""

import time
import multiprocessing as mp

lock = mp.Lock() # 创建进程互斥锁
counter = mp.Value('i', 0) # 使用共享内存做计数器

def hello(lock, counter):
    """进程函数"""
    
    if lock.acquire(): # 请求互斥锁，如果被占用，则阻塞，直至获取到锁
        time.sleep(0.2) # 假装思考、敲键盘需要0.2秒钟
        counter.value += 1
        print('我是第%d个'%counter.value)
    
    lock.release() # 千万不要忘记释放互斥锁，否则后果很严重

def demo():
    p_list= list()
    for i in range(30): # 假设群里有30人，都喜欢使用PyCharm
        p_list.append(mp.Process(target=hello, args=(lock, counter)))
        p_list[-1].start()
    
    for t in p_list:
        t.join()
    
    print('统计完毕，共有%d人'%counter.value)

if __name__ == '__main__':
    demo()