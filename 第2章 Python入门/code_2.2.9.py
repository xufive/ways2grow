# -*- encoding: utf-8 -*-

"""
2.2.9 装饰器
"""

import time

def timer(func): # 定义装饰器timer，func是被装饰的函数
    def wrapper(*args, **kwds):
        t0 = time.time()
        func(*args, **kwds)
        t1 = time.time()
        print('耗时%0.3f秒'%(t1-t0,))
    return wrapper

@timer
def do_something(delay):
    print('函数do_something开始')
    time.sleep(delay)
    print('函数do_something结束')

if __name__ == '__main__':	
    do_something(3)
