l=[[10,20],[3,40]]
print(l[0][1])
l[1][0]=55
print(l)


# to axis all the elements from the inner list
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        print(l[i][j])


# to create inner lists if rows and columns are given

# l=[]
# r=int(input())
# c=int(input())
# for i in range(0,r):
#     rl=[]
#     for j in range(c):
#         ele=int(input())
#         rl.append(ele)
#     l.append(rl)
# print(l)

# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# print(l)

# WAp to take dynamic inputs from the user for inner list and print even nos from the inner list
# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# for z in l:
#     for i in z:
#         if i%2==0:
#             print(i)

# sum of each row in the innerlist
# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# for j in l:
#     print(sum(j))

#             or
# for i in range(0,len(l)):
#     print(sum(l[i]))



# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# ma=l[0][0]
# ma=0
# for i in range(len(l)):
#     for j in range(len(l[i])):
#
#         if l[i][j]>ma:
#             ma=l[i][j]

# or
# for j in l:
#     for k in j:
#         if k>ma:
#             ma=k
# print(ma)



y



