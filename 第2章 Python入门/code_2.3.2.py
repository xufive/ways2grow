# -*- encoding: utf-8 -*-

"""
2.3.2 类的成员
"""

class A:
    pass

a = A()
del a
#print(a) # 此时对象a已被销毁，执行该语句将抛出异常

class B:
    def __del__(self):
        print('执行析构函数，清理现场')

		
b = B()
del b
#print(b) # 此时对象b已被销毁，执行该语句将抛出异常

class C:
    def __init__(self): # 定义构造函数
        self.a = 10 # 定义一个成员变量a
    def getA(self): # 定义成员函数
        print("a=%d" % self.a)

		
a = C() # 实例化
a.getA()
