total=0
num=int(input("Input a integer,or-1 to stop"))
Max=num
Min=num
while num!=-1:
    if num>Max:
        Max=num
    if num<Min:
        Min=num
    num=int(input("Input a integer,or-1 to stop"))
print("max=",Max,"min=",Min)