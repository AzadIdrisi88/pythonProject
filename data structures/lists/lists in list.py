a = [[1, 2, 2023], [5, 6, 4], [8, 7, 6], [9, 6, 4]]


def total(l):
    return -sum(l)


a.sort(key=total)

print(a)
# Write a program that takes as input a list of dates and then sorts

b = [[2, 4, 2020], [5, 4, 2023], [7, 4, 2017], [4, 2, 2021]]
def total(l):
    return sum(l)


a.sort(key=total)

print(b)
