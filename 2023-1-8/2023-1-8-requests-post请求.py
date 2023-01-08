import requests
import json
url='https://fanyi.baidu.com/sug'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
}
data={
    'kw':'eye'
}
response=requests.post(url=url,data=data,headers=headers)
content=response.text
obj=json.loads(content)
print(obj)
# post请求不需要编解码
# 请求参数是data
# 不需要定制请求对象