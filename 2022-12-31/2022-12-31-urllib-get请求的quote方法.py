import urllib.request
import urllib.parse
name=urllib.parse.quote('周杰伦')
#周杰伦变成了Unicode编码
url='https://www.baidu.com/s?wd='
url+=name
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
print(content)