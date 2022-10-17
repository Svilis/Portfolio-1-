while True:
    temp = input("Enter your temp in celsius(e.g. 15C):")
    if temp[-1] == "C" or temp[-1] == "c":
        new_temp = temp[:-1]
        fah = (float(new_temp) * 9 / 5) + 32
        print(str(round(fah, 2)) + "°F")
        break
    else:
        print("Please enter a C")
    break
