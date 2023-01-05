
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
import urllib.request
import urllib.parse
def create_request(page):
    base_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data={
        'cname':'武汉',
        'pid':'',
        'pageIndex':page,
        'pageSize':'10'
    }
    data=urllib.parse.urlencode(data).encode('utf-8')
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    request=urllib.request.Request(url=base_url,headers=headers,data=data)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    return response.read().decode('utf-8')

def download(page,content):
    with open(f'KFC-{str(page)}.json', 'w', encoding='utf-8') as fp:
        fp.write(content)

if __name__=='__main__':
    start_page=int(input('请输入起始页码:'))
    end_page=int(input('请输入结束的页码:'))
    for page in range(start_page,end_page+1):
        request=create_request(page)
        content=get_content(request)
        download(page,content)