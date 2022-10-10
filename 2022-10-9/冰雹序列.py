def print_mailstone_min_max(start,length):
    max=start
    min=start
    print(start,end="")
    x=start
    for i in range(length-1):
        if x%2==0:
            x=x//2
        else:
            x=3*x+1
        print(x,end=" ")
        if max<x:
            max=x
        if min>x:
            min=x
    print("\nthe max number is:",max)
    print("the min number is:",min)