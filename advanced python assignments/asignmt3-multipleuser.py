uname1 = 'krishna'
pword1 = '11111'
uname2 = 'rahul'
pword2 = '22222'
uname3 = 'suresh'
pword3 = '33333'
uname4 = 'ramesh'
pword4 = '44444'
uname5 = 'naresh'
pword5 = '55555'

username = input("please enter your username")

if username == uname1 :
    print("valid username")
    password = input(f"hey {username} please enter your password")
    if password == pword1 :
        print(f"hey {username} you are now logged in")
    else :
      print("incorrect password")

elif  username == uname2:
        print("valid username")
        password = input(f"hey {username} please enter your password")
        if password == pword2:
            print(f"hey {username} you are now logged in")
        else:
            print("incorrect password")

elif username == uname3:
    print("valid username")
    password = input(f"hey {username} please enter your password")
    if password == pword3 :
        print(f"hey {username} you are now logged in")
    else :
      print("incorrect password")

elif username == uname4:
    print("valid username")
    password = input(f"hey {username} please enter your password")
    if password == pword4 :
        print(f"hey {username} you are now logged in")
    else :
      print("incorrect password")

elif username == uname5 :
    print("valid username")
    password = input(f"hey {username} please enter your password")
    if password == pword5 :
        print(f"hey {username} you are now logged in")
    else :
      print("incorrect password")

else :
    print("invalid username")

