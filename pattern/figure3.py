n=5
h = 2*n-1
for i in range(1,n-1):
    for j in range(1,i+1):
        print("0",end="")
    for k in range(1,h-2*i+1):
            print(" ",end="")
    for j in range(1,i+1):
        print("0",end="")
    print()