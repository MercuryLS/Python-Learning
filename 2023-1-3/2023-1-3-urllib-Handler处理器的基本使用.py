import urllib.request
url='http://www.baidu.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
request=urllib.request.Request(url=url,headers=headers)
handlers=urllib.request.HTTPHandler()
opener=urllib.request.build_opener(handlers)
response=opener.open(request)
content=response.read().decode('utf-8')
print(content)