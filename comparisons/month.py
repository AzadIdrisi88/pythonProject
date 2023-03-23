print("month name=")
x = int(input("month no="))
if x == 1:
    print("jan,31")
elif x == 2:
    y = int(input("year="))

    if y % 400 == 0:
        print("29")
    elif y % 4 == 0 and y % 100 != 0:
        print("feb,29")
    else:
        print("feb,28")
elif x == 3:
    print("mar,31")
elif x == 4:
    print("apr,30")
elif x == 5:
    print("may,31")
elif x == 6:
    print("jun,30")
elif x == 7:
    print("jul,31")
elif x == 8:
    print("aug,31")
elif x == 9:
    print("sep,30")
elif x == 10:
    print("oct,31")
elif x == 11:
    print("nov,30")
elif x == 12:
    print("dec,31")
else:
    print("invalid")
