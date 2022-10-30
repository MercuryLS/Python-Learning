from re import X

def replace(list,target,replacement):
    if target in list:
        index=list.index(target)
        list[index]=replacement

def delete_a(list):
    x=len(list)
    i=0
    while i<x:
        string=str(list[i])
        if 'a' in string:
            list.remove(string)
            x=len(list)
            i=0
        i+=1

def main():
    data=["it","was","a","stormy","night"]
    data.insert(3,"dark")
    data.insert(4,"and")
    print(data)
    replace(data,"was","is")
    print(data)
    delete_a(data)
    print(data)

main()