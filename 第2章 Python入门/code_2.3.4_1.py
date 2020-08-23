# -*- encoding: utf-8 -*-

"""
2.3.4 面向对象三要素
"""

class Animal:
    def eat(self):
        print('我能吃东西')

class Fash(Animal): # 单继承
    def __init__(self, name):
        self.name = name
    
    def swim(self):
        print('我会游泳')
		
class Bird(Animal): # 单继承
    def __init__(self, name):
        self.name = name
    
    def who(self):
        print('我是%s'%self.name)
    
    def fly(self):
        print('我会飞')
		
class Batman(Bird): # 单继承，显式调用父类的构造函数
    def __init__(self, name, color):
        Bird.__init__(self, name)
        self.color = color
    
    def say(self):
        print('我会说话，喜欢%s'%self.color)
		
class Ultraman(Fash, Batman): # 多继承
    def __init__(self, name, color, region):
        super(Ultraman, self).__init__(name)
        super(Fash, self).__init__(name, color)
        self.region = region
    
    def where(self):
        print('我来自%s'%self.region)
		
uman = Ultraman('奥特曼', '红色', '火星')
uman.who() # 我是奥特曼
uman.where() # 我来自火星
uman.say() # 我会说话，喜欢红色
uman.eat() # 我能吃东西
uman.fly() # 我会飞
uman.swim() # 我会游泳
