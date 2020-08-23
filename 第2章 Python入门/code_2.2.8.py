# -*- encoding: utf-8 -*-

"""
2.2.8 迭代器和生成器
"""

it = iter([1,2])
print(next(it)) # 1
print(next(it)) # 2
#print(next(it)) # 此时迭代器已读完，抛出异常

def get_square(n):
    result = list()
    for i in range(n):
        result.append(pow(i,2))
    return result

print(get_square(5))

def get_square(n):
    for i in range(n):
        yield(pow(i,2))

grator = get_square(5)
for i in grator:
    print(i, end=', ')
