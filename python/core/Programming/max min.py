# max number

# n=int(input())
# t=n
# min=0
# while t>0:
#     r=t%10
#     if r>min:
#         min=r
#
#     t=t//10
# print(min)
#
# # n=int(input())
# t=n
# max=9
# while t>0:
#     r=t%10
#     if r<max:
#         max=r
#     t=t//10
# print(max)

# sum of even digits

# n=int(input())
# sum=0
# c=0
# while n>0:
#     r=n%10
#     if r%2==0:
#         sum+=r
#
#     n=n//10
# print(sum)


# perfect square:

# n=int(input())
# for i in range(1,n):
#     if i*i==n:
#         print("perfect")
#         break
# else:
#     print("Not a perfect square")

# n natural numbers:

# n=int(input())
# for i in range(1,n+1):
#     print(i)

def prime(n):
    fc=0
    for i in range(1,n+1):
        fc+=1
    if fc==2:
        return True
    else:
        return False

n=int(input())
c=0
i=2
while True:
    if prime(i):
        c+=1
        if c==n:
            print(i)
            break
    i=i+1

# def prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     else:
#         return False
#
# n=int(input())
# c=0
# i=2
# while True:
#     if prime(i):
#         c=c+1
#         if c==n:
#             print(i)
#             break
#     i+=1