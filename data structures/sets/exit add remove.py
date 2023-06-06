s1 = {1, 2, 3, 4}
while True:
    print("0-Exit,1-Add,2-Show,3-remove,4-discard,5-update")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        n = int(input("Enter value\n"))
        s1.add(n)
        continue
    if option == 2:
        print(s1)
        continue
    if option == 3:
        n = int(input("enter removal value\n"))
        s1.remove(n)
        continue
    if option == 4:
        n = int(input("enter discard value\n"))
        s1.discard(n)
        continue
    # if option==5:
    #     n=int(input("enter to update value\n"))
    #     s1.update(n)
    #     continue
    print("Invalid option")
