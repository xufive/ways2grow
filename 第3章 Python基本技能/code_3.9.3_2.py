# -*- coding: utf-8 -*-

"""
3.9.3 进程间通信——管道
"""

import time, random
import multiprocessing as mp

def sub_process_A(pipe):
    """A进程函数"""
    
    aim = random.randint(0, 127)
    pipe.send('我在闭区间[0,127]之间想好了一个数字，你猜是几？')
    print('A: 我在闭区间[0,127]之间想好了一个数字，你猜是几？')
    while True:
        guess = pipe.recv()
        time.sleep(0.5 + 0.5*random.random()) # 假装思考一会儿
        if guess == aim:
            pipe.send('恭喜你，猜中了！')
            print('A: 恭喜你，猜中了！')
            break
        elif guess < aim:
            pipe.send('猜小了')
            print('A: 不对，猜小了')
        else:
            pipe.send('猜大了')
            print('A: 不对，猜大了')

def sub_process_B(pipe):
    """B进程函数"""
    
    result = pipe.recv()
    n_min, n_max = 0, 127
    while True:
        time.sleep(0.5 + 2*random.random()) # 假装思考一会儿
        guess = n_min + (n_max-n_min)//2
        pipe.send(guess)
        print('B：我猜是%d'%guess)
        
        result = pipe.recv()
        if result == '恭喜你，猜中了！':
            print('B：哈哈，被我猜中！')
            break
        elif result == '猜小了':
            n_min, n_max = guess+1, n_max
        else:
            n_min, n_max = n_min, guess

if __name__ == '__main__':
    pipe_enda, pipe_endb = mp.Pipe() # 创建管道，返回管道的两个端，均可收发信息
    
    p_a = mp.Process(target=sub_process_A, args=(pipe_enda,))
    p_a.daemon = True
    p_a.start()
    
    p_b = mp.Process(target=sub_process_B, args=(pipe_endb,))
    p_b.daemon = True
    p_b.start()
        
    p_a.join() # 主进程等待p_a进程结束
    p_b.join() # 主进程等待p_b进程结束