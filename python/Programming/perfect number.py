# factors of given is equal to input then perfect
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
#         print(i)
# print(sum)
if sum==n:
    print("Perfect No")
else:
    print("Not a perfect No")


n=int(input())
