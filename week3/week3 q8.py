while True:
    num = input("Please enter a number between 0 and 12:")

    if int(num) > 12:
        print("The number you have entered is too big")
    elif int(num) > 0:
        for n in range(13):
            ans = int(n) * int(num)
            print(str(n) + " x " + str(num) + " = " + str(ans))
        break
    elif int(num) <= -1:
        new_num = abs(int(num))
        for n in reversed(range(13)):
            ans = int(n) * int(new_num)
            print(str(n) + " x " + str(new_num) + " = " + str(ans))
        break
