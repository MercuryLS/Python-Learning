# sourcery skip: avoid-builtin-shadow
from selenium import webdriver
import time

path='chromedriver.exe'
browser=webdriver.Chrome(path)

url='https://www.baidu.com/'
browser.get(url)
time.sleep(2)

input=browser.find_element_by_id('kw')
# 文本框输入周杰伦
input.send_keys('周杰伦')
time.sleep(2)
botton=browser.find_element_by_id('su')
botton.click()
time.sleep(2)
# 滑动到底部
js_bottom='document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(2)
# 获取下一页
next_botton=browser.find_element_by_xpath('//*[@id="page"]/div/a[10]')
next_botton.click()
# 返回一步
browser.back()
time.sleep(2)
# 向前一步
browser.forward()
time.sleep(2)
# 退出
browser.quit()