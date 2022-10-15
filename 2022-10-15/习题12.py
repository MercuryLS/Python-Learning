from tkinter import N


def digit_sum(n):
    n=abs(n)
    sum=0
    while n!=0:
        sum+=n%10
        n=n//10
    print("The sum is:",sum)

def main():
    n=int(input("Please input an integer:"))
    digit_sum(n)

main()