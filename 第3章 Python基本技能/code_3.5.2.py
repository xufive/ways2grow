# -*- encoding: utf-8 -*-

"""
3.5.2 requests模块
"""

import requests

# Session类在发送请求、接收应答时自动处理cookie
sess = requests.Session()

# 1. 使用合法的账号登录
url_login = 'http://sdysit.com/modis'
form_login = {
    "account": "guest",
    "passwd": "hello"
}

resp = sess.post(url_login, data=form_login)
if resp.ok:
    print('1. 已成功登录\n')
else:
    print('登录失败')
    sys.exit(1)

# 2. 请求文件列表
url_list = 'http://sdysit.com/modis/list'

resp = sess.get(url_list)
if resp.ok:
    print('2. 已获取文件列表\n')
else:
    print('请求文件列表失败')
    sys.exit(1)

# 3. 解析文件下载地址
result = resp.json()
if result['code'] == '10':
    print('3. 已解析文件下载地址')
    for item in result['data']:
        print('\t', item['name'], '->', item['url'])
    print()
else:
    print('文件列表数据错误')
    sys.exit(1)

# 4. 下载文件
print('4. 文件文件')
for item in result['data']:
    print('\t开始下载文件...%s'%item['name'])
    resp = sess.get(item['url']) # 下载文件
    if resp.ok:
        with open(r'..\res\%s'%item['name'], 'wb') as fp: # 保存文件
            fp.write(resp.content)
        print('\t文件%s下载完毕\n'%item['name'])
    else:
        print('\t下载文件%s失败'%item['name'])
