# def arms(n):
#     t=n
#     sum=0
#     dc=0
#     while t>0:
#         r=t%10
#         dc+1
#         t=t//10
#     t=n
#     while t>0:
#         r=t%10
#         sum=sum+r**dc
#         t=t//10
#     if sum==n:
#         print("arm")
#     else:
#         print("Not a ARm")


# n=int(input())
# v=[]
# a=0
# b=1
# v.append(a)
# v.append(b)
# for i in range(2,n+1):
#     c=a+b
#     v.append(c)
#     a=b
#     b=c
# for i in range(1,n+1):
#     if i not in v:
#         print(i,end=" ")


l=list(map(int,input().split()))
l.sort()
k=int(input())
lo=0
u=len(l)-1
for i in range(len(l)):
    mid=lo+u//2
    if l[mid]==k:
        print("Found")
        break
    elif l[mid]>k:
        u=mid-1
    elif l[mid]<k:
        lo=mid+1
else:
    print("Not Found")

