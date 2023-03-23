print("input length of the triangle is=")
x = int(input("x="))
y = int(input("y="))
z = int(input("z="))
# if x == y == z:
#     print("equilateral triangle")
# elif x == y or y == z or z == x:
#     print("isosceles triangle")
# else:
#     print("scalene triangle ")

count = 0
if x == y:
    count += 1
if x == z:
    count += 1
if y == z:
    count += 1
print(count)
if count == 3:
    print("Equilateral")
elif count == 1:
    print("Isosceles")
else:
    print("Scalene")
