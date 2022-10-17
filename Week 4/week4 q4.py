def remove_last(string):
    if len(string) < 2:
        print(string)
    else:
        string2 = string[:-1]
        print(string2)


text = input("Input some text: ")
remove_last(text)
