import urllib.request
import urllib.parse
import json

url='https://fanyi.baidu.com/sug'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
data={'kw':'spider'}
#post请求参数必须编码
data=urllib.parse.urlencode(data).encode('utf-8')
#post请求的参数不会拼接在url的后面，应该放在请求对象的参数中
request=urllib.request.Request(url=url,data=data,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
obj=json.loads(content)
print(obj)
#多行文件实现迅速排版:Shift+Alt+F