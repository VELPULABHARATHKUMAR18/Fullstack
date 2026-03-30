# the product ans sum == input then spy

n=int(input())
sum=0
pro=1
while n>0:
    r=n%10
    sum+=r
    pro*=r
    n//=10
if sum==pro:
    print("spy")
else:
    print("Not Spy")