# r=range(20)
# for i in r:
# print(i)
# r=range(20)
# for i in r:
#     print( i, end=",")
# print()
# r=range(15)
for i in range(1, 20, 2):
    print(i, end=",")
print()
for i in range(15, 0, -1):
    print(i, end=",")
print()
for i in reversed(range(1, 15)):
    print(i, end=",")
print()
for i in range(1, 15, 1):
    print(i * i, end=" , ")  # square of a no.
print()
for i in range(2, 11, 1):
    print(i * (i - 1), end=" , ")
print()
for i in range(1, 11):
    # print("1 /", i, end=" , ")
    print(1 / i, end=" , ")


