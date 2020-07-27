name = []

x = int(input("enter the number of names to be added "))
a=0
while a<10:
     n = input("please enter the name")
     if n not in name:
         name.append(n)
         a+= 1
     else:
         print("this name already exists")

print(name)


