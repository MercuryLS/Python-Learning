def print_palindrome():
    s=input("Please input a word:")
    s=s.lower()
    n=len(s)
    if n%2==0:
        for m in range(n):
            if s[m]==s[n-1-m]:
                print("是回文数")
                break
            else:
                print("非回文数")
                break
    else:
        for j in range(int((n+1)/2)):
            if s[j]==s[n-1-j]:
                print("是回文数")
                break
            else:
                print("非回文数")
                break

def main():
    print_palindrome()

main()