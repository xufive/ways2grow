# -*- encoding: utf8 -*-

"""
3.8.3 线程同步——事件Event
"""

import time
import threading

E = threading.Event() # 创建事件

def work(id):
    """线程函数"""
    
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
        threads.append(threading.Thread(target=work, args=(i,)))
        threads[-1].start()
    
    time.sleep(5) # 5秒钟后上班时间到
    E.set()
    
    time.sleep(5) # 5秒钟后,大佬(9号)到
    threads.append(threading.Thread(target=work, args=(9,)))
    threads[-1].start()
    
    for t in threads:
        t.join()
    
    print('都下班了，关灯关门走人')

if __name__ == '__main__':
    demo()