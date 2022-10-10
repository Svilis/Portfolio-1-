bad_passwords = ["password", "letmein", "sesame", "hello", "justinbieber"]

while True:
    password = input("Enter your new password:")
    password2 = input("Validate your password:")
    length = len(password)

    if password != password2:
        raise Exception("Incorrect Password")
    elif any((match := substring) in password for substring in bad_passwords):
        print("You have entered a bad password")
    else:
        print("Password Set")
        break
