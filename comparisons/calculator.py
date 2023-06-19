n1 = int(input("Enter First Number= "))
operators = input("Select the Operator + ,- , * ,/, ** ")
n2 = int(input("Enter Second Number= "))
if operators == "+":
    print("Addition is ", n1 + n2)
elif operators == "-":
    print("Substraction is ", n1 - n2)
elif operators == "*":
    print("Multiplication is ", n1 * n2)
elif operators == "/":
    print("Division is ", n1 / n2)
elif operators == "**":
    print("Square is ", n1 ** n2)


else:
    print("Invalid Operator")
