# max number of k_sum pairs

l=[1,4,6,10,2,6,8]
k=12
le=0
r=len(l)-1
l.sort()
c=0
while le<r:
    c_sum=l[le]+l[r]
    if c_sum==k:
        c+=1
        le+=1
        r-=1
    elif c_sum<k:
        le+=1
    else:
        r-=1
print(c)


