def main():
    how_many=int(input("how many"))
    mysum=0
    for i in range(how_many):
        next=float(input("next number?"))
        mysum+=next
    print()
    print("sum=",mysum)

main()