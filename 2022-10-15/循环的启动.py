import random
def main():
    print("This program picks numbers from 1 to 10")
    print("until a particular numbers comes up")
    print()

    number=int(input("pick a number between 1 and 10?"))
    result=0
    count=0
    while result!=number:
        result=random.randint(1,10)
        print("next number=",result)
        count+=1
    print("your number came up after",count,"times")

main()