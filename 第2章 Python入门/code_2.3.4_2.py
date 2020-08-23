# -*- encoding: utf-8 -*-

"""
2.3.4 面向对象三要素
"""

class A:
    def __init__(self, a, b, c):
        self.a = a # 公有属性
        self._b = b # 保护属性
        self.__c = c # 私有属性
    
    def x(self):
        print('公有方法')
    
    def _y(self): 
        print('保护方法')
    
    def __z(self):
        print('私有方法')
		
a = A(1, 2, 3)
print(a.a) # 访问公有属性
print(a._b) # 访问保护属性
#print(a.__c) # 访问私有属性，将会抛出异常

a.x() # 调用公有方法
a._y() # 调用保护方法
#a.__z() # 调用私有方法，将会抛出异常
