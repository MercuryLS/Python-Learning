import urllib.request

url='https://www.baidu.com/s?wd=ip'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
request=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(request)
proxies={'http':'61.216.185.88:60808'}
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')
with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)
