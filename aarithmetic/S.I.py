#  write  a  python script to calculate simple interest.
print("To calculate simple interest and amount")
principal = int(input("Enter a principal amount= "))
rate = int(input("Enter a  rate % = "))
time = int(input("Enter a time = "))
si = (principal * rate * time) / 100
print("Simple interest is = ", si)
amt = si + principal
print("Amount is = ", amt)
