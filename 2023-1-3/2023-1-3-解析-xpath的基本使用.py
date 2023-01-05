from lxml import etree
tree=etree.parse('2022-1-3-解析-xpath的基本使用.html')
# # 查找ul下的li
# li_list=tree.xpath('//body/ul/li')
#text()获取标签中的内容，获取网页数据时不需要
# 查找所有有id的li标签
# li_list=tree.xpath('//body/ul/li[@id]/text()')

# 查找id为1的标签
# li_list=tree.xpath('//body/ul/li[@id="l1"]/text()')

# 查找id为1的li标签的class的属性值
# li_list=tree.xpath('//body/ul/li[@id="l1"]/@class')

# 查询id含l的标签
# li_list=tree.xpath('//body/ul/li[contains(@id,"l")]/text()')

# 查询id以l开头的标签
# li_list=tree.xpath('//body/ul/li[start-with(@id,"l")]/text()')

# 查询id为l1,class为c1的标签
# li_list=tree.xpath('//body/ul/li[@id="l1" and @class="c1"]/text()')
li_list=tree.xpath('//body/ul/li[@id="l1"]/text()' | '//body/ul/li[@id="l2"]/text()') #不允许在id中括号里进行或运算

print(li_list)
print(len(li_list))