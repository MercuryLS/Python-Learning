phrase=input("type a phrase(enter to quit)?")
shortest=phrase
while phrase!="":
    if len(phrase)<len(shortest):
        shortest=phrase
    phrase=input("type a phrase (enter to quit)?")
print("shortest phrase was",shortest)
