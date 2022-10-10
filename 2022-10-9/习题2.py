def repl():
    n=int(input("Please input n:"))
    s=""
    sentence=input("Please input a sentence:")
    for i in range(n):
        s+=sentence
    print(s)

def main():
    repl()

main()