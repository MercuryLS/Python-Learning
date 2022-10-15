import random
from tkinter import N
def three_heads():
    n=[0,0,0]
    while 1:
        n[0]=0
        n[0]=random.randint(0,1)
        if n[0]==1:
            print("H")
        else:
            print("T")
        if n[0]==1 and n[1]==1 and n[2]==1:
            print("Three heads in a row!")
            break
        
        n[1]=0
        n[1]=random.randint(0,1)
        if n[1]==1:
            print("H")
        else:
            print("T")
        if n[0]==1 and n[1]==1 and n[2]==1:
            print("Three heads in a row!")
            break

        n[2]=0
        n[2]=random.randint(0,1)
        if n[2]==1:
            print("H")
        else:
            print("T")
        if n[0]==1 and n[1]==1 and n[2]==1:
            print("Three heads in a row!")
            break

def main():
    three_heads()

main()