# -*- encoding: utf-8 -*-

"""
2.1.6十组最常用的内置函数
"""

print(sum([3,4,5])) # 求和函数
print(min(3,4,5), max(3,4,5)) # min()/max()可以接受多个参数
print(min([3,4,5]), max((3,4,5))) # min()/max()也可以接受列表或元组做参数
print(abs(-3.14)) # 绝对值函数
print(pow(2,3)) # 计算2的3次方
print(pow(2,1/2)) # 开平方
print(divmod(5,2)) # 以元组形式返回5/2的商和余数。某些场合用起来非常高效、优雅
print(round(3.1415926)) # 取整
print(round(3.1415926,5)) # 精确到小数点后5位
