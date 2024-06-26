#like lists but cannot be modified, list defined by [] , tuple is ()
'''
numbers = (1,2,3,4)
print(numbers[0]) # we can check length, counft, access elements but cannot change

'''

'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
'''

'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

'''