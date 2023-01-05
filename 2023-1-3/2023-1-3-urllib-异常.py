import urllib.request
import urllib.error

url='https://blog.csdn.net/sulixu/article/details/119818949'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
try:
    request=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
except urllib.error.HTTPError:
    print('1')
except urllib.error.URLError:
    print('2')