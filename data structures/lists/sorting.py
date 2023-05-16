# a = [4, 6, 9, 1, 0, 8, 5, 2]
# a.sort()
# print(a)
# print()
# a.sort(reverse=True)
# print(a)
# print()
# a = ["cat", "dog", "ball", "apple", "car"]
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# print()
#
# a = ["cat", "dog", "ball", "apple", "car"]
# sortedarray = sorted(a)
# print(sortedarray)
# print(a)
# print()
# reversesortedarray = sorted(a, reverse=True)
# print("reverse array =  ", reversesortedarray)
# print()
#
# a = ["cannnnnt", "dog", "ball", "apple", "car"]
# a.sort(key=len)
# print(a)
# a.sort(key=len, reverse=True)
# print(a)
# print()
#

# def f(s):
#     return s[-1]
# a.sort(key=f)
# print(a)
def f(s):
    print(s)
    return s[0]
a = ["ball", "cat", "apple"]
print(a)
a.sort(key=f)
print(a)

# Using lambda
a.sort(key=lambda x:x[len(x) - 1], reverse=True)  # Sorting by last character and reverse
print(a)

def mycompare(a, b):
    # Return -ve if a<b , 0 if a==b and +ve if a>b
    # This will sort in reverse order
    return b - a


a = [1, 2, 3, 4, 5]
a.sort(key=mycompare)
print(a)
# The same thing using lambda
a = [1, 2, 3, 4, 5]
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)
# Generate a random array and sort it
from numpy import random

a = list(random.randint(100, size=10))
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)
# Another way of doing the same thing
a = [random.randint(100) for x in range(10)]
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)


