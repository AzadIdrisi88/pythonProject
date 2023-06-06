accounts = {}
while True:
    print("0-Exit", "1-Create Account ", "2-Deposit", "3-Withdraw", "4-All")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        data = int(input("Create Account No.= "))
        if accounts.get(data) is not None:
            print("Account already exists")
        else:

            Holder = input("Enter Account Holder Name= ")
            dp = int(input("Enter Amount= "))

            if dp <= 0:
                print("not accepted")

            else:

                accounts[data] = [Holder, dp]

                print(accounts)
        continue
    if option == 2:
        data = int(input("Enter Account No.= "))
        account = accounts.get(data)
        if account is None:
            print("Account Not Exist")
        else:
            amt = int(input("Enter Deposit Amount= "))
            if amt <= 0:
                print("not accepted")
            else:
                totalamount = account[1] + amt
                account[1] = totalamount
                print(account)
        continue
    if option == 3:
        data = int(input("Enter Account No.= "))
        account = accounts.get(data)
        if account is None:
            print("Account Not Exist")
        else:
            widra = int(input("Enter Withdrawal Amount= "))

            if widra > account[1] or widra <= 0:
                print("Insufficient Balance")
            else:
                remainamount = account[1] - widra
                account[1] = remainamount
        continue

    if option == 4:
        print(accounts)
        continue
    print("invalid Selection")
    print("Please Select Right Option")
