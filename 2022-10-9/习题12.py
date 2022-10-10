def word_count(s):
    num=len(s.split())
    print(num)

def main():
    s=input("Please input a sentence:")
    word_count(s)

main()