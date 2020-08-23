# -*- encoding: utf-8 -*-

"""
2.1.2 两个顶级定义——函数和类
"""

def say_hello(): # 函数可以没有参数
    print('Hello')

def adder(x, y): # 函数有两个参数
    return x + y # 使用关键字return返回结果

if __name__ == '__main__':
    say_hello() # 调用函数say_hello
    result = adder(3, 4) # 调用函数adder
    print(result) # 打印返回的函数调用结果

