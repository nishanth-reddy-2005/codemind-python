def pair(n,arr):
    e=0
    o=0
    for i in range(n):
        if(arr[i]%2==0):
            o+=1
        else:
            e+=1
    if o%2==0 and e%2==0:
        return 1
    else:
        return 0
n=int(input())
li=list(map(int,input().split()))
print(pair(n,li))