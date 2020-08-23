# -*- encoding: utf-8 -*-

"""
3.1.2 datetime模块
"""

from datetime import datetime, timedelta

# 1. datetime 子类
# ------------------------------

print(datetime.now()) # 获取当前本地时间
print(datetime(2020,1,1,0,0,0)) # 实例化datetime对象
print(datetime.fromisoformat('2020-04-06 10:20:30')) #字符串转datetime对象
print(datetime.strptime('20201010', '%Y%m%d')) #字符串转datetime对象
print(datetime.fromtimestamp(1585855029.0)) # 时间戳转datetime对象
dt = datetime.utcnow() # 获取当前UTC时间
print(dt.timetuple()) # 返回time.struct_time对象
print(dt.timestamp()) # 返回datetime对象的时间戳
print(dt.isoweekday()) # 返回一个整数代表星期几，星期一为1，星期天为7
print(dt.weekday()) # 返回一个整数代表星期几，星期一为0，星期天为6
print(dt.strftime('%Y-%m-%d %X')) # 返回日期时间字符串

# 2. timedelta 子类
# ------------------------------

print(timedelta(3))  # 生成3天的timedelta对象
delta = timedelta(days=3, hours=5, minutes=25, seconds=10)
print(delta) # delta是一个3天零19510秒的timedelta对象
print(delta.days) # delta包含的天数
print(delta.total_seconds()) # 返回delta的总秒数
dt = datetime.now() # 获取当前日期时间
print(dt-delta) # 3天又5小时25分钟10秒之前的日期时间
