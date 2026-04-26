def arms(n):
    t=n
    sum=0
    dc=0
    while t>0:
        r=t%10
        dc+1
        t=t//10
    t=n
    while t>0:
        r=t%10
        sum=sum+r**dc
        t=t//10
    if sum==n:
        print("arm")
    else:
        print("Not a ARm")
