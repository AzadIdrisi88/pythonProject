# Find the common elements common in a list a1=[1,2,3],b=[2,3,4],commmon=[2,3,]
l1 = [1, 2, 3]
l2 = [3,4,5]
s1 = set(l1)
print(s1)
s2 = set(l2)
print(s2)
inter = list(s1.intersection(s2))
print(inter)
