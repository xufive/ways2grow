# -*- encoding: utf-8 -*-

"""
2.3.4 面向对象三要素
"""

class H2O:
    def who(self):
        print("I'm H2O")
		
class Water(H2O):
    def who(self):
        print("I'm water")
		
class Ice(H2O):
    def who(self):
        print("I'm ice")
		
class Vapor(H2O):
    def who(self):
        print("I'm vapor")
		
def who(obj):
    obj.who()
	
objs = [H2O(), Water(), Ice(), Vapor()]
for obj in objs:
    who(obj)

