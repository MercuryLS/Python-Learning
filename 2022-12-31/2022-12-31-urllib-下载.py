import urllib.request
url_page='http://www.baidu.com'
urllib.request.urlretrieve(url_page,'baidu.html')
url_imag='http://safe-img.xhscdn.com/bw1/025b0813-1918-4253-86af-03a7ca4052b5?imageView2/2/w/1080/format/jpg'
urllib.request.urlretrieve(url_imag,filename='threebody.jpg')
url_video='http://www.bilibili.com/b23de534-d12d-42df-8bf9-20c4fe388ad3'
urllib.request.urlretrieve(url_video,'asas.mp4')