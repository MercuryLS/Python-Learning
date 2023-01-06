import urllib.request
from bs4 import BeautifulSoup
url='https://www.starbucks.com.cn/menu/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
soup=BeautifulSoup(content,'lxml')
name_list=soup.select('ul[class="grid padded-3 product"] strong')
print(name_list)