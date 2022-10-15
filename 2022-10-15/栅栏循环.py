def multiprint(s,times):
    if times==0:
        print("()")
    else:
        print("("+s,end="")
        for i in range(times-1):
            print(";"+s,end="")
        print(")")

multiprint("please",6)