# write a python script to remove a last digit of a given number.
n = int(input("Enter  a number =  "))
if n >= 0:
    n = n // 10
    print("After removing the last digit the number is = ", n)
else:
    n = -(n // -10)
    print("After removing the last digit the number is = ", n)
