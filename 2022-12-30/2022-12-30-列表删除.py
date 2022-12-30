alp1_list=['a','b','c','d']
alp2_list=['a','b','c','d']
alp3_list=['a','b','c','d']
#直接令新的列表等于会出问题
del alp1_list[1]
print(alp1_list)
alp2_list.pop()
print(alp2_list)
alp3_list.remove('c')
print(alp3_list)