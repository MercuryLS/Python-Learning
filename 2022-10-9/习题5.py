def xo():
    size=int(input("Please input the size:"))
    for i in range(1,size+1):
        for j in range(1,size+1):
            if(i==j)|(i+j==size+1):
                print("x",end="")
            else:
                print("o",end="")
        print("")
        
def main():
    xo()
    
main()