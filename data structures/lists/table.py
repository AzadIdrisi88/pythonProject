n = int(input())
l = []
for e in range(1, 11):
    l = l + [n * e]
print(l, end=" ")
print()
table = [i * n for i in range(1, 11)]
print(table)
