#fp=open('test.txt','w')
# fp=open('test.txt','a')
# fp.write('Hello\n'*5)
#如果文件存在会先清空再写
# fp.close()
fp=open('test.txt','r')
content=fp.readlines()
print(content)