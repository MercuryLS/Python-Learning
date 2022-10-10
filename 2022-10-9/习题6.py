def smallest_largest():
    total=int(input("The numbers:"))
    
    for i in range(1,total+1,1):
        num=int(input("number "+str(i)+":"))
        if(i==1):
            smallest=num
            largest=num
        else:
            if(num>largest):
                largest=num
            if(num<smallest):
                smallest=num
    print("smallest="+str(smallest))
    print("largest="+str(largest))
    
def main():
    smallest_largest()

main()