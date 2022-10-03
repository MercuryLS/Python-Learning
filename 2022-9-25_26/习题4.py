def main():
    a=int(input("请输入a:"))
    b=int(input("请输入b:"))
    def print_square():
     for i in range (a,b+1):
        for k in range(i,b+1):
            print(k,end="")
        for j in range(a,i):
            print(j,end="")
        print('')
    print_square()

main()
