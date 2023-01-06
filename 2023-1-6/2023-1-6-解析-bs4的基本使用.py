from bs4 import BeautifulSoup
soup=BeautifulSoup(open('data.html',encoding='utf-8'),'lxml')
# 根据标签名查找结点，找到的是第一个符合的数据
# print(soup.a)
# 数据的属性
# print(soup.a.attrs)

#bs4的一些函数

#find返回第一个符合条件的数据
# print(soup.find('a'))
# print(soup.find('a',title='a2'))
# print(soup.find('a',class_="a1"))注意下划线

#find_all返回一个列表
# print(soup.find_all('a'))
# 获取多个标签的数据
# print(soup.find_all(['a','span']))

#limit查找前几个数据
# print(soup.find_all('li',limit=2))

#select
# 返回一个列表多个数据
# print(soup.select('a'))
# 通过.代替class叫做类选择器
# print(soup.select('.a1'))
# #id选择器
# print(soup.select('#l1'))
# 属性选择器
# print(soup.select('li[id]'))
# 查找id中为l2的数据
# print(soup.select('li[id="l2"]'))
# 层级选择器
# 后代选择器
# print(soup.select('div li'))
# 子代选择器
# print(soup.select('div > ul > li'))
# 找到a标签和li标签
# print(soup.select('a,li'))
# 获取节点信息
# obj=soup.select('#d1')[0]
# 如果标签中只有内容二者一样，如果还有标签string无法获得，因此推荐get_text()
# print(obj.string)
# print(obj.get_text())
obj=soup.select('#p1')[0]
# name是标签的名字
# print(obj.name)
# 将属性值作为一个字典返回
# print(obj.attrs)
# 获取节点的属性
print(obj.attrs.get('class'))
print(obj['class'])