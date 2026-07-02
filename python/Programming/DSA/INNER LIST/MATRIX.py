# # TO PRINT MATRIX BASED ON ROWS AND COLUMNS
#
# l=[]
# r=int(input("enter row"))
# c=int(input("enter col"))
# for i in range(r):
#     rl=[]
#     for j in range(c):
#         ele=int(input("enter ele"))
#         rl.append(ele)
#     l.append(rl)
# print(l)
from dateutil.tz.win import valuestodict

# to print ony row values
# l=[]
# r=int(input())
# for i in range(r):
#     l.append(int(input()))
# print(l)

# to print only column values

l=[10,2,3,50]
k=10
for i in l:
    r=i%k
    print(r)
    i//=10

