def add(a, b):
    c = a + b
    print(c)

# with arguments without return type
def sub(a,b):
    c = a-b
    #print (c)

# without  arguments  with return type for multiplication
def multi():

    c = print("no parameters are passed")
    return c

# witharguments with return type
def div(a =10,b=5):
    c =a/b
    return c
# for modulus : with arguments without return type
def mod(a,b):
    c = a% b

x =mod(4,5)
print(x)


# ** without arguments with return type
def expmulti():
    a,b=4,5
    c = a**b
    return c
x = expmulti()
print(x)

# // with arguments with return type
def expdiv(a =10,b=5):
    c =a//b
    return c
y = expdiv(20,5)
print(y)



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
    if choice == '1':
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        x = add(no1,no2)
        print(x)

    elif choice == '2':
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        sub(no1,no2)
    elif choice == "3":
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        x =multi()
        print(x)
    elif choice == "4" :
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        div(no1,no2)
    elif choice == "5" :
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        mod(no1,no2)
    elif choice == 6 :
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        expmulti()
    elif choice == 7 :
        no1 = int(input("enter first number"))
        no2 = int(input("enter 2nd number"))
        expdiv(no1,no2)
    elif choice == 8 :
        exit()
    else :
        print("please enter a valid choice")

print("the task is completed")


