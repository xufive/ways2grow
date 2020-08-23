# -*- encoding: utf-8 -*-

"""
3.8.4 线程池
"""

from concurrent.futures import ThreadPoolExecutor

def pow2(x):
    return x*x

with ThreadPoolExecutor(max_workers=4) as pool: # 4个线程的线程池
    result = pool.map(pow2, range(10)) # 使用4个线程分别计算0~9的平方

print(list(result)) # result是一个生成器，转成列表才可以直观地看到计算结果


def pow3(x): 
    return x*x*x

def save_result(task): # 保存线程计算结果
    global result
    result.append(task.result())

result = list()
with ThreadPoolExecutor(max_workers=3) as pool:
    for i in range(10):
        if i%2: # 奇数做平方运算
            task = pool.submit(pow2, i)
        else: # 偶数做立方运算
            task = pool.submit(pow3, i)
        task.add_done_callback(save_result) # 为每个线程指定结束后的回调函数
		
print(result)
