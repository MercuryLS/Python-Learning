# 难点1：隐藏域
# 难点2：验证码
import requests
from bs4 import BeautifulSoup
import urllib.request

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
}
url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
response=requests.get(url=url,headers=headers)
content=response.text
soup=BeautifulSoup(content,features="lxml")
vies_state=soup.select('#__VIEWSTATE')[0].attrs.get('value')
view_state_generator=soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# 验证码
code=soup.select('#imgCode')[0].attrs.get('src')
code_url = f'https://so.gushiwen.cn{code}'
# urllib.request.urlretrieve(url=code_url,filename='code.jpg')  请求之后下面再次请求导致验证码刷新
# 用session方法
session=requests.session()
response_code=session.get(code_url)
# 注意是二进制数据，因为下载的是图片
content_code=response_code.content
# wb是将二进制写入文件
with open('code.jpg','wb') as img:
    img.write(content_code)

code_name=input('请输入验证码:')
login_url='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
login_data={
    '_VIEWSTATE':vies_state,
    '__VIEWSTATEGENERATOR':view_state_generator,
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email':'lz1569141492@outlook.com',
    'pwd':'lz,20040303.',
    'code':code_name,
    'denglu':'登录'
}
login_response=session.post(url=login_url,headers=headers,data=login_data)
login_content=login_response.text
with open('poem.html','w',encoding='utf-8') as fp:
    fp.write(login_content)