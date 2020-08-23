# -*- coding: utf-8 -*-

"""
3.9.3 进程间通信——事件
"""

import time
import multiprocessing as mp

E = mp.Event() # 创建事件

def work(id, E):
    """进程函数"""
    
    print('<%d号员工>上班打卡'%id)
    if E.is_set(): # 已经到点了
        print('<%d号员工>迟到了'%id)
    else: # 还不到点
        print('<%d号员工>浏览新闻中...'%id)
        E.wait() # 等上班铃声
    
    print('<%d号员工>开始工作了...'%id)
    time.sleep(10) # 工作10秒后下班
    print('<%d号员工>下班了'%id)

def demo():
    E.clear() # 设置为“未到上班时间”
    threads = list()
    
    for i in range(3): # 3人提前来到公司打卡
        threads.append(mp.Process(target=work, args=(i, E)))
        threads[-1].start()
    
    time.sleep(5) # 5秒钟后上班时间到
    E.set()
    
    time.sleep(5) # 5秒钟后,大佬(9号)到
    threads.append(mp.Process(target=work, args=(9, E)))
    threads[-1].start()
    
    for t in threads:
        t.join()
    
    print('都下班了，关灯关门走人')

if __name__ == '__main__':
    demo()