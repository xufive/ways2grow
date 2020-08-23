# -*- encoding: utf-8 -*-

"""
2.1.5 五大内置类——列表、字典、元组、集合、字符串
"""

print(str(3.14)) # 数字转字符串
print(str(['a',1])) # 列表转字符串
print(str({'a':1, 'b':2})) # 字典转字符串

s = 'python大法好，very good.'
print(s[1:-1]) # 掐头去尾：'ython大法好，very good'
print(s[::2]) # 隔一个取一个：'pto大好vr od'
print(s[::-1]) # 反转字符串：'.doog yrev，好法大nohtyp'
print(s.upper()) # 全部大写：'PYTHON大法好，VERY GOOD.'
print(s.lower()) # 全部小写：'python大法好，very good.'
print(s.capitalize()) # 字符串首字母大写：'Python大法好，very good.'
print(s.title()) # 单词首字母大写：'Python大法好，Very Good.'
print(s.startswith('python')) # 判断是否以指定的子串开头：True
print(s.endswith('good.')) # 判断是否以指定的子串结尾：True
print(s.find('very')) # 首次出现的索引，未找到则返回-1：10
print(s.split()) # 分割字符串，还可以指定分隔符：['python大法好，very', 'good.']
print(s.replace('very', 'veryvery')) # 替换子串：'python大法好，veryvery good.'
print('2345.6'.isdigit()) # 判断是否是数字：False
print('adS12K56'.isalpha()) # 判断是否是字母：False
print('adS12K56'.isalnum()) # 判断是否是字母和数字：True
print('\t adS12K56 \n'.strip()) # 去除首尾空格（包括制表位和换行符）：'adS12K56'
