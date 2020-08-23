# -*- encoding: utf-8 -*-

"""
3.5.1 urllib模块
"""

import urllib.request
import urllib.parse


# 下面的代码，演示了使用urllib模块发送GET请求，处理应答对象，以及从应答对象中获取数据的基本方法
# ---------------------------------------------------------------------------------------------

resp = urllib.request.urlopen('https://cn.bing.com') # 发送GET请求
print(resp.status) # http协议状态码：200
print(resp.getheader('Content-Type')) # 取得应答报头中的Content-Type：'text/html; charset=utf-8'

html = resp.read() # 取得应答内容（body的内容）
print(len(html)) # 113083
print(type(html)) # <class 'bytes'>

html = html.decode('utf-8')
print(len(html)) # 112539
print(type(html)) # <class 'str'>


# 下面的代码，演示了使用urllib模块构造请求对象，对需要提交的数据编码，以及定制请求报头的基本方法
# ---------------------------------------------------------------------------------------------

url = 'http://httpbin.org/post'
form_data = {'name':'Alice', 'age':18}
data = bytes(urllib.parse.urlencode(form_data), encoding='utf8')
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Host':'httpbin.org '
}
req = urllib.request.Request(url=url, data=data, headers=headers)
resp = urllib.request.urlopen(req) # 发送请求
print(resp.status) # http协议状态码：200
print(resp.read()) # 应答内容
print(resp.getheader('Content-Length')) # 从应答报头中读取内容长度
