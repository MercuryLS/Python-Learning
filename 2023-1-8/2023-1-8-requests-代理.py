import requests
url='https://www.baidu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
}
data={
    'wd':'ip'
}
proxy={
    'http':'183.236.232.160:8080',
    # 'http':'221.205.83.193:8088'
}
response=requests.get(url=url,params=data,headers=headers,proxies=proxy)
content=response.text
with open('data.html','w',encoding='utf-8') as fp:
    fp.write(content)