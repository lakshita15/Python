#Write a function that takes a dictionary and returns a new dictionary with the keys and values swapped.


def swap_dictionary (dict):
    result = {}
    for x in dict:
       for y in dict.values():
           result[y] = x

    return result


dict1 = {'a': 1, 'b': 2}
ans = swap_dictionary(dict1)
print(ans)