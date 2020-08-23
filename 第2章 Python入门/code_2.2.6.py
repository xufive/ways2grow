# -*- encoding: utf-8 -*-

"""
2.2.6 with-as
"""

fp = open(r"..\res\csv_data.csv", 'r')
try:
    contents = fp.readlines()
    print(contents)
finally:
    fp.close()

with open(r"..\res\csv_data.csv", 'r') as fp:
    contents = fp.readlines()
    print(contents)
