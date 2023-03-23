# if False:
#     print(1)
#     print(2)
# else:
#     print(3)
#     print(4)
# a, b = 5, 0
# if a >= b:
#     # print("if")
#     max = a
# else:
#     # print("else")
#     max = b
# print(max)

# if a > b and a > c:  # if else ladder
#     max = a
#     # print("a")
# elif b > c:
#     max = b
#     # print("b")
# else:
#     # print("c")
#     max = c
#
# print(max)
a, b, c = int(input("A = ")), int(input("B = ")), int(input("C = "))
if a < b:
    if a < c:
        less = a
    else:
        less = c
else:
    if b < c:
        less = b
    else:
        less = c

if a < c:
    if b > c:
        high = b
    else:
        high = c
else:
    high = a
mid = a + b + c - high - less
print("Less", less)
print("High", high)
print("Mid", mid)
