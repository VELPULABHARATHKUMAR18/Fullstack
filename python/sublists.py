 # sum of sub lists is armstrong
# def arm(n):
#     t=n
#     s=0
#     dc=0
#     while t>0:
#         r=t%10
#         dc+=1
#         t//=10
#     t=n
#     while t>0:
#         r=n%10
#         s=s+(r**dc)
#         t//=10
#     if s==n:
#         return True
#     else:
#         return False
# l=[7,9,11,12,45]
# for i in range(0,len(l)):
#
#     for j in range(i,len(l)):
#         sum=0
#         for k in range(i,j+1):
#             # print(l[k],end=" ")
#             sum+=l[k]
#         if arm(sum):
#             print(sum)

# print all the subsets where sum is equal to key value:

l=list(map(int,input().split()))
key=int(input())
for i in range(0,len(l)):

    for j in range(i,len(l)):
        sum=0
        for k in range(i,j+1):
            sum+=l[k]
        # print(sum)
        if sum==key:
            print(sum)
