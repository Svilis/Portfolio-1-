while True:
    num = input("Please enter a number between 0 and 12:")

    if int(num) < 0:
        print("The number you entered is too small.")
    elif int(num) > 12:
        print("The number you have entered is too big")
    else:
        for n in range(13):
            ans = int(n) * int(num)
            print(str(n) + " x " + str(num) + " = " + str(ans))
        break
