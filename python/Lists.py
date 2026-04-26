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


