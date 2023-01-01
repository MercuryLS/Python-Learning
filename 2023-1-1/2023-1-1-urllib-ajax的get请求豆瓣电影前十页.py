import urllib.request
import urllib.parse
# 第一页:https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&        start=0&limit=20
# 第二页:https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&        start=20&limit=20
# 第三页:https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&        start=40&limit=20

def create_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data={
        'start':(page-1)*20,
        'limit':20
    }
    data=urllib.parse.urlencode(data)
    base_url+=data
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    request=urllib.request.Request(url=base_url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    return response.read().decode('utf-8')

def down_load(page,content):
    with open('douban-'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page=int(input('请输入起始的页数:'))
    end_page=int(input('请输入结束的页数:'))
    for page in range(start_page,end_page+1):
        request=create_request(page)
        content=get_content(request)
        down_load(page,content)