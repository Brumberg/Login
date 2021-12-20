import Homepage

username = ("sam cliffe")
password = ("12345")
LoggedIn = False

def login():
    validusername = False
    validpassword = False
    attempts = int(3)
    print("Welcome to the login page")

    #checks validity of username
    while validusername == False:
        userinput = input ("please enter your username: ")
        if userinput == username:
            validusername = True
        else:
            print("Invalid username, please try again")
            validusername = False

    #checks validity of password + gives the user 3 attempts to get the password correct
    while validpassword == False:
        userinput = input ("please enter your password: ")
        if userinput == password:
            validpassword = True
            print("welcome, "+username)
            LoggedIn = True
            Homepage.homepage()
        else:
            print("Invalid password")
            attempts = (attempts - 1)
            if attempts == (0):
                print("you have 0 attempts left")
                quit()
            else:
                print("you have",attempts,"attempts left, please try again")
            validpassword = False
