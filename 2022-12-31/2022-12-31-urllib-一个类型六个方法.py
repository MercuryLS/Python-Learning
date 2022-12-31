import urllib.request
url='http://www.baidu.com'
response=urllib.request.urlopen(url)
#一个类型
#print(type(response))
#content=response.read(5) 返回多少个字节
content=response.readlines()
print(content)
print(response.getcode())
print(response.geturl())
print(response.getheaders())