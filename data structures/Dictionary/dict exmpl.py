d = {}
print(d, type(d))
d[1] = "one"
d[2] = 'two'
print(d)
d1 = {1: "bird", 2: "lion", 3: "fish"}
print(d1)
print(d1[3])
d1[4] = "cat"
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())

for key in d1.items():
    print(key)

for key, value in d1.items():
    print(key, value)
