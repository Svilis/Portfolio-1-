def letters(string):
    upper = 0
    lower = 0

    for i in string:
        if i == " ":
            pass
        elif i.isupper():
            upper += 1
        elif i.islower:
            lower += 1

    print("Number of upper case characters: ", upper)
    print("Number of lower case characters: ", lower)

letters("aaaa FFFF")
