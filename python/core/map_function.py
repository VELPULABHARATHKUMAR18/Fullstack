#  Use map() with a lambda to add 5 to every element of the following nested
#list [[1, 2], [3, 4], [5, 6]]

l=[[1,2],[3,4],[5,6]]

k=list(map(lambda x:x+[5],l))
print(k)