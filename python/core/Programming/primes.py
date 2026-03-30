
# next prime
#
# def prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     else:
#         return False
# n=int(input())
# i=n+1
# while True:
#     if prime(i):
#         print(i)
#         break
#     i=i+1

# before prime

# def prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     else:
#         return False
# n=int(input())
# i=n-1
# while True:
#     b=prime(i)
#     if b==True:
#         print(i)
#         break
#     i-=1


# n=int(input())
# c=0
# for i in range(1,n+1):
#     if i*(i+1)==n:
#         c+=1
# if c==1:
#         print("pronic")
# else:
#     print("not")

# Nereast Prime
#
def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False
n=int(input())
if n<=0:
    print("InValid Input")
else:
    ap=0
    i=n+1
    while True:
        b=prime(i)
        if b==True:
            ap=i
            break
        i+=1
    bp=0
    q=n-i
    while True:
        b=prime(i)
        if b==True:
            bp=i
            break
        q-=1
    ad=ap-n
    bd=n-bp
    if ad==bd:
        print(ap,bp)
    elif ad<bd:
        print(ap)
    else:
        print(bp)