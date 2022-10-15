def is_vowel():
    char=input("Please input a character:")
    char=char.lower()
    if char in ['a','e','i','o','u']:
        print("是元音")
    else:
        print("不是元音")

is_vowel()