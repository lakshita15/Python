
numbers = []

input_numbers = input("Enter numbers separated by spaces: ")

string_list = input_numbers.split()

for s in string_list:
    numbers.append(float(s))

unique_numbers = sorted(set(numbers))


if len(unique_numbers) >= 3:
    third_largest = unique_numbers[-3]
    print(f"Third largest number: {third_largest}")
else:
    print("Not enough unique numbers to determine the third largest number.")

if len(unique_numbers) >= 3:
    third_smallest = unique_numbers[2]
    print(f"Third smallest number: {third_smallest}")
else:
    print("Not enough unique numbers to determine the third smallest number.")
