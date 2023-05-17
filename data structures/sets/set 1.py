s1 = set([1, 2, 3, 4, 5, 6])
s2 = {1, 2, 3, 4, 5, 6, 7}
print(s1, s2)
print(type(s1), type(s2))
s1.add(8)
print(s1)
s1.update([1, 2, 3, 4, 5, 6, 7, 2, 4, 5, 5, 6, 7, 7, 8, 8])
print(s1)
s1.remove(8)
print(s1)
s1.discard(2)
print(s1)
s1.clear()
print(s1)
cricketers = {"A", "C"}
footballers = {"B", "C"}
u = cricketers.union(footballers)
print("union=", u)
u = cricketers.copy()
u.update(footballers)
print("union=", u)
i = cricketers.intersection(footballers)
print("intersection=", i)
i = cricketers.copy()
i &= footballers
print("intersection", i)
diff = cricketers.difference(footballers)
print("difference", diff)
diff = cricketers - footballers
print("difference", diff)
symmdiff = cricketers.symmetric_difference(footballers)
print("symmetric difference=", symmdiff)
symmdiff = cricketers.copy()
symmdiff ^= footballers
print("symmetric difference=", symmdiff)

print()

a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
print("subset=", a.issubset(b))
print("subset=", a <= b)
print("subset=", b.issubset(a))
print("subset=", b <= a)

print()
print("superset=", a.issuperset(b))
print("superset=", a >= b)
print("superset=", b.issuperset(a))
print("superset=", b >= a)

print()

a = {1, 2}
b = {2, 3}
c = {3, 4}
print("disjoint", a.isdisjoint(b))
print("disjoint", a.isdisjoint(c))

print()

a = {1, 2}
b = {2, 3}
c = {3, 4}
d = a.copy()
d.intersection_update(b)
print("intersection update=", d)
d = a.copy()
d.difference_update(b)
print("difference update=", d)
d = a.copy()
d.symmetric_difference_update(b)
print("symmetric difference update=", d)
