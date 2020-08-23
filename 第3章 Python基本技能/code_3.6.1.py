# -*- encoding: utf-8 -*-

"""
3.6.1 使用Beautifulsoup解析html/xml数据
"""

from bs4 import BeautifulSoup

html_doc = """
	<html>
		<div id="My gift">
			<p class="intro short-text" align="left">One</p>
			<p class="intro short-text" align="center">Two</p>
			<p class="intro short-text" align="right">Three</p>
		</div>
		<img class="photo" src="demo.jpg">
		<div class="photo">
			<a href="sdysit.com"><img src="logo.png"></a>
			<p class="subject">远思科技有限公司</p>
		</div>
	</html>
"""

soup = BeautifulSoup(html_doc, "lxml") # 使用lxml解析器

# 获取节点对象的名称和属性
print(soup.p.name) # p标签节点的name
print(soup.img.attrs) # 获取img标签节点的属性字典
print(soup.img['src']) # 也可以直接使用属性名获取属性值
print(soup.p['class']) # 获取p标签节点的样式，返回一个列表
print(soup.div['id']) # 获取div标签节点的id

# 获取节点的文本内容
print(soup.p.text) # 获取p标签节点的文本（方法1）
print(soup.p.getText()) # 获取p标签节点的文本（方法2）
print(soup.p.get_text()) # 获取p标签节点的文本（方法3）
print(soup.p.string) # 获取p标签节点的文本（方法4）

print(soup.div.text)
for item in soup.div.stripped_strings:
    print(item)

# 父节点、子节点、兄弟节点
print(soup.p.parent.name) # 获取p标签节点的父级节点的名字
print(soup.div.contents) # 以列表形式返回div标签节点的子节点
print(soup.div.children) # 以迭代器形式返回div标签节点的子节点
print(list(soup.div.children)) # 迭代器转为列表
print(list(soup.div.descendants)) # 转为列表的后代节点
p_tag = soup.p
print(p_tag.text)
p_tag = p_tag.next_sibling.next_sibling 
print(p_tag.text)
p_tag = p_tag.previous_sibling.previous_sibling
print(p_tag.text)

# 搜索节点
print(soup.find('img')) # 返回单个节点
print(soup.find_all('p')) # 返回节点列表
import re
print(soup.find_all(re.compile('^d'))) # 返回节点名以d开头的节点列表

print(soup.find_all(id='My gift')[0].name) # 查找id=My gift的节点
print(soup.find_all(id=True)[0].name) # 查找有id属性的节点
print(soup.find_all(attrs={"id":"My gift"})[0].name) # 使用attrs查找
print(soup.find_all(attrs={"class":"intro short-text"  ,"align":"right"})[0].text) # 使用attrs查找

print(soup.find_all(attrs={"align":"right"})[0].text)
print(soup.find_all("p", class_="intro"))
print(soup.find_all(string="Two"))

def justdoit(tag):
    return tag.parent.has_attr('id') and tag['align']=='center'

print(soup.find_all(justdoit))
