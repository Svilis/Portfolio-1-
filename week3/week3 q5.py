bad_passwords = ["password", "letmein", "sesame", "hello", "justinbieber"]

while True:
    password = input("Enter your new password, must be between 8 and 12 characters:")
    password2 = input("Validate your password:")
    length = len(password)

    if password != password2:
        print("Passwords do not match.")
    if length < 8:
        print("Your password is too short.")
    elif length > 12:
        print("Your password is too long.")
    elif any((match := substring) in password for substring in bad_passwords):
        print("You have entered a bad password")
    else:
        print("Password Set")
        break
