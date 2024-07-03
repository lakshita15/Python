#Write a function to merge two dictionaries.

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Create a copy of the first dictionary
    merged_dict.update(dict2)   # Update the copy with the second dictionary
    return merged_dict

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = merge_dicts(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
