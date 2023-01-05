import random
import urllib.request

proxies_pool=[
    {'http':'121.13.252.60:41564'},
    {'http':'120.24.76.81:8123'},
    {'http':'210.5.10.87:53281'},
    {'http':'121.13.252.62:41564'},
]
url='https://www.baidu.com/s?wd=ip'
proxies=random.choice(proxies_pool)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
request=urllib.request.Request(url=url,headers=headers)
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')
with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)
