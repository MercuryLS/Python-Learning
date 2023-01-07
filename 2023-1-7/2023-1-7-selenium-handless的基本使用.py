# 无界面浏览器，更加快捷
from selenium import webdriver
from selenium. webdriver. chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless' )
# chrome_options.add_argument('--disable-gpu')
# path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = path
# browser = webdriver .Chrome(chrome_options=chrome_options)
# 封装形式：
def share_browers():
    chrome_options = Options()
    chrome_options.add_argument('--headless' )
    chrome_options.add_argument('--disable-gpu')
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    return webdriver .Chrome(chrome_options=chrome_options)

browser=share_browers()
url='https://www.baidu.com/'
browser.get(url)
browser.save_screenshot('baidu.png')