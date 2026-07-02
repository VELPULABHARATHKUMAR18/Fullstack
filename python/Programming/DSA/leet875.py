piles=list(map(int,input().split()))
h=int(input())
low=1
high=(max(piles))
while low<high:
    mid=(low+high)//2
    hrs=0
    for p in piles:
        hrs+=(p+mid-1)//mid
    if hrs<=h:
        high=mid
    else:
        low=mid+1
print(low)
