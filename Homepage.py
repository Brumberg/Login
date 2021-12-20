
import Log_In_Function
import Log_Out_Function
import Sign_Up_Function

#the main homepage which gives the user different options they can choose from
def homepage():
    ValidInput = False
    print ("""---- HOMEPAGE ----
    1. Log In
    2. Sign Up
    3. Log Out""")

    #ensures that the value that the user enters is correct and then redirects the user to the relevant option
    userinput = int(input("Please choose an option from above: "))
    while ValidInput == False:
        if userinput == (1):
            ValidInput = True
            Log_In_Function.login()

        elif userinput == (2):
            ValidInput = True
            Sign_Up_Function.signup()

        elif userinput == (3):
            ValidInput = True
            Log_Out_Function.logout()

        else:
            print("Invalid Input")
            userinput = int(input("Please choose an option from above: "))
