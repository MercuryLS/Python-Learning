from re import I


def factorial(n):
    product=1
    for i in range(2,n+1):
        product*=I
    return product

def main():
    #if n<=0……
    n=int(input("the value of n:"))#n输入-1会输出1，range(2,0)不会循环直接弹出，不会报错
    print(factorial(-1))

main()