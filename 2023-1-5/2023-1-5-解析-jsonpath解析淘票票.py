import urllib.request
import json
import jsonpath
url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1672890657064_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers={
# ':authority':'dianying.taobao.com',
# ':method':'GET',
# ':path':'/cityAction.json?activityId&_ksTS=1672890657064_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
# ':scheme':'https',
'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
# 'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'bx-v':'2.2.3',
'cookie':'cna=YHN6G0YkMBgCAXWboWi5KN/C; ariaDefaultTheme=undefined; t=8152315df338d5fff8458f2e92396b38; cookie2=1cb1b2968d738f25bdd91f500cddc37f; v=0; _tb_token_=e33e36a91eeee; isg=BFZW_-rYKZdVihx2dXCkoT4fpwxY95oxgGVkF8C_DTnUg_YdKIdMQfR9Gx9vK5JJ; l=fBrjOzmnT3kmgHfaBOfZFurza779LIRfguPzaNbMi9fP_D5H5aUOB67y-MLMCnGVesOyR3kbtB6WBzTG0yKNVcYON7h1WnqxndhyN3pR.',
'referer':'https://dianying.taobao.com/',
'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
'x-requested-with':'XMLHttpRequest',
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
# split切割
content=content.split('(')[1].split(')')[0]
with open('data.json','w',encoding='utf-8') as fp:
    fp.write(content)
obj=json.load(open('data.json','r',encoding='utf-8'))
city_list=jsonpath.jsonpath(obj,'$..regionName')
print(city_list)