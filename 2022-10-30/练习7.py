def collapse(list,sum):  # sourcery skip: avoid-builtin-shadow
    if len(list)%2==0:
        sum.extend(list[i]+list[i+1] for i in range(0,len(list)-1,2))
    else:
        sum.extend(list[i]+list[i+1] for i in range(0,len(list)-2,2))
        sum.append(list[-1])

def main():
    list=[1,2,3,4,5]
    sum=[]
    collapse(list,sum)
    print(sum)

main()