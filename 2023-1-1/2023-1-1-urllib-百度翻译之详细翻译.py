import urllib.request
import urllib.parse
import json

url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers={
    # 'Accept':'*/*',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'Acs-Token':'1672560348803_1672582973468_r5Il+d7eV22e4yrm2mJOCrZDFsvkGlrcsByz+U0uEAzOZfH1SDneOw6EY9oxm5tcmKiRXbhubz7cj3NGxacQFeG4lRr12bl1nAmWNeWMFBUU40vNkhkIaYR/iQbyl5B2laMRIGLTll4MXxqV3t/UlRIILKqDQolPpnOPlXKN1ANCuDkYNbn+AlTbSGew9+H8e0VTk7wz2QhHvh5C27eA9kgzJGkWK0Y9msNdFGZMUy8lVjyg0iKUwCGCqPLURXX/Cv6Jdo2tzUV61vx1LRi+Jn8nalrYNsbDzLSAip6mac/Pb7tXujVre4DEynTVO+GN/oGFzxqaVIi1XCQGjkSsXr/Qi44p17eAmv8abYYQroA=',
    # 'Connection':'keep-alive',
    # 'Content-Length':'116',
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'BIDUPSID=DCA3E165C7FBD05C04D598763EF33514; PSTM=1660126639; BAIDUID=DCA3E165C7FBD05CAB2EA77893D563CD:FG=1; BDUSS=UwVFdLTEhpZkhDeG9CY0VOUkxpR05ya2hBLXZxMjhaRG9GVGlrQXFWN3VvQjFqSVFBQUFBJCQAAAAAAAAAAAEAAAARIE2uuty6w7XEuNW6w7LFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO4T9mLuE~ZiTm; BDUSS_BFESS=UwVFdLTEhpZkhDeG9CY0VOUkxpR05ya2hBLXZxMjhaRG9GVGlrQXFWN3VvQjFqSVFBQUFBJCQAAAAAAAAAAAEAAAARIE2uuty6w7XEuNW6w7LFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO4T9mLuE~ZiTm; newlogin=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=008gak2la50g8100ak802gqq1hr2ig51i; BAIDUID_BFESS=DCA3E165C7FBD05CAB2EA77893D563CD:FG=1; ZFY=U2vKLz8tgu0VnfL1DV964d2lQMLHoM:ByqIzAItiUHBU:C; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=rompg4fc34n&ss=lcdg31yw&sl=4&tt=o9k&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=1xch&hd=1xdp"; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=3; delPer=0; H_PS_PSSID=36554_37975_37647_37555_37907_36921_37989_37930_37951_37904_26350_37881; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1672480537,1672563201,1672582934; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1672582973',
    # 'Host':'fanyi.baidu.com',
    # 'Origin':'https://fanyi.baidu.com',
    # 'Referer':'https://fanyi.baidu.com/?aldtype=16047',
    # 'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    # 'sec-ch-ua-mobile':'?0',
    # 'sec-ch-ua-platform':'"Windows"',
    # 'Sec-Fetch-Dest':'empty',
    # 'Sec-Fetch-Mode':'cors',
    # 'Sec-Fetch-Site':'same-origin',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    # 'X-Requested-With':'XMLHttpRequest'
}
data={
'from':'en',
'to':'zh',
'query':'love',
'simple_means_flag':'3',
'sign':'198772.518981',
'token': '1521d1d097d45fd5df64dcbf20969be9',
'domain':'common'
}
data=urllib.parse.urlencode(data).encode('utf-8')
request=urllib.request.Request(url=url,data=data,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
obj=json.loads(content)
print(obj)