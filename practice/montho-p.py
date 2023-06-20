x=int(input("Enter month no.= "))
if x==1:
    print("January ,31 days")
elif x==2:
    y=int(input("Enter a Year="))
    if y%400==0:
        print("February , 29 days")
    elif y%4==0 and y%100 !=0:
        print("February , 29 days")
    else:
        print("February , 28 days")
elif x==3:
    print("March , 31 days")
elif x==4:
    print("April , 30 days")
elif x==5:
    print("May , 31 days")
elif x==6:
    print("June , 30 days")
elif x==7:
    print("July , 31 days")
elif x==8:
    print("August , 31 days")
elif x==9:
    print("September , 30 days")
elif x==10:
    print("October , 31 days")
elif x==11:
    print("Novenber , 30 days")
elif x==12:
    print("December , 31 days")
else:
    print("Invalid Month")        


