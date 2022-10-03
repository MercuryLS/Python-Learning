def vertical():
    string=input('Enter String: ')
    for char in range(0,len(string)+1):
        print(string[char:char+1])

def main():
    vertical()

main()
