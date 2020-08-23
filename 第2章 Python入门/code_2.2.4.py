# -*- encoding: utf-8 -*-

"""
2.2.4 列表推导式
"""

a = [1, 2, 3, 4, 5]
result = list()
for i in a:
    result.append(i*i)

print(result) # [1, 4, 9, 16, 25]

a = [1, 2, 3, 4, 5]
print([i*i for i in a]) # [1, 4, 9, 16, 25]

print([i for i in range(10) if i%2==0]) # [0, 2, 4, 6, 8]
print([i if i%2==0 else -1*i for i in range(10)]) # [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]
