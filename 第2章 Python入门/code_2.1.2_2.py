# -*- encoding: utf-8 -*-

"""
2.1.2 两个顶级定义——函数和类
"""

class GameServer:
    """游戏服务器类"""
    
    def __init__(self, port):
        """构造函数"""
        
        self.port = port # 类属性：服务使用的端口
        self.running = False # 类属性：服务运行标志
    
    def start(self):
        """启动服务"""
        
        self.running = True
    
    def stop(self):
        """停止服务"""
        
        self.running = False
    
    def status(self):
        """查看服务状态"""
        
        if self.running:
            print('服务运行于%d端口上。'%self.port)
        else:
            print('服务已停止。')


if __name__ == '__main__':
    gs = GameServer(3721) # 类实例化，生成一个服务器对象
    print(gs.port) # 打印服务端口：3721
    gs.status() # 打印服务状态：服务已停止。
    gs.start() # 对象方法：启动服务
    gs.status() # 打印服务状态：服务运行于3721端口上。
    gs.stop() # 对象方法：停止服务
    gs.status() # 打印服务状态：服务已停止。

