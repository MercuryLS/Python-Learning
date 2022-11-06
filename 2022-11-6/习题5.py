def reverse(dict):
    reversed_dict={}
    list_value=list(set(dict.values()))
    for v in list_value:
        list_v=[]
        for k in dict.keys():
            if dict[k]==v:
                list_v.append(k)
        reversed_dict[v]=list_v
    return reversed_dict

def main():
    myDict={42:"marty",81:"sue",17:"ed",31:"dave",56:"ed",3:"marty",29:"ed"}
    print(reverse(myDict))
    
main()