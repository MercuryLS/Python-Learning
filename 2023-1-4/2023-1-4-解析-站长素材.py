import urllib.request
from lxml import etree

def create_request(page):
    if page == 1:
        url='https://sc.chinaz.com/tupian/gudianmeinvtupian.html'
    else:
        url = f'https://sc.chinaz.com/tupian/gudianmeinvtupian_{str(page)}.html'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    return response.read().decode('utf-8')

def download(content):
    tree=etree.HTML(content)
    name_list=tree.xpath('//div[@class="item"]/img/@alt')
    src_list=tree.xpath('//div[@class="item"]//img/@data-original')
    for i in range(len(name_list)):
        name=name_list[i]
        src=src_list[i]
        img_url = f'https:{src}'
        img_url=img_url.replace('_s', '')#这里用了.replace指令才可以下载高清大图
        urllib.request.urlretrieve(url=img_url, filename='./E:/img'+name+'.jpg')#这里方便看就不合并了

if __name__ == '__main__':
    start_page=int(input('请输入起始页码:'))
    end_page=int(input('请输入结束页码:'))
    for page in range(start_page,end_page+1):
        request=create_request(page)
        content=get_content(request)
        download(content)
        
