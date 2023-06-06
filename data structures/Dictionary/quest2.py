d = {1: 2, 3: 4, 5: 2, 6: 1, 7: 5}
# l1=[]
# for x in d:
l1 = list(d.keys())
l2 = list(d.values())
l = l1 + l2
print(l)
l = set(l1 + l2)
print(l)
