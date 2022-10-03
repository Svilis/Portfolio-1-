students = input("Input number of students:\n")
size = input("Enter the required group size:\n")

groups = float(students)//float(size)
remainder = float(students)%float(size)
print("There will be " + str(groups) + " groups with " + str(remainder) + " students left over.")
