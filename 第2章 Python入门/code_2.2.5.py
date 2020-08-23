# -*- encoding: utf-8 -*-

"""
2.2.5 断言
"""

import time

def i_want_to_sleep(delay):
    assert(isinstance(delay, (int,float))), '函数参数必须为整数或浮点数'
    print('开始睡觉')
    time.sleep(delay)
    print('睡醒了')


if __name__ == '__main__':
    i_want_to_sleep(1.1)
    i_want_to_sleep(2)
    i_want_to_sleep('2') # 输入字符串类型的参数，程序抛出异常
