a = [10, 2, 3, 4, 5, 6, 7, 8]


def f(x):
    # print(x)
    if x % 2 == 0:
        return 0
    else:
        return 1


print(a)
a.sort(key=f)
print(a)
