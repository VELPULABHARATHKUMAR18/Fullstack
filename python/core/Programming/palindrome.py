n=int(input())
t=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==t:
    print(rev)
else:
    print("Not a plain")


# # usinf function
#
# def palin(n):
#     t=n
#     rev=0
#     while n>0:
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     if rev==t:
#         print("Palin")
#     else:
#         print("not a palin")
# s=int(input)
# r=palin(s)
