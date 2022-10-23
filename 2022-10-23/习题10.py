from fileinput import close
from pydoc import stripid
import random
from tkinter import N
def three_heads():
    n=[0,0,0]
    count=0
    while 1:
        n[0]=0
        n[0]=random.randint(0,1)
        if n[0]==1:
            with open("coin.txt","a") as coin:
                if (count-9)%10==0:
                    print("H",file=coin)
                else:
                    print("H",file=coin,end="")
                count+=1
        else:
            with open("coin.txt","a") as coin:
                if (count-9)%10==0:
                    print("T",file=coin)
                else:
                    print("T",file=coin,end="")
                count+=1
        if n[0]==1 and n[1]==1 and n[2]==1:
            break

        n[1]=0
        n[1]=random.randint(0,1)
        if n[1]==1:
            with open("coin.txt","a") as coin:
                if (count-9)%10==0:
                    print("H",file=coin)
                else:
                    print("H",file=coin,end="")
                count+=1
        else:
            with open("coin.txt","a") as coin:
                if (count-9)%10==0:
                    print("T",file=coin)
                else:
                    print("T",file=coin,end="")
                count+=1
        if n[0]==1 and n[1]==1 and n[2]==1:
            break

        n[2]=0
        n[2]=random.randint(0,1)
        if n[2]==1:
            with open("coin.txt","a") as coin:
                if (count-9)%10==0:
                    print("H",file=coin)
                else:
                    print("H",file=coin,end="")
                count+=1
        else:
            with open("coin.txt","a") as coin:
                if (count-9)%10==0:
                    print("T",file=coin)
                else:
                    print("T",file=coin,end="")
                count+=1
        if n[0]==1 and n[1]==1 and n[2]==1:
            break
    coin.close()

def coin_flip():
    with open("coin.txt","r") as coin:
        for line in coin:
            print(line.rstrip())
    coin.close()

def main():
    with open("coin.txt","w") as coin:
        print("",file=coin,end="")
    three_heads()
    coin_flip()

main()