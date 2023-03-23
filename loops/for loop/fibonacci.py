# 0,1, 1, 2, 3  5, 8,  13, 21, 34
"""
a   b   c
0   1   1
1   1   2
1   2   3
2   3   5

"""
a, b = 0, 1
n = 10
print(a, b,end=" ")
for i in range(3, n +1):
    c = a + b
    a = b
    b = c
    print(c, end=" ")
