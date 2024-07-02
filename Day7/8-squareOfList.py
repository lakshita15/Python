def squareOfNumbers(lst):
    # Modify the list in place by iterating through indices
    for i in range(len(lst)):
        lst[i] = lst[i] * lst[i]
    return lst

# Input parsing
user_in = input("Enter a list of numbers separated by spaces: ")
print("User input:", user_in)

# Convert the input string to a list of numbers
list_in = list(map(int, user_in.split()))
print("List of numbers:", list_in)

# Get the squared numbers
square_ans = squareOfNumbers(list_in)
print("Squared numbers:", square_ans)