p = int(input("Physics\n"))
c = int(input("Chemistry\n"))
m = int(input("Maths\n"))
if p < 40 or c < 40 or m < 40:
    print("Fail")
else:
    total = (p + c + m)
    percent = total / 3
    print(total, percent)
    if percent < 50:
        print("3rd")
    elif percent < 60:
        print("2nd")
    else:
        print("1st")
