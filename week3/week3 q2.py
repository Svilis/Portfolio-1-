while True:
    password = input("Enter your new password:")
    password2 = input("Validate your password:")

    if password != password2:
        raise Exception("Incorrect Password")
    else:
        print("Password Set")
        break
