# -*- encoding: utf-8 -*-

"""
2.3.5 抽象类
"""

import abc

class A(object, metaclass=abc.ABCMeta): # 定义抽象类，定义了两个成员函数
    @abc.abstractmethod
    def f1(self):
        pass
    
    @abc.abstractmethod
    def f2(self):
        pass
	
class B(A): # 继承抽象类，重写了两个成员函数
    def f1(self):
        print('重写f1')
    
    def f2(self):
        print('重写f2')
		
class C(A): # 继承抽象类，只重写了一个成员函数
    def f1(self):
        print('重写f1')
		
b = B() # B类重写了两个成员函数
c = C() # C类只重写了一个成员函数，没有遵守规则，将会抛出异常
