# list is mutable object we add and upadte the list:
# list is used to store multiple objects in a single variable



# l=[1,2,30,40,5,10,5]
# l.extend(list(map(int,input().split(","))))
# print(l)

# list=[10,20,30,40]
# list.insert(1,30)
# print(list)


# # append method :
# l=[]
# l.append(50)
# l.append(120)
# print(l)

# printing index values

# l=[10,20,30,40]
# for i in range(0,len(l)):
#     print(l[2])
# l.extend([50,6,8,10])
# print(l)
# l.remove(10)
# print(l)
# print(l.index(50))
# print(l)
# l.pop(5)
# print(l)
# l.extend([10,10,20])
# print(l)
# print(l.count(10))
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.clear()
# print(l)
# l.append(50)
# print(l)
# l.extend([10,20,50,60])
# print(l)
# l1=l.copy()
# print(l1)
# l1.append(30)
# print(l)



# n=int(input())
# l=[]
# for i in range(0,n):
#     l.append(int(input()))
# for i in l:
#     if i%2==0:
#         print(i)


# def x(arr,k):
#     for i in arr:
#         for j in arr:
#             if arr.index(i)!=arr.index(j):
#                 if i+j==k:
#                     print([i,j])
# x([1,2,3,4,5],6)

# def x(arr):
#     l=[]
#     for i in arr:
#         l.append(int(str(i)[::-1]))
#     l=l[::-1]
#     print(l)
# x([11,12,13,14,15])

# def x(l):
#     x=[]
#     v=[]
#     for i in l:
#         x.append(l.count(i))
#     m=max(x)
#     for i in l:
#         if l.count(i)==m and i not in v:
#             v.append(i)
#     print(*v)
#     print(max(v))
# x([5,10,15,10,15,25,25,10,25,5,5])


# l=list(map(int,input().split()))
# for i in l:
#     print(i)

# l=list(map(int,input().split()))
# l.insert(3,4)
# print(l)


# l=list(map(int,input().split()))
# l2=list(map(int,input().split()))
# print(l+l2)


# l.remove(5)
# print(l)

# l.pop(8)
# print(l)


# print(l.index(6))

# l1=[1,2,3,3,8,5,4,1,3,6,3,]
# key=8
# c=0
# # print(l1.count(3))
# for i in l1:
#     if l1[i]==key:
#         c+=1
# print(c)

# l=[10,20,30,10,5,62]
# for i in l:
#     ad=l[0]+l[-1]
# print(ad)

# l=[10,20,30,40,50]
# sum=0
# c=0
# for i in l:
#     sum+=i
#     c+=1
#     z=sum/c
# print(z)

# def prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     else:
#         return False
# l=[1,2,7,9]

# for i in l:
#     if prime(i):
#         print(i)

# for k in l:
#     i=k+1
#     while True:
#         if prime(i):
#             print(i)
#             break
#         k+=1

# for i in range(len(l)-1,-1,-1):
#     print(l[i])

# l=[10,5,3,5,15,10,1,17]

# key=20
# for i in range(0,len(l)-1):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==key:
#             print(l[i],l[j])

# l=list(set(l))
# n=8
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l[-n])

# max=0
# for i in range(len(l)):
#     if l[i]>max:
#         max=l[i]
# print(max)


# min=9
# for i in range(len(l)):
#     if l[i]<min:
#         min=l[i]
# print(min)
# key=5
# for i in l:
#     if i==key:
#         print(key)
#     else:
#        print("not found")

# def fact(n):
#     sum=1
#     for i in range(n,0,-1):
#         sum*=i
#     return sum
# l=[2,6,7,5,10]
# for i in l:
#     print(fact(i))
# l=[10,2,0,4,8,9,45,8,10,10]
# key=int(input())
# l.sort()
# lo=0
# v=len(l)-1
# f=False
# while lo<=v:
#     mid=(lo+v)//2
#     if l[mid]==key:
#         print("Found")
#         f=True
#         break
#     elif l[mid]<key:
#         lo=mid+1
#     else:
#         v=mid-1
# if key not in l:
#     print("Not found")
# l2=[]
# for i in range(len(l)):
#     if l[i]==key:
#         l2.append(i)
# print(l2)

# def prime(n):
#     fc=0
#     for i in range(1,101):
#         if n%i==0:
#             fc+=1
#     if fc%2==0:
#         return True
#     else:
#         return False
# for i in range(1,101):
#     if prime(i):
#         print()


# Rotation

# l=list(map(int,input().split()))
# for i in range(0,len(l)):
#     t=l[0]
#     for j in range(0,len(l)-1):
#         l[j]=l[j+1]
#     l[len(l)-1]=t
#     print(l)


# anti clock wise

# l=list(map(int,input().split()))
# for i in range(len(l)):
#     t=l[len(l)-1]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=t
#     print(l)

# sub lists
#
# l=[10,20,30,40]
# for i in range(0,len(l)):
#     for j in range(i,len(l)):
#         for k in range(i,j+1):
#             print(l[k])
#     print()
#
# l=[10,20,30,40,50]
# key=4
# for i in range(len(l)):
#     t=l[len(l)-2]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#
#     l[len(l)-2]=t
# print(l)

# def prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     else:
#         return False
def arm(n):
    t=n
    s=0
    dc=0
    while t>0:
        r=t%10
        dc+=1
        t//=10
    t=n
    while t>0:
        r=n%10
        s=s+(r**dc)
        t//=10
    if s==n:
        return True
    else:
        return False
l=[7,9,11,12,45]
for i in range(0,len(l)):

    for j in range(i,len(l)):
        sum=0
        for k in range(i,j+1):
            # print(l[k],end=" ")
            sum+=l[k]
        if arm(sum):
            print(sum)


# l=list(map(int,input().split()))
# k=int(input())
# k=k%len(l)
# print(l[k:]+l[:k])
# print(l[-k:]+l[:-k])


