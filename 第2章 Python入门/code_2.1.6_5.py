# -*- encoding: utf-8 -*-

"""
2.1.6十组最常用的内置函数
"""

data = [[0.468,0.975,0.446],[0.718,0.826,0.359]]
with open(r'..\res\csv_data.csv', 'w') as fp: # 写csv文件
    for line in data:
        ok = fp.write('%s\n'%','.join([str(item) for item in line]))

result = list()		
with open(r'..\res\csv_data.csv', 'r') as fp: # 读csv文件并解析
    for line in fp.readlines():
        result.append([float(f) for f in line.strip().split(',')])
		
print(result) # [[0.468, 0.975, 0.446], [0.718, 0.826, 0.359]]

