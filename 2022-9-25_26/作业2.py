#·自测12:一人要将小额支票兑换成纸币(100元、10元、5元、2元、1元).
# 试编写一函数print_changes,该函数接受钱数，
# 并返回纸币的种类及张数(尽量使张数最少)。

def print_changes(money):
    count100=money//100
    left100=money%100
    count10=left100//10
    left10=left100%10
    count5=left10//5
    left5=left10%5
    count2=left5//2
    count1=left2=left5%2
    print(str(money)+"元将兑换"+str(count100)+"张100元纸币，"
        +str(count10)+"张10元纸币，"+str(count5)+"张5元纸币，"
        +str(count2)+"张2元纸币，"+str(count1)+"张1元纸币")
    
    
def main():
    m=input("please input money")
    print_changes(int(m))
    
main()