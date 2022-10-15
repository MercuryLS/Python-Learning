from tkinter import N

def to_binary(n):
    num=[0 for _ in range(64)]#一维数组不用x用_
    i=0
    while n!=0:
        num[i]=n%2
        n=n//2
        i+=1
    print("The result is:",end="")
    for i in range(i-1,-1,-1):
        print(num[i],end="")

def main():
    n=int(input("Input a number:"))
    to_binary(n)

main()