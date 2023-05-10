n = 5
mid = (n + 1)//2

for row in range(1, n + 1):
    for col in range(1, n + 1):
        condition = not row+col==n+1 and not row==col
        if condition:
            print(" 0 ", end="")
        else:
            print("   ", end="")
    print()
