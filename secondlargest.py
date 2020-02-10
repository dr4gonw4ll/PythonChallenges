def letsort(li):
    temp=0;
    for i in range(0,len(li)):
        for j in range(i,len(li)):
            if(li[i]<=li[j]):
                temp=li[j]
                li[j]=li[i]
                li[i]=temp
    return(l);


if __name__ == '__main__':
    n = int(input())
    arr = map(int,input().split())
    l = list(arr)
    li1 = letsort(l)
    max = li1[0];
    ar = map(lambda x:x-max,li1)
    newar = list(ar)
    for k in range(0,len(newar)):
        if(newar[k]!=0):
            print(newar[k]+max)
            break
