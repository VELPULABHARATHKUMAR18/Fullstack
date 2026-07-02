s= "four two one triple three double four six zero"
l=list(s.split())
d={1:"one",2:"two",3:"three",4:"four",0:"zero",6:"six"}
# for i in l:
#     i=i.lower()
#     if i=="double":
#         p=l[l.index(i)+1].lower()
#         for key, value in d.items():
#             if p == value:
#                 print(key, end="")
#     elif i=="triple":
#         p=l[l.index(i)+1].lower()
#         for key, value in d.items():
#             if p == value:
#                 print(key, end="")
#                 print(key,end="")
#     else:
#         for key, value in d.items():
#             if i==value:
#                 print(key,end="")


# s="nine zero one double zero six seven triple six zero"
# l=s.split()
# d={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
# for i in range(0,len(l)):
#     if l[i]=="double":
#         print(d[l[i+1]],end="")
#     elif l[i]=="triple":
#         print(d[l[i+1]],end="")
#         print(d[l[i+1]], end="")
#     else:
#         print(d[l[i]],end="")


# s="bdg"
# d={"abc":2,"def":3,"ghi":4,"jkl":5,"mno":6,"pqrs":7,"tuv":8,"wxyz":9}
# sum=0
# for i in range(0,len(s)):
#     for key,values in d.items():
#         if s[i] in key:
#             sum+=values
# print(sum)




# s=" triple nine zero one double zero six seven triple six zero"
# d={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
# s=s.split()
# for i in range(0,len(s)):
#     if s[i]=="double":
#         print(d[s[i+1]],end="")
#     elif s[i]=="triple":
#         print(d[s[i+1]],end="")
#         print(d[s[i+1]],end="")
#     else:
#         print(d[s[i]],end="")


# s="qaz"
# s=s.lower()
# a="qwertyuiop"
# b="asdfghjkl"
# c="zxcvbnm"
# c1=0
# c2=0
# c3=0
# for i in range(len(s)):
#     if s[i] in a:
#         c1+=1
#     elif s[i] in b:
#         c2+=1
#     elif s[i] in c:
#         c3+=1
# if c1==len(s):
#     print("True")
# elif c2==len(s):
#     print("True")
# elif c3==len(s):
#     print("True")
# else:
#     print("False")



