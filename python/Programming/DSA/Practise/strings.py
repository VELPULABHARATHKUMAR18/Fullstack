# s="Bharath i Kumar"
# c=0
#
# for i in s:
#     c+=1
# print(c)

# count vowels:
# l=['a','e','i','o','u']
# s=s.lower()
# c=0
# for i in s:
#     if i not in l:
#         c+=1
# print(c)

# count of uppercase and lowercase
# lc=0
# c=0
# for i in s:
#     if 'A'<=i<='Z':
#         c+=1
#     elif 'a'<=i<='z':
#         lc+=1
# print(c)
# print(lc)


# Count digits.
# dc=0
# s="bha8854t25th kuma5654r"
# res=[]
# for i in s:
#     if '0'<=i<='9':
#         res.append(int(i))
# print(sum(res))

#
#
# s="Hahrath"
# s=list(s)
# left=0
# right=len(s)-1
# while left<right:
#     s[left],s[right]=s[right],s[left]
#     left+=1
#     right-=1
# s="".join(s)
# print(s)

s="Bharath"
res=''
for i in range(len(s)-1,-1,-1):
    res+=i
if res==s:
    print("palin")




