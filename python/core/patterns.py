
# n=int(input())
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

n=10
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("*",end=" ")
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()




#
# n=int(input())
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     for k in range(1,n-i+1):
#         print(" ",end=" ")
#     for l in range(n-i):
#         print(" ",end=" ")
#     for m in range(i):
#         print("*",end=" ")
#     print()
#
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print("*",end=" ")
#     for k in range(1,i+1):
#         print(" ",end=" ")
#     for l in range(i):
#         print(" ",end=" ")
#     for m in range(n-i):
#         print("*",end=" ")
#     print()