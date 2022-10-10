while True:
    password = input("Enter your new password, must be between 8 and 12 characters:")
    password2 = input("Validate your password:")
    length = len(password)

    if length < 8:
        print("Your password is too short.")
    elif length > 12:
        print("Your password is too long.")
    elif str(password) != password2:
        raise Exception("Incorrect Password")
    else:
        print("Password Set")
        break
