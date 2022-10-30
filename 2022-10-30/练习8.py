def vowel_count(string,count):  # sourcery skip: avoid-builtin-shadow
    string=string.lower()
    l=list(string)
    for item in l:
        if item == 'a':
            count[0]+=1
        if item == 'e':
            count[1]+=1
        if item == 'i':
            count[2]+=1
        if item == 'o':
            count[3]+=1
        if item == 'u':
            count[4]+=1

def main():
    count=[0,0,0,0,0]
    string=input("Please input a string:")
    vowel_count(string,count)
    print(count)

main()