# -*- encoding: utf-8 -*-

"""
2.1.3 三种语句结构——顺序、分支和循环
"""

a, b, c = 3, 4, 5
if a > b: # 最简单的if-else分支
    print(a)
else:
    print(b)


if a > b and a > c: # 类似switch结构的分支
    print(a)
elif b > c:
    print(b)
else:
    print(c)


if a > b: # 嵌套的if-else分支
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

