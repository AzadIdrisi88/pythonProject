# range takes 3 inputs start, end and step. start is 0 be default, step is 1 and end needs to be given
# Loop runs up to n-1
r = range(11)
for i in r:
    print(i, end=",")
print()
for i in range(1, 11):
    print(i, end=",")
print()
for i in range(1, 11, 5):
    print(i, end=",")

# Negative step
print()
for i in range(10, 0, -1):
    print(i, end=",")
print()
for i in reversed(range(1, 11)):
    print(i, end=",")
