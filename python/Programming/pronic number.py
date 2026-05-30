# product of two consecutive integers equal to input value.
n=int(input())
c=0
for i in range(1,n+1):
    if i*(i+1)==n:
        c+=1
if c==1:
    print("Pronic no")
else:
    print("Not Pronic")