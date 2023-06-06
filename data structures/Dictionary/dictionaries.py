# d=dict()
d = {}
d=dict()
print(d)
print(type(d))
print(d)
d["one"] = 1
print(d)
print(d["one"])
d = {"UP": "Lucknow", "Bihar": "Patna"}
print(d)
print(d["UP"])
print(d.keys())
print(d.values())
print(d.items())
for key, value in d.items():
    print(key, value)
d["UP"] = 90
print(d)
print(d.get("UP"))
print(d.get("UPP"))
print(d.get("UP", "Not Found"))
print(d.get("UPP", "Not Found"))
d.pop("UP")
d.
print(d)
d.clear()
print(d)

