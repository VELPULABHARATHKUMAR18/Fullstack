 #Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
#filter() to keep only the keys whose values are greater than 50

d = {"apple": 100, "banana": 40, "cherry": 150}
print(d.keys())
print(d.values())
print(d.items())
d1=dict(filter(lambda x:x[1]>50,d.items()))
print(d1)