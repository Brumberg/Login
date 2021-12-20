from Homepage import *

def signup():
    username_length_approved = False
    password_length_approved = False

    print("Welcome to the sign up page")
    username_input = input ("""Please enter the username you wish to have or type "exit" to return to the homepage: """)
    if username_input == ("exit"):
        homepage()
    else:
        #checks that the username entered has a maximum of 10 characters and loops if it is more than 10 characters
        while username_length_approved == False:
            if len(username_input) <= (10):
                username_length_approved = True
                username = (username_input)
                print("Welcome "+username+", We just need to finish setting up your account...")
            else:
                username_input = input("please enter a username with a maximum of 10 characters: ")



#allows the user to make their own password and also checks that it has a minimum of 5 characters
    password_input = input("Please enter a password (minimum 5 characters): ")
    while password_length_approved == False:
        if len(password_input) >= (5):
            password_length_approved = True
            password = (password_input)
        else:
            username_input = input("please enter a password with a minimum of 5 characters: ")

    #prints the users infomation
    useremail = input("Please enter your email: ")
    print("Great "+username+", your account is set up")
    print("Here are your details")
    print("Username - "+username)
    print("Password - " +password)
    print("Email - "+useremail)