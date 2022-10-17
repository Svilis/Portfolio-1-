from statistics import mean
temp_list = []

while True:
    temp = input("Enter a temperature: ")
    if temp == "":
        break
    else:
        temp_list.append(int(temp))

new_temp_list = list(map(int, temp_list))
avg = mean(new_temp_list)

print(max(temp_list))
print(min(temp_list))
print(avg)
