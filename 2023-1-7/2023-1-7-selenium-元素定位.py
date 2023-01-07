from selenium import webdriver
path='chromedriver.exe'
browser=webdriver.Chrome(path)
url='https://www.baidu.com/'
browser.get(url)
# 根据id
# botton=browser.find_element_by_id('su')
# 根据标签属性的值
# botton=browser.find_element_by_name('wd')
# 根据xpath,注意第一个返回的是列表
# botton=browser.find_elements_by_xpath('//*[@id="su"]')
# botton=browser.find_element_by_xpath('//*[@id="su"]')
# 根据标签名获取对象
# botton=browser.find_elements_by_tag_name('input')
# 根据bs4的语法实现
# botton=browser.find_elements_by_css_selector("#su")
# 通过链接文本获取对象
botton=browser.find_element_by_partial_link_text('图片')
print(botton)