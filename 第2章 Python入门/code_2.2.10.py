# -*- encoding: utf-8 -*-

"""
2.2.10 闭包
"""

import math

def log_factory(n): # 定义一个闭包生成函数
    def log_n(x): # 生成闭包
        return math.log(x)/math.log(n) # 闭包中携带了环境参数n
    return log_n # 返回闭包

if __name__ == '__main__':	
    log5 = log_factory(5) # 用闭包生成器生成闭包
    log7 = log_factory(7) # 用闭包生成器生成闭包
    print(log5(25)) # 该闭包携带的自由量是5
    print(log7(49)) # 该闭包携带的自由量是7
