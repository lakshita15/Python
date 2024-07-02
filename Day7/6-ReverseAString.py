'''
def reverse(string_list):
    pointer_1 = 0
    pointer_2 = len(string_list) - 1
    
    while pointer_1 < pointer_2:
        # Swap the elements
        string_list[pointer_1], string_list[pointer_2] = string_list[pointer_2], string_list[pointer_1]
        
        # Move the pointers towards each other
        pointer_1 += 1
        pointer_2 -= 1
    
    return string_list

string_in = input("Enter the string you want to reverse: ")

# Convert string to list
splitted_string = list(string_in)
returned_string = reverse(splitted_string)

# Convert list back to string
reversed_string = ''.join(returned_string)
print(reversed_string)


'''

def reverse(string_list):
    pointer_1 = 0
    pointer_2 = len(string_list) - 1
    
    for i in range(len(string_list)//2):
        string_list[pointer_1],string_list[pointer_2] = string_list[pointer_2],string_list[pointer_1]
    return string_list

string_in = input("Enter the string you want to reverse: ")

# Convert string to list
splitted_string = list(string_in)
returned_string = reverse(splitted_string)

# Convert list back to string
reversed_string = ''.join(returned_string)
print(reversed_string)
