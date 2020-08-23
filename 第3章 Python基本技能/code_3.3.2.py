# -*- encoding: utf-8 -*-

"""
3.3.2 读写CSV文件
"""

def read_csv(csv_file, sep=','):
    data = list()
    with open(csv_file, 'r') as fp:
        for line in fp.readlines():
            row = [float(item) for item in line.strip().split(sep)]	
            data.append(row)
    return data

def write_csv(data, csv_file, sep=','):
    with open(csv_file, 'w') as fp:
        for row in data:
            fp.write(sep.join([str(item) for item in row]))
            fp.write('\n')

data = read_csv(r'..\res\demo.csv') # 读CSV文件
print(data)
	
write_csv(data, r'..\res\demo_w.csv') # 写CSV文件
