accounts={}
while True:
    print("0-Exit","1-Creating Account","3-Deposit","4-Withdraw","5-All")
    option=int(input())
    if option==0:
        break
    if option==1:
        data=int(input("Creating Account No.= "))
        name=input("Enter Holder Name= ")
        dpt=int(input("Enter Amount = "))
        accounts[data]={name,dpt}
        print(accounts)