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

# l=list(map(int,input().split()))
# key=int(input())
# for i in range(0,len(l)):
#
#     for j in range(i,len(l)):
#         sum=0
#         for k in range(i,j+1):
#             print(l[k],end=" ")
#         print()
#             sum+=l[k]
#         print(sum)
#         if sum==key:
#             print(l[i:j+1])


# subarrays whose sum ==key value

l = [1, 4, 6, 12, 10, 2, 4, 8]
key = 12
found=False

c=0
for i in range(len(l)):
    s = 0
    for j in range(i, len(l)):
        s += l[j]

        if s == key:
            c+=1

            print(c)
            found=True

if not found:
    print("Not Found")


# print of subarray whose sum is palindrome or not
# def palin(n):
#
#     return str(n) == str(n)[::-1]
# l=[20,20,30,15,33,10,5,45,88,10]
# c=0
# for i in range(0,len(l)):
#     s=0
#     for j in range(i,len(l)):
#         s+=l[j]
#
#         if palin(s):
#             c+=1
#             print(s)
#             print(l[i:j+1])
# if c==0:
#     print("Not")





 ps=0
 c=0
 pre={}
 pre[0]=1
 for i in range(0,len(l)):
     ps+=l[i]
     ch=ps-key
     c=c+pre.get(ch,0)
    pre[ps]=pre.get(ps.0)+1
 return c

