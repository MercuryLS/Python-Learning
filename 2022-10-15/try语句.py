def is_integer(s):
    try:
        s=int(s)
        return True
    except ValueError:
        return False

def get_int(prompt):
    line=input(prompt)
    while not is_integer(line):
        print("not a integer;try again")
        line=input(prompt)
    return int(line)

def main():
    age=get_int("How old are you?")#"How old are you?"指向形参prompt,get_int里面去掉prompt后无法出现How old are you?.age指向line
    retire=55-age
    print("retire in",retire,"year")

main()