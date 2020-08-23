# -*- encoding: utf-8 -*-

"""
3.8.2 创建、启动和管理线程
"""

import time
import threading

def hello(name):
    """线程函数"""
    
    for i in range(5):
        time.sleep(1)
        print('Hello, 我是%s'%name)

def demo():
    A = threading.Thread(target=hello, args=('A',))
    B = threading.Thread(target=hello, args=('B',))
    
    #A.setDaemon(True)
    #B.setDaemon(True)
    
    A.start()
    B.start()
    
    B.join(3) # 监工B线程3秒
            
    print('线程A%s'%('还在工作中' if A.isAlive() else '已经结束工作',))
    print('线程B%s'%('还在工作中' if B.isAlive() else '已经结束工作',))
    print('下班了。。。')

if __name__ == '__main__':
    demo()
