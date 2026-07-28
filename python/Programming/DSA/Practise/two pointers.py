# # Reverse an array.
# s="kumar"
# res=""
# l=len(s)-1
#
# while l>=0:
#     res+=s[l]
#     l-=1
# print(res)

# # Check palindrome.
#
# l=[1,2,1,1]
# t=l.copy()
# le=0
# r=len(l)-1
# while le<r:
#     l[le],l[r]=l[r],l[le]
#     le+=1
#     r-=1
# if l==t:
#     print("palin")
# else:
#     print("not")

# Move zeros to end.

# l=[0,2,0,4,0,0,8,9,1]
# res=[]
# for i in l:
#     if i!=0:
#         res.append(i)
# while len(res)<len(l):
#     res.append(0)
# print(res)

# using two pointers:

# left=0
# for i in range(len(l)):
#     if l[i]!=0:
#         l[left],l[i]=l[i],l[left]
#         left+=1
# print(l)


# Find pair with target sum (sorted array).

# l=[1,2,4,6,8,9,15,48,50,52]
# target=10
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             print(l[i],l[j])

# le=0
# r=len(l)-1
# while le<r:
#     if l[le]+l[r]==target:
#         print(l[le],l[r])
#         le+=1
#         r-=1
#     elif l[le]+l[r]<target:
#         le+=1
#     else:
#         r-=1

# Remove duplicates.
# s="bharath"

# r=""
# for i in s:
#     if i not in r:
#         r+=i
# print(r)


# v=['a','e','i','o','u']
# s=list("bharath kumar velpula")
# r=""
# for i in s:
#     if i in v:
#         r+=i
# print(r[::-1])

# l=0
# r=len(s)-1
# while l<r and s[l] not in v:
#     l+=1
# while l<r and s[r] not in v:
#     r-=1
# s[l],s[r]=s[r],s[l]
# l+=1
# r-=1
# print("".join(s))

# Remove all occurrences of a given element.
# l=[5,2,10,5,8,5,2]
# ele=5
# r=[]
# for i in range(0,len(l)):
#     if l[i]!=ele:
#         r.append(l[i])
# print(r)


# Sort an array of 0s and 1s using two pointers.
# l=[0,1,1,0,1,0,0,1,1]
#
# le=0
# r=len(l)-1
# while le<r:
#     while le<r and l[le]==0:
#         le+=1
#     while le < r and l[r]==1:
#         r-=1
#     if le<r:
#         l[le],l[r]=l[r],l[le]
#         le+=1
#         r-=1
# print(l)


# Find the first pair with a given sum.

# l=[1,2,4,6,8,9,15,48,50,52]
# target=10
# le=0
# r=len(l)-1
# while le<r:
#     if l[le]+l[r]==target:
#         print(l[le],l[r])
#         break
#     elif l[le]+l[r]<target:
#         le+=1
#     else:
#         r-=1













