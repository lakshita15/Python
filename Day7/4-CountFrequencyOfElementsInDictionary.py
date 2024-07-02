def count_frequency_in_dict (dictionary):
    freq_dict = {}
    for value in dictionary.values():
        # print(value)
        if value in freq_dict:
            freq_dict[value]+=1
        else:
            freq_dict[value] = 1
    return freq_dict



example_dict = {'a': 'apple', 'b': 'banana', 'c': 'apple', 'd': 'orange', 'e': 'banana', 'f': 'apple'}
frequency =  count_frequency_in_dict(example_dict)
print(frequency)