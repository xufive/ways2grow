# -*- encoding: utf-8 -*-

"""
2.2.1 函数的参数
"""

def bmi_1(height, weight, name):
    i = weight/height**2
    print('%s的体重指数为%0.1f'%(name, i))

def bmi_2(height, weight, name='您'):
    i = weight/height**2
    print('%s的体重指数为%0.1f'%(name, i))

def bmi_3(height, weight, *args, name='您'):
    weight = (weight+sum(args))/(1+len(args))
    i = weight/height**2
    print('%s的体重指数为%0.1f'%(name, i))

def bmi_4(height, weight, *args, name='您', **kwds):
    weight = (weight+sum(args))/(1+len(args))
    i = weight/height**2
    print('%s的体重指数为%0.1f'%(name, i))
    for key in kwds:
        print('%s的%s是%s'%(name, key, str(kwds[key])))

if __name__ == '__main__':
    bmi_1(1.75, 75, 'Xufive')
    
    bmi_2(1.75, 75) # 可以不传递name参数，使用默认值
    bmi_2(1.75, 75, 'Xufive') # 也可以传递name参数
    
    bmi_3(1.75, 75, name='xufive')
    bmi_3(1.75, 75, 74)
    bmi_3(1.75, 75, 74, 75.5, 74.7)
    bmi_3(1.75, 75, 74, 75.5, 74.7, name='xufive')
    
    bmi_4(1.75, 75, 74, 75.5, 74.7, name='Xufive')
    bmi_4(1.75, 75, 74, name='Xufive', 性别='男', 爱好='摄影')
    bmi_4(1.75, 75, 74, 性别='男', 爱好='摄影', name='Xufive')
    bmi_4(1.75, 75, 74, 75.5, 74.7, 性别='男', 爱好='摄影')

