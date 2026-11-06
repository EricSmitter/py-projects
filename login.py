user = []

def login():
    try:
        user = input("enter your username: ")
    except ValueError:
        print("User does not exist")
        if (createUser := input("Would you like to create an account? y/n: ")) == "y":
            newUser()
    passCheck = input("Enter your password: ")
    if passCheck == user[user + 1]:
        print("You're logged in!")
    else:
        print("Incorrect Password.")
        login()
def newUser():
    user.append(input("Enter a username: "))
    createPass()

def createPass():
    user.append(input("Create a password: "))
    check = input("Retype your password: ")
    if check == user[1]:
        pass
    else:
        print("Error: Passwords do not match")
        createPass()

login()
createPass()
