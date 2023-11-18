a = [1, 2, 3]
print(a)
print(a[0])
print(a[-2])
n = len(a)
print(n)
#
a = [1, 2, 3, 4, 5, 6, ]
print(a)
print(a[0])
print(a[-3])
n = len(a)
print(n)
#
l = []
print(l)
print(type(l))
#
l = [1, 2, 3, 4, 5]
print(l)
#
l = list()
print(l)
#
l = list([1, 2, 3, 4])
#  0  1  2  3
# -4 -3 -2 -1
print(l)
n = len(l)
print(n)
print(l[0], l[2], l[3])
print()

for i in range(n):
    print(l[i], "=", l[-n + i])
print()

l = [1, "two", 3, "four", 5]
print(l)
for x in l:
    print(x)
n = len(l)
for i in range(n):
    print("l[", i, "]=", l[i], end="  ", sep="")
print()
l = [1, 2, 3, 4, 5, 7, 8, 9, 6, 5]
print("min value", min(l))
print("max value", max(l))

l = [0, 1, "two", 3, "four", 5]
print("1 to 3", l[1:4])
print("1 to end", l[1:])
print("Beginning to 3", l[:4])
print("complete Array", l[:])
