# -*- coding: utf-8 -*-

"""
3.9.3 进程间通信——条件
"""

import time
import multiprocessing as mp
import random

cond = mp.Condition() # 创建条件对象
draw = mp.Array('i', [0,0]) # [Seeker小朋友认输, Hider小朋友认输]

def seeker(cond, draw):
    """Seeker小朋友的进程函数"""
    
    global draw_Seeker, draw_Hidwer
    
    time.sleep(1) # 确保Hider小朋友已经进入消息等待状态
    cond.acquire() # 阻塞时请求资源
    time.sleep(random.random()) # 假装蒙眼需要花费时间
    print('Seeker: 我已经蒙上眼了')
    cond.notify() # 把消息通知到Hider小朋友
    cond.wait() # 释放资源并等待Hider小朋友已经藏好的消息
    
    print('Seeker: 我来了') # 收到Hider小朋友已经藏好的消息后
    cond.notify() # 把消息通知到Hider小朋友
    cond.release() # 不要再听消息了，彻底释放资源
    time.sleep(random.randint(3,10)) # Seeker小朋友的耐心只有3-10秒钟
    
    if draw[1]:
        print('Seeker: 哈哈，我找到你了，我赢了')
    else:
        draw[0] = True
        print('Seeker: 算了，我找不到你，我认输啦')

def hider(cond, draw):
    """Hider小朋友的进程函数"""
    
    global draw_Seeker, draw_Hidwer
    
    cond.acquire() # 阻塞时请求资源
    cond.wait() # 如果先于Seeker小朋友请求到资源，则立刻释放并等待
    time.sleep(random.random()) # 假装找地方躲藏需要花费时间
    print('Hider: 我藏好了，你来找我吧')
    cond.notify() # 把消息通知到Seeker小朋友
    cond.wait() # 释放资源并等待Seeker小朋友开始找人的消息
    
    cond.release() # 不要再听消息了，彻底释放资源
    time.sleep(random.randint(3,10)) # Hider小朋友的耐心只有3-10秒钟
    
    if draw[0]:
        print('Hider: 哈哈，你没找到我，我赢了')
    else:
        draw[1] = True
        print('Hider: 算了，这里太闷了，我认输，自己出来吧')

def demo():
    p_seeker = mp.Process(target=seeker, args=(cond, draw))
    p_hider = mp.Process(target=hider, args=(cond, draw))
    p_seeker.start()
    p_hider.start()
    
    p_seeker.join()
    p_hider.join()

if __name__ == '__main__':
    demo()