
numbers = []

input_numbers = input("Enter numbers separated by spaces: ")

string_list = input_numbers.split()

numbers = [float(s) for s in string_list]

numbers.sort()

# Find the third smallest and third largest numbers
if len(numbers) >= 3:
    third_smallest = numbers[2]
    third_largest = numbers[-3]
    print(f"Third smallest number: {third_smallest}")
    print(f"Third largest number: {third_largest}")
else:
    print("Not enough unique numbers to determine the third smallest or third largest number.")
