import jsonpath
import json
obj=json.load(open('store.json','r'))
# 注意store中没有中文字符不需要encoding='utf-8
author_1ist=jsonpath.jsonpath(obj,'$.store.book[*].author')
author_list2=jsonpath.jsonpath(obj,'$..author')
all_=jsonpath.jsonpath(obj,'$.store.*')
price_ist=jsonpath.jsonpath(obj,'$.store..price')
# 第三本书
book3=jsonpath.jsonpath(obj,'$..book[2]')
# 最后一本书,这里是book的length写法,@反映了
book=jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
# 前两本书
book1_2=jsonpath.jsonpath(obj,'$..book[:2]')
# 过滤含isbn的书，条件过滤需要在圆括号前加?
book_list=jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
# 超过十元的书
book_list2=jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(book_list2)