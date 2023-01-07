# sourcery skip: avoid-builtin-shadow
from selenium import webdriver

path='chromedriver.exe'
browser=webdriver.Chrome(path)

url='https://www.baidu.com/'
browser.get(url)

input=browser.find_element_by_id('su')
#获取元素属性
print(input.get_attribute('class'))
#获取标签文本
print(input.tag_name)
#获取元素文本
print(input.text)#获取的是><之间的文字