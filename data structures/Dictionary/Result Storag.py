# result={1:[1,"Popat",77,88,99],2:[2,"John",77,88,99]}
result = {}
while True:
    print("0-Exit", "1-To Add Data", "2-Show By Roll No.", "3-To Correction ", "4-To Remove,5-All")
    option = int(input())
    if option == 0:
        break

    if option == 1:
        # key = int(input("enter key="))
        roll = int(input("Enter roll no.= "))
        if result.get(roll) is not None:
            print("Already Exist Candidate")
        else:
                name = input("Candidate Name = ")
                marks1 = int(input("English Marks= "))
                marks2 = int(input("Hindi Marks= "))
                marks3 = int(input("Maths Marks= "))

                result[roll] = [roll, name, marks1, marks2, marks3]
                print(result)
        continue

    if option == 2:
        roll = int(input("Enter Candidate Roll No = "))
        data = result.get(roll)
        print(data)
        continue
    if option == 3:

        roll = int(input("Correction Roll No.= "))
        if result.get(roll) is  None:
            print("Not found")
        else:
            name = input("Candidate Name = ")
            marks1 = int(input("English Marks= "))
            marks2 = int(input("Hindi Marks= "))
            marks3 = int(input("Maths Marks= "))

            result[roll] = [roll, name, marks1, marks2, marks3]
            print(result)
        continue
    if option == 4:
        roll = int(input("Remove Candidate Roll No.="))
        if result.get(roll) is None:
            print("Not found")
        else:
            remove = result.pop(roll)
            print("Removed", remove)
        continue
    if option == 5:
        print(result)
        continue

    print("Invalid Key")
