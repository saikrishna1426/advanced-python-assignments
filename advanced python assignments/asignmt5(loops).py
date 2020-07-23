print("simple calculator")
while True :
    print("press 1 for addition")
    print("press 2 for subtraction")
    print("press 3 for multiplication")
    print(" press 4 for division")
    print("press 5 for modulus")
    print("press 6 for exponential multiplication")
    print("press 7 for exponential division")
    print("press 8 for exit")
    choice = (input("please enter the number"))
    if choice == '1' :
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        print(f"additon of {no1} and {no2} is,",no1 + no2)
    elif choice == '2' :
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        print(f"subtraction of {no1}and {no2} is", no1 - no2)
    elif choice == "3":
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        print(f"mulitplication of {no1} and {no2} is,", no1 * no2)
    elif choice == "4" :
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        print(f"division of {no1} and {no2} is,", no1 / no2)
    elif choice == "5" :
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        print(f"modulus of {no1} and {no2} is,", no1 % no2)
    elif choice == 6 :
         pass
    elif choice == 7 :
         break
    elif choice == 8 :
        exit()
    else :
        print("please enter a valid choice")

print("the task is completed")