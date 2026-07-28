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

# s="malayalam"
# res=''
# for i in range(len(s)-1,-1,-1):
#     res+=s[i]
# if res==s:
#     print("palin")
# else:
#     print("Not")

# Count special characters.
# s="Bha#Ra!tH@"
# c=0
# for i in range(0,len(s)):
#     if "a"<=s[i]<="z" or "A"<=s[i]<="Z":
#        pass
#     else:
#         c+=1
# print(c)

# character frequency
# s="Bharath"
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# Reverse each word in a sentence.
# s="hii howwe are yous"
# s=s.split()
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end=" ")

# largest word in the sentence
# s=s.split(" ")
# largest=s[0]
# for i in s:
#     if len(i)>len(largest):
#         largest=i
# print(largest)


#  non-repeating character if you want only first element then add break
s="Bharathb"
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for i in s:
#     if d[i]==1:
#         print(i)


# First repeating character
# s=s.lower()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for i in s:
#     if d[i]>1:
#         print(i)
#         break

def maxsum(l):
    dp=[-1]*len(l)
    dp[0]=l[0]
    dp[1]=max(l[0],l[1])
    for i in range(2,len(l)):
        p=l[i]+dp[i-2]
        np=dp[i-1]
        dp[i]=max
