#习题1：编写一个名为print_numbers的函数，该函数接受一个最大值作为参数，
# 函数将打印从1到(包含)该最大值的每个数字,每个数字用方括号括起来。

def print_numbers(max):
    for i in range(1,max+1):
        print("["+str(i)+"]")

def main():
    max=input("please input an integer")
    print_numbers(int(max))
main()