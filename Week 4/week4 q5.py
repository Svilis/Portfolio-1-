def fah_to_cel(temp):
    ans = (float(temp) - 32) * 5/9
    print(str(round(ans, 2)) + "°C")


def cel_to_fah(temp):
    ans = (float(temp) * 9/5) + 32
    print(str(round(ans, 2)) + "°F")


while True:
    c_or_f = input("Enter \"c\" or \"f\" for the temp you want to convert to:")
    c_or_f.islower()
    if c_or_f == "c":
        fah = input("Enter your temp in fahrenheit:")
        fah_to_cel(fah)
    elif c_or_f == "f":
        cel = input("Enter your temp in celsius:")
        cel_to_fah(cel)
    break
