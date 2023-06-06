# create a list,sort it and remove duplicates and print it.

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 4, 4, 6, 6, 8, 6, 8, 9, 2, 1, 5, 6, 4]
l = sorted(set(l1))
print(l)

print()

# Find the product of all elements in a list.
product = 1
l2 = [1, 2, 3, 4]
for x in l2:
    product *= x
print(product)
