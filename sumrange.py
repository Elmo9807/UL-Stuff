last_num = 0

for i in range(1, 11):
    sum = last_num + i
    print("Current Number", i, "Last Number", last_num, "Sum:", sum)
    last_num = i