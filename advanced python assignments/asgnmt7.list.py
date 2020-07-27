# in this code: to create an empty list... and to take names from USER.... with no same names... to enter .if same name is entered it will
# ask user to enter with different name....

name = []

x = int(input("enter the number of names to be added "))


i = 0
count= 0
j=0
def run():
    for i in range(x):
        y = input(f"enter{i} name ")

        if y in name:
            global count

            count = count +1
            print("this name already exists, please enter difrnt name")


            continue
        else:
          name.append(y)

run()
print(count)
print(f"still u need to enter {count} more different names..")
for j in range(count):
    y = input(f"please enter  name ")
    if y in name:
        print("this name already exists, please enter difrnt name")

        continue
    else:
        name.append(y)
print(name)



# outcome :  the above program is only a oneway of taking inputs from user....
 # ... in this code... there is an error becoz... while the code runs for 2nd time....if still user enters the same name again.... then
 # then the program stops there after 2nd time..