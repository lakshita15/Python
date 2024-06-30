
numbers = [] 
list = input("Enter numbers separated by spaces: ")
string_list = list.split(" ")

for s in string_list:

    numbers.append(float(s))

largest = max(numbers)
smallest = min(numbers)


print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
