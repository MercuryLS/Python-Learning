#urlencode多参数时用到
#https://www.baidu.com/s?wd=%周杰伦&sex=男
# import urllib.parse
# data={'wd':'周杰伦','sex':'男','location':'Taiwan'}
# a=urllib.parse.urlencode(data)
# print(a)
#获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7源码
import urllib.request
import urllib.parse
base_url='https://www.baidu.com/s?'
data={'wd':'周杰伦','sex':'男','location':'中国台湾省'}
new_data=urllib.parse.urlencode(data)
url=base_url+new_data
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
