def days_in_month():
    n=int(input("Please input the month:"))
    if (n==1)|(n==3)|(n==5)|(n==7)|(n==8)|(n==10)|(n==12):
        print(31)
    elif (n==4)|(n==6)|(n==9)|(n==11):
        print(30)
    else:
        year=int(input("Please input the year:"))
        if ((year%4==0)&(year%100!=0))|(year%400==0):
            print(29)
        else:
            print(28)
            
def main():
    days_in_month()

main()
