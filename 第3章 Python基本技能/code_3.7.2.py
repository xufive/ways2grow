# -*- encoding: utf-8 -*-

"""
3.7.2 sys模块
"""

import sys

def summation(x, y):
    try:
        x, y = float(x), float(y)
    except:
        print('非法参数')
        sys.exit(1)
    finally:
        print('即使异常终止，这一句仍会被执行')
        
    print('%f + %f = %f'%(x, y, x+y))
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('请在程序名后输入两个数值型参数，每个参数前都以空格分隔')
        sys.exit(1)
    print(sys.argv)
    summation(sys.argv[1], sys.argv[2])
