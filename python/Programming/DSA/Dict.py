# finding frequency of list using dict

l=[10,20,30,10,30,20,40]
# c=0
d={}
# for i in range(0,len(l)):
#     if l[i] in d:
#         c=d[l[i]]
#         d[l[i]]=c+1
#
#     else:
#         d[l[i]]=1
# print(d)
#
# def palin(n):
#     rev=0
#     t=n
#     while n>0:
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     if rev==t:
#         print("True")
#     else:
#         return("False")
# n=int(input())
# b=palin(n)

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# DSA problem 131 rverse string

# def revstring(n):
#     l=0
#     r=len(n)-1
#     while l<r:
#         n[l],n[r]=n[r],n[l]
#         l+=1
#         r-=1
#     return n
# n=list(input())
# b=revstring(n)
# print(b)

# 151
# def reverse(s):
#
#     s=s.split()
#     z=s[::-1]
#     return(" ".join(z))
# s=input()
# b=reverse(s)
# print(b)


# n=input()
#
# z=n[::-1]
# z=z.split()
# print(" ".join(z))

n=list(map(int,input().split()))
key=input()
for i in range(0,len(n)):
    for j in range(i,len(n)):
        sum=0
        for k in range(i,j+1):
            # print(n[k],end="")
            z=sum+=n[k]
if z==key:
    print(l[k])






