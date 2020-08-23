# -*- encoding: utf-8 -*-

"""
3.6.2 使用正则表达式解析文本数据
"""

import re

s1 = '公元2020年'
s2 = '公元2020年以后'
s3 = '自公元2020年以来'

p = re.compile(r'公元([1-9]\d*)年')

result = p.match(s1) # 匹配s1
print(result) # 匹配成功
print(result.group()) # group()方法返回匹配到的字符串：'公元2020年'
print(result.groups())# groups()方法返回子表达式匹配到的字符串：('2020',)

result = p.match(s2) # 匹配成功，虽然s2末尾多了两个字
print(result)

result = p.match(s3) # 匹配失败，因为s3开头多了一个字
print(print(result)) # None

p = re.compile(r'公元([1-9]\d*)年$')
result = p.match(s2) # 模式串加上$后，末尾多了两个字的s2匹配失败
print(print(result)) # None

p = re.compile(r'公元([1-9]\d*)年')

result = p.search(s1)
print(result) # s1存在匹配的子串
print(result.group())
print(result.groups())

print(p.search(s2)) # s2存在匹配的子串
print(p.search(s3)) # s3存在匹配的子串

p = re.compile(r'^公元([1-9]\d*)年$') # 若指定以模式串开头和结尾
print(p.search(s2)) # s2不存在匹配的子串 
print(p.search(s3)) # s3不存在匹配的子串

txt = """
WDC for Geomagnetism, Kyoto
Hourly Equatorial Dst Values (REAL-TIME)  
          MARCH   2020
DAY   1   2   3   4   5   6   7   8    9  10
 1  -19 -11 -10  -7  -8  -9 -11 -14  -15  -9
 2  -12 -14 -14 -16 -15 -14 -12 -11  -12 -10
 3    1  -3 -10  -9  -9  -9 -10 -10  -13  -9
 4   -6  -3  -1  -2  -2  -3  -2  -3   -6  -3
 5    1   3   3   3   0  -3  -2  -2   -1   2
 """
 
p = re.compile('^\s([1-5])\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)$', flags=re.M)
result = p.findall(txt)
print(result)

s = '无论，还是。或者？都是分隔符'
p = re.compile(r'[，。？]')
print(p.split(s)) # ['无论', '还是', '或者', '都是分隔符']

s = '无论，还是。或者？都是分隔符'
p = re.compile('[，。？]')
print(p.sub('+', s)) # '无论+还是+或者+都是分隔符'

