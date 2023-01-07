from selenium import webdriver
path='chromedriver.exe'
browser=webdriver.Chrome(path)
url='https://www.jd.com/'
browser.get(url)
content=browser.page_source
with open('test.json','w',encoding='utf-8') as fp:
    fp.write(content)