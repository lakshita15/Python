String1 = "hello world"
last = "mahajan"

#BASICS
'''
print(type(String1))
print(String1[4]) #index of 4 char
print(String1[-4]) #index of 4th char but from back of the string
print(String1[0:4]) # hell print bcos 0123 index value will be printed and not 4th index
print(String1[:4]) # hell print bcos python assume 0 as starting index

another = String1[:] #prints hello world
print(String1[0:-1]) #prints hello worl
'''
# FORMATTED STRINGS
'''
MSG = print(f'{String1} [{last}] is a coder') 
'''

#STRING METHODS

# LENGTH OF STRING IS FOUND USING LEN FUNCTION => called as methods
print(len(String1))

# String1 = String1.upper() #=> method to turn string to uppercase, doesn't alter the original string, creates a new string and return that new string
print(String1.upper()) 
print(String1.upper()) 
print(String1.find("l")) 
print(String1.replace("world", "guys")) 
print(String1.replace("woorld", "guys")) #if theres a typo, it won't find it and return the original string without replacing it

# in this we have an <in> operator to find if we have some character or word in string it is similar to find but it return a boolean value
print("world" in String1) #gives True