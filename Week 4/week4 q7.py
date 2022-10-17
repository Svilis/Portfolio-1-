from statistics import mean
temp_list = []
list_length = 6

for i in range(list_length):
    temp = input("Enter a temperature:")
    temp_list.append(temp)

new_temp_list = list(map(int, temp_list))
avg = mean(new_temp_list)

print(max(temp_list))
print(min(temp_list))
print(avg)
