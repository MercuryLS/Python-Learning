from tkinter import N

def print_factors(n):    
    num=[0 for _ in range(64)]
    k=0
    for i in range(1,n+1):
        if n%i==0:
            num[k]=i
            k+=1
    print(1,end=" ")
    for j in range(1,k-1):
        print("and",num[j],end=" ")
    print("and",n)

def main():
    n=int(input("Please input an integer:"))
    print_factors(n)

main()