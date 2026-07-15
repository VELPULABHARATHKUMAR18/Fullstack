# l=list(map(int,input().split()))
# max=0
# for i in l:
#     if i>max:
#         max=i
# print(max)

# n=int(input())
#
# max=0
# while n>0:
#     r=n%10
#     if r>max:
#         max=r
#     n//=10
# print(max)

# l=list(map(int,input().split()))
# min=9
# for i in l:
#     if i<min:
#         min=i
# print(min)


# l=[10,2,31,50,2,38]
# sum=0
# for i in l:
#     sum+=i
# print(sum)

# Avg of an array
# sum=0
# c=0
# for i in l:
#     sum+=i
#     c+=1
# print(sum/c)

# count of even no:

# c=0
# for i in l:
#     if i%2!=0:
#         c+=1
# print(c,end=" ")

# Reverse an array manually.

# left=0
# right=len(l)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1
# print(l)

# Find the second largest element.
#

# l.sort()
# print(l[-2])

# for i in range(0,len(l)):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l[-2])

# Check whether an element exists (linear search).
# target=10
# for i in range(0,len(l)):
#     if l[i]==target:
#         print("found")
#         break
#     else:
#         print("Not")
#         break

# Find the index of a given element.
# target=10
# for i in range(0,len(l)):
#     if l[i]==target:
#         print(i)
#         break
# else:
#     print("Ele not found")

# Count how many times an element appears.

# l=[1,2,2,3,2,3]
# target = 2
# c=0
# for i in range(len(l)):
#     if l[i]==target:
#         c+=1
# print(c)


# Find the last occurrence of an element.
# for i in range(len(l)-1,-1,-1):
#     if l[i]==target:
#         print(i)
#         break


# Find the first occurrence of an element.

# for i in range(len(l)):
#     if l[i]==target:
#         print(i)
#         break

# Reverse a string without using built-in functions.
# s="harathb"
# res=''
# for i in range(len(s)-1,-1,-1):
#     res+=s[i]
# print(res)

# s="mabha"
# res=''
# for i in range(len(s)-1,-1,-1):
#     res+=s[i]
#     if s==res:
#         print("palindrome")
#         break
# else:
#     print("not")

# def palin(s):
#     res=''
#     for i in range(len(s)-1,-1,-1):
#         res+=s[i]
#     if s==res:
#         return "palin"
#     else:
#         return "not"
# s=(input())
# print(palin(s))

# Reverse a number.

# l=[1,2,34,6,5]
# z=[]
# for i in range(len(l)-1,-1,-1):
#     z.append(l[i])
# print(z)

# Check whether a number is a palindrome.
# def palin(l):
#     z=[]
#     for i in range(len(l)-1,-1,-1):
#         z.append(l[i])
#     if l==z:
#         return 'palin'
#     else:
#         return 'not'
# l=[1,2,1,1]
# print(palin(l))


# # Count vowels in a string.
#
# s='malayalam'
# s=s.lower()
# c=0
# vowels=["a",'e','i','o','u']
# for i in s:
#     if i in vowels:
#         c+=1
# print(c)


# Count consonants in a string
# s=input()
# c=0
# vowels=["a",'e','i','o','u']
# for i in s:
#     if i not in vowels:
#         c+=1
# print(c)

# Count frequency of each character.
# s='bharath'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d) with dictionary

# s='malayalam'
# for i in s:
#     c=0
#     for j in s:
#         if i==j:
#             c+=1
#     print(i,c)

# Move Zeros to the End
# l=[0,2,0,5,50,0,8,9,10,0,0]
# res=[]
# for i in l:
#     if i!=0:
#         res.append(i)
# while len(res)<len(l):
#     res.append(0)
# print(res)

# Move Zeros to the first
#
# l=[10,0,58,36,0,8,0,0]
# res=[]
# for i in l:
#     if i==0:
#         res.append(i)
# for i in l:
#     if i!=0:
#         res.append(i)
# print(res)


# Remove duplicates.
# l=[10,12,10,14,14,8,16,8]
# res=[]
# for i in l:
#     if i not in res:
#         res.append(i)
# print(res)


# Count the frequency of each element.

# l=[1,1,2,2,6,8,8,7,7,2]
# d={}
#
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)

# Check if an array is sorted.

# l=[10,15,45]
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         print("not sorted")
#         break
# else:
#     print("sorted")


# Find the missing number from 1 to n.

# to get the missing number we choose n= higest no and sum the number n=n*(n+1)//2 is expected ssum and actual sum is sum(arry) then substract the expected sum - actual sum

l=[1,2,3,4,5,6,8]
n=max(l)
expect=n*(n+1)//2
actual=0
for i in l:
    actual+=i
print(expect-actual)
