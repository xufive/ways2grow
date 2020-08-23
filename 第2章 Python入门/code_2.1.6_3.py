# -*- encoding: utf-8 -*-

"""
2.1.6十组最常用的内置函数
"""

nums = input('请输入3个整数，中间以空格分割，回车结束输入：')
print(nums) # 请注意，nums是一个字符串，不是整数
nums = [int(item) for item in nums.split()] # 这样才可以把输入的字符串变成3个整数
print(nums) # 此时nums是一个列表，其元素是整型数字

print(len('asdf34g')) # 返回字符串长度
print(len([3,4,5])) # 返回列表长度
print(len({'x':1, 'y':2})) # 返回字典长度
print(len({True, False, None})) # 返回集合长度
print(len(range(5))) # 返回range对象（迭代器）长度

print(type(range(5))) # <class 'range'>

for i in range(5): # 默认从0开始，步长为1
    print(i, end=',')

for i in range(5,10): # 在[5,10)区间内生成序列，步长为1
    print(i, end=',')

for i in range(5,10,2): # 在[5,10)区间内生成序列，步长为2
    print(i, end=',')

print(list(range(5))) # 将range类转成list类
