def is_unique(dict):
    list_value=list(dict.values())
    for i in range(0,len(list_value)):
        for j in range(i+1,len(list_value)):
            if list_value[i]==list_value[j]:
                return False
    return True

def main():
    dict1={"marty":"stepp","stuart":"reges","jessica":"wolk","allison":"obourn","hal":"perkins"}
    print(is_unique(dict1))
    dict2={"kendrick":"perkins","stuart":"reges","jessica":"wolk","bruce":"reges","hal":"perkins"}
    print(is_unique(dict2))
    
main()
    
    