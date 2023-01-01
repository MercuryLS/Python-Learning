import json
# with open('test.txt','w') as fp:
#     fp.write('hello world')

# 序列化的方式
# dumps()
# fp=open('test.txt','w')
# name_list=['zs','ls']
# names=json.dumps(name_list)
# fp.write(names)
# fp.close()
# print(names)

# dump()
# json.dump(name_list,fp)
# fp.close()

# 反序列化
fp=open('test.txt','r')
content=fp.read()
print(content)

# load
# result=json.loads(content)

# loads
result=json.load(fp)
print(result)