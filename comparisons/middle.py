print("find the middle no=")
# print(type("987"))
# print(type(8765))
# print(type(0.8))
x = int(input("x="))
y = int(input("y="))
z = int(input("z="))
if y <= x <= z or z <= x <= y:
    mid = x
elif y >= x and y <= z or y >= z and y <= x:
    mid = y
else:
    mid = z
print("mid", mid)
