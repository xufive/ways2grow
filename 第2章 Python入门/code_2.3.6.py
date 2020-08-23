# -*- encoding: utf-8 -*-

"""
2.3.6 单实例模式
"""

def Singleton(cls): # 定义单实例模式装饰器
    _instance = {}
    
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
	
    return _singleton

@Singleton
class Config(object): # 定义单实例类
    pass

cfg1 = Config() # 实例化
cfg2 = Config() # 实例化
print(cfg1 is cfg2) # 两次实例化得到的实例是同一个对象
