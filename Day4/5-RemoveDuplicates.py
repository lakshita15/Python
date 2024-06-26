my_list = [2,4,7,8,3,2,3,4,5,0,8]
unique = []
for number in my_list:
    if number not in unique:
        unique.append(number)
print(unique)