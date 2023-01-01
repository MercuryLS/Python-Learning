# fp=open('test.txt','w')
# fp.write('hello world!')
# fp.close()
# fp=open('demo/test.txt','w') #文件夹是不可以被创建的
with open('test.txt','w') as fp:
    fp.write('hello world!')
# 保证了关闭