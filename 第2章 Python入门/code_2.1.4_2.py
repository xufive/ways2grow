# -*- encoding: utf-8 -*-

"""
2.1.4 四种数据类型——整型、浮点型、布尔型、字符串
"""

def factorial(n):
    """阶乘函数"""
    
    if n == 0:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    result = factorial(100) # 计算100的阶乘
    print(result)
