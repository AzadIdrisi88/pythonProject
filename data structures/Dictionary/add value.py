d = {}
while True:
    print("0-Exit", "1-item")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        key = input("enter a key= ")
        value = input("enter a value= ")
        d[key] = value
        continue
    if option == 2:
        print(d)
        continue
    print("invalid")
