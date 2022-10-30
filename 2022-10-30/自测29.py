def swap_pairs(data):
    if len(data)%2!=0:
        for i in range(0,len(data)-2,2):
            data[i],data[i+1]=data[i+1],data[i]
    else:
        for i in range(0,len(data)-1,2):
            data[i],data[i+1]=data[i+1],data[i]

def main():
    data=["10","20","30","40","50"]
    swap_pairs(data)
    print(data)

main()