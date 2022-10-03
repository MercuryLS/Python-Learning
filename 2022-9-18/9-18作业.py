#Q1(1)
for i in range(4):
    print("*****")
    
#Q1(2)
for i in range(1,6):
    print("*"*i)
    
#Q1(3)
for i in range(1,8):
    print(str(i)*i)
    
#Q1(4)
for i in range(0,12,2):
    print("\\"*i,end="")
    print("!"*(22-2*i),end="")
    print("/"*i)
    
#Q2
for i in range(1,11):
    sum = 0
    for j in range(1,i+1):
        sum = sum + i
    print(sum,end=" ")


