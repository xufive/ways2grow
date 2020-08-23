# -*- encoding: utf-8 -*-

"""
3.5.2 requests模块
"""

import requests
from requests.cookies import RequestsCookieJar
import re, html

# 尝试运行这段代码的读者，请先在代码中的第一个url注册，并使用自己的账号替换代码中的用户名和密码。

resp = requests.get('https://urs.earthdata.nasa.gov/home')
print(resp.ok) # 查看应答是否成功

p = re.compile(r'name="authenticity_token" value="(.*)" />')
token = p.findall(resp.text)[0] # 解析token
jar = RequestsCookieJar() # 创建RequestsCookieJar对象
jar.update(resp.cookies)
url = 'https://urs.earthdata.nasa.gov/login'
forms = {
    "username": "linhl",
    "redirect_uri": "",
    "commit": "Log+in",
    "client_id": "",
    "authenticity_token": token,
    "password": "1234567iI"
}

resp = requests.post(url, data=forms, cookies=jar) # 提交登录表单
print(resp.ok) # 查看应答是否成功

jar.update(resp.cookies) # 更新cookie
url = 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/6/MOD13Q1/2019/321/MOD13Q1.A2019321.h00v08.006.2019337235356.hdf'
resp = requests.get(url, cookies=jar) # 请求下载页
print(resp.ok) # 查看应答是否成功

p = re.compile(r'href="(https://ladsweb.modaps.eosdis.nasa.gov.*hdf)"')
furl = p.findall(resp.text)[0] # 解析文件下载的url
furl= html.unescape(furl) # 反转义，将'&amp;'替换为'&'
resp = requests.get(furl, cookies=jar) # 下载文件
print(resp.ok) # 查看应答是否成功

with open(r'..\res\MOD13Q1.hdf', 'wb') as fp: # 保存文件
    fp.write(resp.content)
