import requests
url='https://www.baidu.com/'
response=requests.get(url=url)
print(type(response))
# 一个类型六个属性
response.encoding='utf-8'
# 字符串形式
print(response.text)
# url地址
print(response.url)
# 二进制数据
print(response.content)
# 返回响应的状态码
print(response.status_code)
# 响应头
print(response.headers)
