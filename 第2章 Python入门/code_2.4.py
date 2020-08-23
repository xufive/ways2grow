#!/usr/bin/env python
# -*- coding: utf-8 -*-  


"""通常这里是关于本文档的说明（docstring），须以半角的句号、 问号或惊叹号结尾!

本行之前应当空一行，继续完成关于本文档的说明
如果文档说明可以在一行内结束，结尾的三个双引号不需要换行；否则，就要像下面这样
"""


import os, time
import datetime


BASE_PATH = r"d:\YouthGit"
LOG_FILE = u"运行日志.txt"


class GameRoom(object):
    """对局室"""
    
    def __init__(self, name, limit=100, **kwds):
        """构造函数!
        
        name        对局室名字
        limit       人数上限
        kwds        参数字典
        """
        
        pass

  
def craete_and_start():
    """创建并启动对局室"""
    
    pass


if __name__ == '__main__':
    # 开启游戏服务
    craete_and_start()
