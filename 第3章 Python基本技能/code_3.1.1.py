# -*- encoding: utf-8 -*-

"""
3.1.1 time模块
"""

import time

# 1. 最典型应用：获取时间戳和休眠
# ------------------------------

def do_something():
    t0 = time.time() # 记录开始时间戳
    for i in range(5):
        print('我正在努力工作中...')
        time.sleep(0.3)
    t1 = time.time() # 记录结束时间戳
    print('工作结束，耗时%0.3f秒。'%(t1-t0)) # 显示时长
	
do_something()

# 2. 时间戳和struct_time类互转
# ------------------------------

print(time.localtime()) # 获取本地时区的时间，返回struct_time类
print(time.gmtime()) # 获取格林尼治时间，返回struct_time类
print(time.localtime(0)) # 0时间戳，对应东八区，是1970年1月1日8时
print(time.gmtime(0)) # 0时间戳，对应格林尼治零时区，是1970年1月1日0时
print(time.localtime(1586000000.0)) # 时间戳转struct_time类
print(time.mktime(time.localtime())) # struct_time 类转时间戳

# 3. 时间戳和日期时间字符串互转
# ------------------------------

print(time.strftime('%Y-%m-%d %H:%M:%S')) # 将当前日期时间格式化
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1585800000.0))) 
print(time.mktime(time.strptime('2019-10-28 08:00:00', '%Y-%m-%d %X')))
