# -*- encoding: utf-8 -*-

"""
2.1.6十组最常用的内置函数
"""

import time

def printer(text, delay=0.2):
    """打字机效果"""
    
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def waiting(cycle=20, delay=0.1):
    """旋转式进度指示"""
    for i in range(cycle):
        for ch in ['-', '\\', '|', '/']:
            print('\b%s'%ch, end='', flush=True)
            time.sleep(delay)
    print()

def cover(cycle=100, delay=0.2):
    """覆盖式打印效果"""
    
    for i in range(cycle):
        s = '\r%d'%i
        print(s.ljust(3), end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    printer('玄铁重剑，是金庸小说笔下第一神剑，持之则无敌于天下。')
    waiting(cycle=20)
    cover(cycle=20)
