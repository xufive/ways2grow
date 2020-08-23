# -*- encoding: utf-8 -*-

"""
2.3.3 静态变量和实例变量
"""

class A:
    static_x = 10 # 静态变量
    
    def __init__(self):
        self.instance_y = 5 # 实例变量

a = A()
print(a.static_x) # 使用实例名a访问静态变量
print(a.instance_y) # 使用实例名a访问实例变量
print(A.static_x) # 使用类名A访问静态变量
print(A.instance_y) # 使用类名A访问实例变量，将会抛出异常
